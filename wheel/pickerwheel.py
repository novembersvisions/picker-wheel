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
from wheelapp import Wheel

class PickerWheel(kivy.app.App):
    """
    A class allowing for user input in a textbox
    """

    def build(self):
        """
        Initializes the graphics window
        """
        return AnswerInput()

    def update(self, input):
        """
        Obtains input from Wheel
        Controls appearance of textbox and initial message

        Parameter input: information about the mouse/keyboard
        Precondition: must be an instance of GInput
        """
        if Wheel.getState() == 0:
            if self.input.is_key_down('s'):
                Wheel.setState(1)
        
        if self._state == 1:
            self.loading()

    
    def loading(self):
        """
        Happens when the wheel is loading
        """
        Wheel.setMessage(None)

class AnswerInput(BoxLayout):
    """
    Creates BoxLayout in kivy
    """
    pass