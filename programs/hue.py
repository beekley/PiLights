from neopixel import *
import helpers as h

# Immediately change color to solid color
def solid (strip, r, g, b):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(g, r, b))
        strip.show()
