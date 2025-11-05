"""
Guitar
Estimate: 10 minutes
Actual:   5 minutes
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name, year=0, cost=0):
        """Initialise guitar properties."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Give a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by year."""
        return self.year < other.year
