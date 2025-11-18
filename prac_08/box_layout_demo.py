from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Simple demo app showing how to use a BoxLayout with event handlers."""
    def build(self):
        """Load the interface from the kv file and return the root widget."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Update the output label with a greeting based on the text input."""
        print('test')
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear both the TextInput and the output label."""
        print('clear')
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
