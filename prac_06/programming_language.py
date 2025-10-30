"""
Programming Languages
Estimate: 30 minutes
Actual:   36 minutes
"""


class ProgrammingLanguage:
    """Represent a ProgramingLanguage object."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialize a ProgrammingLanguage."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check condition."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
