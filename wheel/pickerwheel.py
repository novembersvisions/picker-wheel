"""
PickerWheel utilizes TextInput

Allows for user input, adds the "draw" method
"""
from kivy.graphics import *
from kivy.graphics.instructions import *
import kivy
import kivy.app
from game2d import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import *

class PickerWheel(kivy.app.App):
    """
    A class allowing for user input in a textbox
    """

    def build(self):
        """
        Initializes the graphics window
        """
        return AnswerInput()

    
    def loading(self):
        """
        Happens when the wheel is loading
        """
        pass

class AnswerInput(BoxLayout):
    """
    Creates BoxLayout in kivy
    """
    pass