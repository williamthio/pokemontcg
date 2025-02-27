import csv
from collections import defaultdict, Counter

MAIN_POKEMON = "charizard"
SECONDARY_POKEMON = "dudunsparce"
MIN_RANK = 4

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


def generate_html_report(card_distributions, deck_info):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Card Distribution Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .container { max-width: 1280px; margin: 0 auto; padding: 20px; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .card-table { width: 30%; display: inline-block; vertical-align: top; margin-right: 2%; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Card Distribution Report</h1>
    """

    for section_type, cards in card_distributions.items():
        html_content += f"<div class='card-table'><h2>{section_type}</h2><table><tr><th>Card</th><th>Count</th><th>Percentage</th></tr>"
        for card, distribution in cards.items():
            card_name, card_url = card.split(" (")
            card_url = card_url.rstrip(")")
            html_content += f"<tr><td rowspan='{len(distribution)}'><a href='{card_url}'>{card_name}</a></td>"
            for i, (count, percentage) in enumerate(sorted(distribution.items(), key=lambda x: -x[1])):
                if i > 0:
                    html_content += "<tr>"
                html_content += f"<td>{count}</td><td>{percentage:.3f}</td></tr>"
        html_content += "</table></div>"

    html_content += """
            <h2>Deck Information</h2>
            <table>
                <tr><th>Tournament URL</th><th>Player Name</th><th>Main Pokémon</th><th>Secondary Pokémon</th><th>Deck URL</th><th>Rank</th></tr>
    """
    for info in deck_info:
        html_content += f"<tr><td><a href='{info[0]}'>{info[0]}</a></td><td>{info[1]}</td><td>{info[2]}</td><td>{info[3]}</td><td><a href='{info[4]}'>{info[4]}</a></td><td>{info[5]}</td></tr>"

    html_content += """
            </table>
        </div>
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    with open("tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    all_cards, deck_count, deck_info = parse_decks(file_content, MAIN_POKEMON, SECONDARY_POKEMON, MIN_RANK)
    card_distributions = calculate_card_distribution(all_cards, deck_count)
    html_report = generate_html_report(card_distributions, deck_info)

    with open("card_distribution_report.html", "w", encoding="utf-8") as f:
        f.write(html_report)
