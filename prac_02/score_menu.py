"""
Program for score menu
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars
(Q)uit"""

def main():
    """Implement a score menu."""
    score = ""
    print(MENU)
    choice = input(">  ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">  ").upper()
    print("Farewell")

def get_valid_score():
    """Get valid input."""
    score = int(input("Enter score: "))
    while score == "":
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_status(score):
    """Determine score status."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print corresponding stars relative to score."""
    print("*" * score)


main()
