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
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

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

    # get widgets from kv file
    textinput = ObjectProperty(None)
    button = ObjectProperty(None)

    def __init__(self):
        """
        Creates BoxLayout with widgets
        """
        pass