"""
Module that constructs a picker wheel interface based on user input
Uses game2d module from CS 1110
"""
from game2d import *

class Wheel(GameApp):
    """
    Primary class for the picker wheel
    Extends GameApp from game2d and utilizes kivy

    Methods: 
    start - initializes application
    update - controls animations based on position
    draw - displays objects on screen

    Inherited attributes:
    view - the game view, used in drawing (invariant: view is an instance of GView)
    input - the user input (invariant: input is an instance of GInput)
    """

    # ATTRIBUTES

    # Attribute _text (mutable): the list of text to be displayed on the picker wheel
    # Invariant: _text is a list containing strings

    # Attribute _labels (mutable): the list of GLabels to be displayed
    # Invariant: _labels is a list containing GLabels

    # Attribute _triangle (mutable): triangle fan of the picker wheel
    # Invariant: _triangle is a GPolygon object

    # Attribute _randcolor (immutable): a list of colors for the wheel _fillcolor attribute
    # Invariant: _randcolor is a list containing strings

    # Attribute _message: the currently active message
    # Invariant: _message is a GLabel, or None

    # Attribute _textbox: textbox for user input
    # Invariant: _textbox is a TextInput object

    # Attribute _state: initialized as 0; controls steps of the app
    # Invariant: _state is an int

    # GETTERS AND SETTERS

    def getMessage(self):
        """
        Returns the message displayed
        """
        return self._message

    def setMessage(self,value):
        """
        Sets the message to the given value

        Parameter value: what to set _message
        Precondition: value must be a GLabel or None
        """
        assert isinstance(value,GLabel) or value == None

        self._message = value

    def getState(self):
        """
        Returns the state of the app
        """
        return self._state

    def setState(self,value):
        """
        Sets the state to the given value

        Parameter value: what to set _state
        Precondition: value must be an int
        """
        assert isinstance(value,int)

        self._state = value

    # INITIALIZER

    def start(self):
        """
        Initializes the picker wheel
        Called once the application is running
        """
        self._message = GLabel(text='Welcome \n What text do you want on the wheel?',
        font_size=30,x=self.width/2, 
        y=500, linecolor='black')

        self._state = 0
        #self._textbox.update(self.input)

    def update(self,dt):
        """
        Animates the wheel, updates list of text

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        #self._text = self._textbox.text
        pass

    def draw(self):
        """
        Draws the objects to the view
        """
        if self._state == 0:
            self._message.draw(self.view)