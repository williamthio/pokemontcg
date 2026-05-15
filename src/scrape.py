import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor
import os
from tenacity import retry, stop_after_attempt, wait_fixed
import sys
import json
import threading

CARD_CACHE_FILE = "src/data/card_cache.json"
card_cache = {}
cache_lock = threading.Lock()

def load_cache():
    global card_cache
    if os.path.exists(CARD_CACHE_FILE):
        try:
            with open(CARD_CACHE_FILE, "r") as f:
                card_cache = json.load(f)
        except Exception:
            card_cache = {}

def save_cache():
    # Called within a locked context in get_canonical_url
    with open(CARD_CACHE_FILE, "w") as f:
        json.dump(card_cache, f, indent=2)

def get_canonical_url(card_url):
    with cache_lock:
        if card_url in card_cache:
            return card_cache[card_url]
    
    try:
        response = get_with_retry(card_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        all_print_urls = set()
        # Ensure the current URL's path is included
        current_path = card_url.replace("https://limitlesstcg.com", "")
        all_print_urls.add(current_path)
        
        # Look for the Prints or Int. Prints section
        for header in soup.find_all(['h2', 'h3']):
            if "Prints" in header.text:
                table = header.find_next('table')
                if table:
                    for link in table.find_all('a', href=True):
                        # Filter for card links (e.g., /cards/ABC/123)
                        parts = link['href'].split('/')
                        if len(parts) >= 4 and parts[1] == 'cards':
                            all_print_urls.add(link['href'])
        
        # Filter for valid card paths and resolve to a canonical one
        # We sort alphabetically to ensure a deterministic canonical URL
        valid_paths = sorted([path for path in all_print_urls if len(path.split('/')) >= 4])
        
        if not valid_paths:
            return card_url
            
        canonical_url = "https://limitlesstcg.com" + valid_paths[0]
        
        with cache_lock:
            for path in valid_paths:
                full_url = "https://limitlesstcg.com" + path
                card_cache[full_url] = canonical_url
            save_cache()
            
        return canonical_url
    except Exception as e:
        print(f"Error resolving canonical URL for {card_url}: {e}")
        return card_url

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def get_with_retry(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def get_latest_tournament_id():
    url = "https://limitlesstcg.com/tournaments/jp"
    response = get_with_retry(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    first_tournament_link = soup.select_one("table.data-table a[href*='/tournaments/jp/']")
    if not first_tournament_link:
        raise ValueError("Could not find the latest tournament link.")
    latest_tournament_id = int(first_tournament_link['href'].split('/')[-1])
    return latest_tournament_id

def scrape_tournament(tournament_id):
    base_url = "https://limitlesstcg.com/tournaments/jp/{}"
    tournament_url = base_url.format(tournament_id)
    
    response = get_with_retry(tournament_url)
    if response.status_code != 200:
        print(f"Failed to access {tournament_url}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tournament_title = soup.select_one(".infobox-heading").text
    table = soup.select_one("table")
    if not table:
        print(f"No table found for {tournament_url}")
        return None
    
    print(tournament_title, tournament_url)
    
    results = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        columns = row.find_all("td")
        if len(columns) < 3:
            continue
        
        ranking = columns[0].text.strip()
        player_name = columns[1].text.strip()
        deck_link = columns[2].find("a")
        
        if not deck_link:
            continue

        pokemon_images = deck_link.find_all("img")
        main_pokemon = pokemon_images[0]['alt'] if len(pokemon_images) > 0 else ""
        secondary_pokemon = pokemon_images[1]['alt'] if len(pokemon_images) > 1 else ""
        deck_url = deck_link["href"]

        print(ranking, player_name, main_pokemon, secondary_pokemon, deck_url)
        
        # Scrape deck details
        deck_response = get_with_retry(deck_url)
        if deck_response.status_code != 200:
            print(f"Failed to access {deck_url}")
            continue
        
        deck_soup = BeautifulSoup(deck_response.text, 'html.parser')
        deck_columns = deck_soup.find_all("div", {"class": "decklist-column"})
        
        deck_cards = []
        types = ['P', 'T', 'E']  # P for Pokemon, T for Trainer, E for Energy
        for idx, column in enumerate(deck_columns):
            for card in column.find_all("div", {"class": "decklist-card"}):
                card_count = card.find("span", {"class": "card-count"}).text.strip()
                card_name = card.find("span", {"class": "card-name"}).text.strip()
                card_url = "https://limitlesstcg.com" + card.find("a", {"class": "card-link"})['href']
                
                if card_count and card_name and card_url:
                    canonical_url = get_canonical_url(card_url)
                    deck_cards.append(f"{types[idx]}#{card_name}#{card_count}#{canonical_url}")
        
        results.append([tournament_url, player_name, main_pokemon, secondary_pokemon, deck_url, ranking, '|'.join(deck_cards)])
    
    return results

def save_progress(tournament_id):
    with open("src/data/progress.txt", "a") as f:
        f.write(f"{tournament_id}\n")

def load_progress():
    if not os.path.exists("src/data/progress.txt"):
        return set()
    with open("src/data/progress.txt") as f:
        return set(int(line.strip()) for line in f)

def sort_csv(file_path):
    with open(file_path, newline='', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        sorted_rows = sorted(reader, key=lambda row: (row[0], int(row[5])))

    with open(file_path, 'w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(sorted_rows)

def main():
    load_cache()
    end_tournament_id = get_latest_tournament_id()
    start_tournament_id = 1839
    num_threads = os.cpu_count() or 5  # Use max threads available

    completed_tournaments = load_progress()

    file_exists = os.path.isfile("src/data/tournament_decks.csv")
    
    with open("src/data/tournament_decks.csv", "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        if not file_exists:
            csv_writer.writerow(["tournamenturl", "playername", "mainpokemon", "secondarypokemon", "deckurl", "rank", "cards"])
        
        tournament_ids = [tid for tid in range(start_tournament_id, end_tournament_id + 1) if tid not in completed_tournaments]
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = executor.map(scrape_tournament, tournament_ids)
            
            for tournament_id, result in zip(tournament_ids, futures):
                if result:
                    for row in result:
                        csv_writer.writerow(row)
                    save_progress(tournament_id)
    
    sort_csv("src/data/tournament_decks.csv")

if __name__ == "__main__":
    main()
