from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi class."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation including flagfall information."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Return the fare for the trip, including the flagfall."""
        return self.flagfall + super().get_fare()
