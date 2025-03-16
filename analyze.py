import os
import csv
import argparse
from collections import defaultdict, Counter

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
        if main_pokemon and secondary_pokemon and (row['mainpokemon'].lower() != main_pokemon.lower() or row['secondarypokemon'].lower() != secondary_pokemon.lower()):
            continue
        if main_pokemon and row['mainpokemon'].lower() != main_pokemon.lower() and row['secondarypokemon'].lower() != main_pokemon.lower():
            continue
        if min_rank and int(row['rank']) > min_rank:
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
    
    print(f"Found {deck_count} decks")

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

<div style="display: flex;">
<div style="flex: 1; margin-right: 10px;">
"""

    # Pokémon Table
    markdown_content += "\n\n### Pokémon\n\n"
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
    markdown_content += "\n\n### Trainer\n\n"
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
    markdown_content += "\n\n### Energy\n\n"
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
<tr><th>Tournament</th><th>Rank</th><th>Player Name</th><th>Main Pokémon</th><th>Secondary Pokémon</th><th>Deck</th></tr>
"""
    for info in deck_info:
        tournament_url = info[0]
        tournament_id = tournament_url.split("/")[-1]
        markdown_content += f"<tr><td><a href='{tournament_url}'>{tournament_id}</a></td><td>{info[5]}</td><td>{info[1]}</td><td>{info[2]}</td><td>{info[3]}</td><td><a href='{info[4]}'>link</a></td></tr>"

    markdown_content += "</table>"

    return markdown_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Pokémon TCG decks.")
    parser.add_argument("--main_pokemon", type=str, default=None, help="Main Pokémon to filter decks.")
    parser.add_argument("--secondary_pokemon", type=str, default=None, help="Secondary Pokémon to filter decks.")
    parser.add_argument("--min_rank", type=str, default=None, help="Minimum rank to filter decks.")

    args = parser.parse_args()

    main_pokemon = args.main_pokemon.strip() if args.main_pokemon != '' else None
    secondary_pokemon = args.secondary_pokemon.strip() if args.secondary_pokemon != '' else None
    min_rank = int(args.min_rank.strip()) if args.min_rank and args.min_rank != '' else None

    with open("tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    all_cards, deck_count, deck_info = parse_decks(file_content, main_pokemon, secondary_pokemon, min_rank)
    card_distributions = calculate_card_distribution(all_cards, deck_count)
    markdown_report = generate_markdown_report(card_distributions, deck_info)

    report_file = f"reports/{main_pokemon}_{secondary_pokemon}_{min_rank:02d}.md"

    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)
