from math import floor
from neopixel import *

# Hijack the neopixel setPixelColor method to store the most recent color value for each pixels
currentColors = []
def init (LED_COUNT):
    for i in range(LED_COUNT):
        currentColors[i] = Color(0, 0, 0)

def setPixelColor (strip, i, color):
    strip.setPixelColor(i, color)
    currentColors[i] = color
