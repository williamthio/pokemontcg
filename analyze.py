import os
import csv
import pandas as pd
from collections import defaultdict, Counter
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


def generate_markdown_report(card_distributions, deck_info):
    markdown_content = """
## Deck Analysis

<div style="display: flex; flex-wrap: wrap;">
<div style="flex: 1; margin-right: 10px;">
"""

    # Pokémon Table
    markdown_content += "<h3>Pokémon</h3>"
    markdown_content += "<table><tr><th>Card</th><th>Count</th><th>Percentage</th></tr>"
    for card, distribution in card_distributions["Pokémon"].items():
        card_name, card_url = card.split(" (")
        card_url = card_url.rstrip(")")
        markdown_content += f"<tr><td rowspan='{len(distribution)}'><a href='{card_url}'>{card_name}</a></td>"
        for i, (count, percentage) in enumerate(sorted(distribution.items(), key=lambda x: -x[1])):
            if i > 0:
                markdown_content += "<tr>"
            markdown_content += f"<td>{count}</td><td>{percentage:.3f}</td></tr>"
    markdown_content += "</table>\n"

    markdown_content += "</div><div style='flex: 1; margin-right: 10px;'>"

    # Trainer Table
    markdown_content += "<h3>Trainer</h3>"
    markdown_content += "<table><tr><th>Card</th><th>Count</th><th>Percentage</th></tr>"
    for card, distribution in card_distributions["Trainer"].items():
        card_name, card_url = card.split(" (")
        card_url = card_url.rstrip(")")
        markdown_content += f"<tr><td rowspan='{len(distribution)}'><a href='{card_url}'>{card_name}</a></td>"
        for i, (count, percentage) in enumerate(sorted(distribution.items(), key=lambda x: -x[1])):
            if i > 0:
                markdown_content += "<tr>"
            markdown_content += f"<td>{count}</td><td>{percentage:.3f}</td></tr>"
    markdown_content += "</table>\n"

    markdown_content += "</div><div style='flex: 1; margin-right: 10px;'>"

    # Energy Table
    markdown_content += "<h3>Energy</h3>"
    markdown_content += "<table><tr><th>Card</th><th>Count</th><th>Percentage</th></tr>"
    for card, distribution in card_distributions["Energy"].items():
        card_name, card_url = card.split(" (")
        card_url = card_url.rstrip(")")
        markdown_content += f"<tr><td rowspan='{len(distribution)}'><a href='{card_url}'>{card_name}</a></td>"
        for i, (count, percentage) in enumerate(sorted(distribution.items(), key=lambda x: -x[1])):
            if i > 0:
                markdown_content += "<tr>"
            markdown_content += f"<td>{count}</td><td>{percentage:.3f}</td></tr>"
    markdown_content += "</table>\n"

    markdown_content += "</div></div>"

    markdown_content += """

## Deck Information

<table>
<tr><th>TID</th><th>#</th><th>Main</th><th>Secondary</th></tr>
"""
    for info in deck_info:
        tournament_url = info[0]
        tournament_id = tournament_url.split("/")[-1]
        markdown_content += f"<tr><td><a href='{tournament_url}'>{tournament_id}</a></td><td>{info[5]}</td><td><a href='{info[4]}'>{info[2]}</a></td><td><a href='{info[4]}'>{info[3]}</a></td></tr>"

    markdown_content += "</table>"

    return markdown_content


if __name__ == "__main__":
    if os.path.exists("reports"):
        shutil.rmtree("reports")
    os.makedirs("reports")

    with open("clustered_tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    # Load data into pandas DataFrame
    data = pd.read_csv("clustered_tournament_decks.csv")

    # Generate cluster summary
    cluster_summary = data.groupby('cluster').agg(
        mean_rank=('rank', 'mean'),
        cluster_size=('cluster', 'size'),
        main_pokemon=('mainpokemon', lambda x: x.mode()[0] if not x.mode().empty else None),
        secondary_pokemon=('secondarypokemon', lambda x: x.mode()[0] if not x.mode().empty else None),
    ).reset_index()

    # Sort by mean rank and cluster size
    cluster_summary = cluster_summary.sort_values(by=['mean_rank', 'cluster_size'])

    readme_table = "| Cluster | Mean Rank | Main Pokémon | Secondary Pokémon | Deck Count |\n"
    readme_table += "|---------|-----------|--------------|-------------------|------------|\n"

    for _, row in cluster_summary.iterrows():
        cluster = row['cluster']
        mean_rank = row['mean_rank']
        main_pokemon = row['main_pokemon']
        secondary_pokemon = row['secondary_pokemon']
        cluster_size = row['cluster_size']

        report_filename = f"reports/cluster_{cluster}.md"
        filtered_cards, filtered_count, filtered_info = parse_decks(file_content, cluster=cluster)
        filtered_distributions = calculate_card_distribution(filtered_cards, filtered_count)
        filtered_report = generate_markdown_report(filtered_distributions, filtered_info)

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(filtered_report)

        readme_table += f"| [{cluster}]({report_filename}) | {mean_rank:.2f} | {main_pokemon} | {secondary_pokemon} | {cluster_size} |\n"

    # Update README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Pokémon TCG Deck Analysis\n\n")
        f.write("## Cluster Analysis\n\n")
        f.write(readme_table)
