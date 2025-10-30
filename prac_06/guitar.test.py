"""
Guitar.test
Estimate: 20 minutes
Actual:    14 minutes
"""

from prac_06.guitar import Guitar


def main():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 2000)

    print(f"{first_guitar.name} get_age() - Expected 103. Got {first_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")

    print(f"\n{first_guitar.name} is_vintage() - Expected True. Got {first_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage) - Expected False. Got {another_guitar.is_vintage()}")


main()
