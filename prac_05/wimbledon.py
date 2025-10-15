"""
Wimbledon
Estimate: 30 minutes
Actual:   50 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Load, process and display data for Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_country_champion(champion_to_count, countries)


def process_records(records):
    """Process records, create a dictionary of champions and set of countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def load_records(filename):
    """Load records from a CSV file in a list of lists"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def display_country_champion(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
