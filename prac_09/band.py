from musician import Musician

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician: Musician):
        self.musicians.append(musician)

    def play(self):
        return '\n'.join(musician.play() for musician in self.musicians)