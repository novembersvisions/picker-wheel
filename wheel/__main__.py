"""
Main application script for picker wheel
"""
from wheelapp import *
from pickerwheel import *

# Application code
if __name__ == '__main__':
    Wheel(width=800,height=700).run()
    PickerWheel().run()