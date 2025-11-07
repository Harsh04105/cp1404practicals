"""
project_management
Estimate: 30 minutes
Actual:   45 minutes
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
                load_projects(in_filename)
                print(f"Loaded {len(projects)} projects from {in_filename} ")
            except FileNotFoundError:
                print("File not found")

        elif choice == "S":

            save_projects()
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
        choice = input(">>> ")
    print("Would you like to save to projects.txt")


def load_projects(filename):
    """Read projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            name, start_date, priority, cost, percent_complete = line.strip().split("\t")
            projects.append(Project(name, int(start_date), int(priority), float(cost), float(percent_complete)))
    return projects


main()
