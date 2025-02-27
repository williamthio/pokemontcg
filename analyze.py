import csv
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

    for row in reader:
        if main_pokemon and secondary_pokemon and (row['mainpokemon'].lower() != main_pokemon.lower() or row['secondarypokemon'].lower() != secondary_pokemon.lower()):
            continue
        if main_pokemon and row['mainpokemon'].lower() != main_pokemon.lower() and row['secondarypokemon'].lower() != main_pokemon.lower():
            continue
        if min_rank and int(row['rank']) > min_rank:
            continue

        print([v for k, v in row.items() if k != 'cards'])

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
    
    print(f"\nFound {deck_count} decks")

    return all_cards, deck_count


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


if __name__ == "__main__":
    mainpokemon_filter = None
    secondarypokemon_filter = None

    # mainpokemon_filter = 'noctowl'
    mainpokemon_filter = 'charizard'
    # mainpokemon_filter = 'dragapult'
    # secondarypokemon_filter = 'charizard'
    # secondarypokemon_filter = 'noctowl'
    # secondarypokemon_filter = 'pidgeot'
    # secondarypokemon_filter = 'dusknoir'
    secondarypokemon_filter = 'dudunsparse'

    min_rank = 4

    with open("tournament_decks.csv", "r", encoding="utf-8") as f:
        file_content = f.read()

    all_cards, deck_count = parse_decks(file_content, mainpokemon_filter, secondarypokemon_filter, min_rank)
    card_distributions = calculate_card_distribution(all_cards, deck_count)

    for section_type, cards in card_distributions.items():
        print(f"\n{section_type}:")
        for card, distribution in cards.items():
            print(card)
            for count, percentage in sorted(distribution.items(),
                                            key=lambda x: -x[1]):
                print(f"  - {percentage:.3f} use {count}")
