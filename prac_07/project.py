class Project:
    """Project class"""
    def __init__(self, name, start_date, priority, cost, percent_complete):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percent_complete = percent_complete

    def __str__(self):
        """Return a string representation of the Project object."""
        return f"{self.name:25} {self.start_date} {self.priority:2} {self.cost:10,.2f} {self.percent_complete}%"


    def save_format(self):
        """Return a tab-separated string suitable for saving to file."""
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t"
                f"{self.priority}\t{self.cost:.2f}\t{self.percent_complete}")