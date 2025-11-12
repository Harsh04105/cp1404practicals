"""
project
Estimate: 15 minutes
Actual:   20 minutes
"""


DATE_FORMAT = "%m/%d/%Y"

class Project:
    """Project class"""

    def __init__(self, name, start_date, priority, cost, percent_complete):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost = float(cost)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        """Return a string representation of the Project object."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, "
                f"priority {self.priority}, estimate: ${self.cost:,.2f}, "
                f"completion: {self.percent_complete}%")

    def __lt__(self, other):
        """Sort Project objects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is at 100%."""
        return self.percent_complete == 100

    def save_format(self):
        """Return a tab-separated string suitable for saving to file."""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost:.2f}\t{self.percent_complete}")
