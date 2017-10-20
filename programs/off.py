import time
from neopixel import *

def quickOff (strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
