import time
from neopixel import *

# Immediately shut off all lights on strip
def quickOff (strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

# Fade out lights on strip in parallel
def wipeOff (strip, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)
