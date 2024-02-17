# Import necessary Kivy modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical')

        # Create a label
        self.my_label = Label(text="Hello, Kivy!")

        # Create a button
        my_button = Button(text="Update Label", on_press=self.update_label)

        # Add widgets to the layout
        layout.add_widget(self.my_label)
        layout.add_widget(my_button)

        return layout

    def update_label(self, instance):
        # Update the label's text
        self.my_label.text = "Button pressed!"

if __name__ == '__main__':
    MyApp().run()
