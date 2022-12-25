"""
GText is a subclass of TextInput, which allows for user input

Adds the "draw" method
"""
from kivy.graphics import *
from kivy.graphics.instructions import *
from kivy.uix.textinput import TextInput
from introcs.geom import Point2, Matrix
import introcs

class GText(TextInput):
    """
    TextInput object from kivy with added functionality
    """

    def draw(self, view):
        """
        Draws this shape in the provided view.

        param view view to draw to
        type view  :class:`GView`
        """
        try:
            view.draw(self._cache)
        except:
            raise IOError('Cannot draw %s since it was not initialized properly' % repr(self))