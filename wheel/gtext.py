"""
GText utilizes TextInput

Allows for user input, adds the "draw" method
"""
from kivy.graphics import *
from kivy.graphics.instructions import *
import kivy
import kivy.app
from game2d import *
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import *

class GText(kivy.app.App):
    """
    A class allowing for user input in a textbox
    """

    def build(self):
        """
        Initializes the graphics window
        """
        return AnswerInput()

class AnswerInput(BoxLayout):
    """
    Creates BoxLayout in kivy
    """

    Builder.load_file('gtext.kv')

    def __init__(self):
        """
        Creates BoxLayout with widgets
        """
        super().__init__(orientation='vertical',height='200px',size_hint_y=None)

        self.textinput = TextInput(size_hint_x=0.5,size_hint_y=0.8)
        self.button = Button(text='Generate Wheel',background_color='blue',font_size=15,
        size_hint_x=0.5,size_hint_y=0.2)

        self.add_widget(self.textinput)
        self.add_widget(self.button)

        # bind button for functionality
        self.button.bind(on_press=self.pressed)
    
    def pressed(self):
        pass