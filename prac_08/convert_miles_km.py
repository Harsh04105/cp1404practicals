from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMiles(App):
    """Conversion app."""
    message = StringProperty()

    def build(self):
        """Build the app from the kv file."""
        self.title = "Convert Miles"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press Enter"
        return self.root

    def handle_calculate(self):
        """ Handle calculation and output result to label widget."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        """Handle up/down button press."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


ConvertMiles().run()
