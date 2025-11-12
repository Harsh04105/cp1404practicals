"""
project_management
Estimate: 2 hours
Actual:   6 hours
"""
import datetime
from operator import attrgetter
from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project \n- (Q)uit"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n"


def main():
    """Run the project management menu program."""
    projects = load_projects(FILENAME)
    print("Welcome to Phytonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            try:
                in_filename = input("Filename: ")
                projects = load_projects(in_filename)
                print(f"Loaded {len(projects)} projects from {in_filename} ")
            except FileNotFoundError:
                print("File not found")
        elif choice == "S":
            save_load_file = input("Filename: ")
            save_projects(projects, save_load_file)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_file = input("Would you like to save to projects.txt: ").lower()
    if save_file.startswith("y"):
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software")


def load_projects(filename):
    """Read projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            name, start_date, priority, cost, percent_complete = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost), int(percent_complete)))
    return projects


def save_projects(projects, filename):
    """Write projects to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        out_file.write(HEADER)
        for project in projects:
            print(project.save_format(), file=out_file)
    print(f"Saved {len(projects)} projects to {FILENAME}")


def display_projects(projects):
    """Display incomplete then completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f" {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f" {project}")


def filter_projects_by_date(projects):
    """Ask for a date and show projects that start on/after that date."""
    sort_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    filtered_projects = [project for project in projects if project.start_date >= sort_date]
    for project in sorted(filtered_projects, key=attrgetter("start_date")):
        print(project)


def add_project(projects):
    """Prompt for details and append a new Project to memory."""
    print("Lets add a new project")
    name = get_valid_input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ")
    cost = get_valid_number("Cost estimate: $", is_float=True)
    percent_complete = get_valid_number("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost, percent_complete))


def get_valid_date(prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            date = input(prompt)
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Not a valid date. Try again.")
    return date # Ignore error


def get_valid_input(prompt):
    user_input = input(prompt)
    while user_input == "":
        print("Input cannot be empty. Try again.")
        user_input = input(prompt)
    return user_input


def get_valid_number(prompt, is_float=False):
    """Get a valid number from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = input(prompt)
            number = float(user_input) if is_float else int(user_input)

            if number < 0:
                print("Number must be >= 0.")
            else:
                is_valid_input = True
        except ValueError:
            print("Not a valid number. Try again.")
    return number # Ignore error


def get_optional_number(prompt):
    """Ask for a number or blank to skip."""
    user_input = input(prompt)
    if user_input == "":
        return ""

    is_valid_input = False
    while not is_valid_input:
        try:
            value = int(user_input)
            is_valid_input = True
        except ValueError:
            print("Not a valid number. Try again.")
            user_input = input(prompt)
            if user_input == "":
                return ""  # allow cancel on re-try
    return value # Ignore error


def update_project(projects):
    """Update completion/priority"""
    for i, project in enumerate(projects):
        print(i, project)
    choice = get_valid_number("Project choice: ")
    selected_project = projects[choice]
    print(selected_project)

    new_percentage = get_optional_number("New percentage: ")
    selected_project.percent_complete = new_percentage if new_percentage != "" else selected_project.percent_complete

    new_priority = get_optional_number("New priority: ")
    selected_project.priority = new_priority if new_priority != "" else selected_project.priority


main()
