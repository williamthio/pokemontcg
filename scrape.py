import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor
import os
from tenacity import retry, stop_after_attempt, wait_fixed
import sys

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def get_with_retry(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

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
                    deck_cards.append(f"{types[idx]}#{card_name}#{card_count}#{card_url}")
        
        results.append([tournament_url, player_name, main_pokemon, secondary_pokemon, deck_url, ranking, '|'.join(deck_cards)])
    
    return results

def save_progress(tournament_id):
    with open("progress.txt", "a") as f:
        f.write(f"{tournament_id}\n")

def load_progress():
    if not os.path.exists("progress.txt"):
        return set()
    with open("progress.txt") as f:
        return set(int(line.strip()) for line in f)

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape.py <end_tournament_id>")
        sys.exit(1)
    
    end_tournament_id = int(sys.argv[1])
    start_tournament_id = 1839
    num_threads = os.cpu_count() or 5  # Use max threads available

    completed_tournaments = load_progress()

    file_exists = os.path.isfile("tournament_decks.csv")
    
    with open("tournament_decks.csv", "a", newline="", encoding="utf-8") as csv_file:
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

if __name__ == "__main__":
    main()
