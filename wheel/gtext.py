"""
GText is a subclass of TextInput

Allows for user input, adds the "draw" method
"""
from kivy.graphics import *
from kivy.graphics.instructions import *
from kivy.uix.textinput import TextInput
from introcs.geom import Point2, Matrix
import introcs
from game2d import *

class GText(TextInput):
    """
    A class allowing for user input in a textbox
    """

    def __init__(self,**keywords):
        """
        Initializes a GText object

        Parameter keywords: dictionary of keyword arguments 
        Precondition: keys are attribute names
        """
        return super().__init__(**keywords)