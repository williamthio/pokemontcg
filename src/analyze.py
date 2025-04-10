import os
import csv
import pandas as pd
from collections import defaultdict, Counter
from jinja2 import Environment, FileSystemLoader
import shutil

def parse_deck_section(cards):
    parsed_cards = []
    for card in cards.split("|"):
        card_type, card_name, count, card_url = card.split("#")
        section_type = "Pokémon" if card_type == "P" else "Trainer" if card_type == "T" else "Energy"
        parsed_cards.append((section_type, card_name, int(count), card_url))
    return parsed_cards

def parse_decks(file_content, main_pokemon=None, secondary_pokemon=None, min_rank=None):
    reader = csv.DictReader(file_content.splitlines())
    all_cards = {
        "Pokémon": defaultdict(list),
        "Trainer": defaultdict(list),
        "Energy": defaultdict(list)
    }
    deck_count = 0
    deck_info = []

    for row in reader:
        if main_pokemon is not None and row['mainpokemon'] != main_pokemon:
            continue
        if secondary_pokemon is not None and row['secondarypokemon'] != secondary_pokemon:
            continue
        if min_rank is not None and int(row['rank']) > min_rank:
            continue

        deck_info.append([v for k, v in row.items() if k != 'cards'])

        deck_count += 1
        deck_cards = {
            "Pokémon": defaultdict(int),
            "Trainer": defaultdict(int),
            "Energy": defaultdict(int)
        }
        cards = row['cards']

        for section_type, card_name, count, card_url in parse_deck_section(cards):
            deck_cards[section_type][f'{card_name} ({card_url})'] = count

        for section_type in all_cards:
            for card_name in deck_cards[section_type]:
                count = deck_cards[section_type][card_name]
                all_cards[section_type][card_name].append(count)
    
    print(f"main_pokemon: {main_pokemon}, secondary_pokemon: {secondary_pokemon}, min_rank: {min_rank}, deck_count: {deck_count}")

    return all_cards, deck_count, deck_info

def calculate_card_distribution(all_cards, deck_count):
    distributions = {}
    for section_type, cards in all_cards.items():
        distributions[section_type] = {}
        for card, counts in cards.items():
            count_freq = Counter(counts)
            count_freq = {
                count: freq / deck_count
                for count, freq in count_freq.items()
            }

            if sum(count_freq.values()) < 1.0:
                count_freq[0] = 1.0 - sum(count_freq.values())

            distributions[section_type][card] = {
                count: percentage
                for count, percentage in sorted(count_freq.items())
            }
    return distributions

def get_top_combinations(deck_info, top_n=50):
     combination_counts = Counter((info[2], info[3]) for info in deck_info)
     return combination_counts.most_common(top_n)

def clean_docs_folder():
    if os.path.exists("docs"):
        for item in os.listdir("docs"):
            if item not in ["css", "js"]:
                item_path = os.path.join("docs", item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
    os.makedirs("docs", exist_ok=True)

def generate_html_report(card_distributions, deck_info):
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template('cluster_report.html')
    return template.render(card_distributions=card_distributions, deck_info=deck_info)

def generate_index_html(summaries):
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template('index.html')
    return template.render(summaries=summaries)

if __name__ == "__main__":
    clean_docs_folder()

    with open("src/data/tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    all_cards, deck_count, deck_info = parse_decks(file_content)
    top_combinations = get_top_combinations(deck_info)

    summaries = []
    for rank, ((main, secondary), count) in enumerate(top_combinations, start=1):
        report_links = {}
        for min_rank in [1, 4, 8, 16]:
            filtered_cards, filtered_count, filtered_info = parse_decks(file_content, main_pokemon=main, secondary_pokemon=secondary, min_rank=min_rank)
            filtered_distributions = calculate_card_distribution(filtered_cards, filtered_count)
            filtered_report = generate_html_report(filtered_distributions, filtered_info)

            report_filename = f"{main}_{secondary}_top_{min_rank}.html".replace(" ", "_")
            with open("docs/" + report_filename, "w", encoding="utf-8") as f:
                f.write(filtered_report)
            report_links[min_rank] = report_filename
        
        summaries.append({
            "rank": rank,
            "main": main,
            "secondary": secondary,
            "count": count,
            "report_links": report_links
        })

    index_html = generate_index_html(summaries)
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)