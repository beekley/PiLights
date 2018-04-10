from math import floor
from neopixel import *

# Hijack the neopixel setPixelColor method to store the most recent color value for each pixels
currentColors = []
strip = STRIP
def init (LED_COUNT, STRIP):
    for i in range(LED_COUNT):
        currentColors.append(Color(0, 0, 0))

# Deprecated
# def setPixelColor (strip, i, color):
#     strip.setPixelColor(i, color)
#     currentColors[i] = color

# Take in 24 bit "Color" value and returns an object with the rgb values
# class Color(object):
#     r = 0
#     g = 0
#     b = 0
#
#     def __init__(self, color):
