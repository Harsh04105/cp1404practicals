"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    """Get input and print output."""
    score = float(input("Enter score: "))
    print(determine_status(score))

    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print(determine_status(random_score))


def determine_status(score: float):
    """Determine score status."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
