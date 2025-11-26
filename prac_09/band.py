from musician import Musician


class Band:
    """Band class"""

    def __init__(self, name):
        """Initialise a Band with a name and an empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician: Musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return each musician’s play output."""
        return '\n'.join(musician.play() for musician in self.musicians)
