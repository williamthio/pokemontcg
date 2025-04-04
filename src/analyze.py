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

def parse_decks(file_content, cluster=None):
    reader = csv.DictReader(file_content.splitlines())
    all_cards = {
        "Pokémon": defaultdict(list),
        "Trainer": defaultdict(list),
        "Energy": defaultdict(list)
    }
    deck_count = 0
    deck_info = []

    for row in reader:
        if cluster is not None and int(row['cluster']) != cluster:
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

def generate_html_report(card_distributions, deck_info, cluster):
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template('cluster_report.html')
    return template.render(card_distributions=card_distributions, deck_info=deck_info, cluster=cluster)

def generate_index_html(cluster_summary):
    env = Environment(loader=FileSystemLoader('src/templates'))
    template = env.get_template('index.html')
    return template.render(cluster_summary=cluster_summary)

if __name__ == "__main__":
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    else:
        os.makedirs("docs")

    with open("src/data/clustered_tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    data = pd.read_csv("src/data/clustered_tournament_decks.csv")

    cluster_summary = data.groupby('cluster').agg(
        mean_rank=('rank', 'mean'),
        cluster_size=('cluster', 'size'),
        main_pokemon=('mainpokemon', lambda x: x.mode()[0] if not x.mode().empty else None),
        secondary_pokemon=('secondarypokemon', lambda x: x.mode()[0] if not x.mode().empty else None),
    ).reset_index()

    cluster_summary = cluster_summary.sort_values(by=['mean_rank', 'cluster_size'])

    for _, row in cluster_summary.iterrows():
        cluster = row['cluster']
        mean_rank = row['mean_rank']
        main_pokemon = row['main_pokemon']
        secondary_pokemon = row['secondary_pokemon']
        cluster_size = row['cluster_size']

        filtered_cards, filtered_count, filtered_info = parse_decks(file_content, cluster=cluster)
        filtered_distributions = calculate_card_distribution(filtered_cards, filtered_count)
        filtered_report = generate_html_report(filtered_distributions, filtered_info, cluster)

        report_filename = f"docs/cluster_{cluster}.html"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(filtered_report)

    index_html = generate_index_html(cluster_summary)
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)