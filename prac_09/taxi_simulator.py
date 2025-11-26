from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator by setting up a list of taxis, track the user's current taxi,
    manages the running bill, and handle the input loop."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                bill_to_date += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi trip."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        current_taxi = taxis[choice]
    except (ValueError, IndexError):
        print("Invalid choice")
        current_taxi = None
    return current_taxi


def drive_taxi(taxi):
    """Ask for a distance to drive, run the taxi trip, and return its fare."""
    try:
        distance = int(input("Drive how far? "))
    except ValueError:
        distance = 0
    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


main()
