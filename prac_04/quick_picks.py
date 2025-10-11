"""
Quick Pick Program
"""

import random

MAXIMUM = 45
MINIMUM = 1
NUMBERS_PER_LINE = 6


def main():
    """Generate non-repeating random numbers from 1 to MAXIMUM for n number of picks."""
    number_of_quick_picks = int(input("How many quick picks: "))
    while number_of_quick_picks < 0:
        print("Must be > 0")
        number_of_quick_picks = int(input("How many quick picks: "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
