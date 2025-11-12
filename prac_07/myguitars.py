"""
myguitars
Estimate: 30 minutes
Actual:   45 minutes
"""


import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read and display guitars from csv file and then let users add to the file."""
    guitars = load_guitars(FILENAME)
    print(f"{len(guitars)} guitars loaded.\n")

    display_guitars(guitars)
    guitars.sort()
    add_guitar(guitars)
    save_guitars(guitars)
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars from CSV into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            if not row:
                continue
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display all guitars in the file."""
    print("Guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    print()


def add_guitar(guitars):
    """Let the user add guitars."""
    print("Add new guitars (blank name to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{name} ({year}) : ${cost:,.2f} added")
        name = input("\nName: ")


def save_guitars(guitars):
    """Save all guitars back to CSV."""
    with open(FILENAME, "w", newline="") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    print(f"{len(guitars)} guitars saved to {FILENAME}")


main()
