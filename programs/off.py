import time
from math import floor
from neopixel import *

# Immediately shut off all lights on strip
def quick (strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

# Fade out lights on strip in parallel
def wipe (strip, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)

# Fun burning animation
# RGB:
# 255, 253, 244 (brighter)
# 255, 251, 221 (bright)
# 255, 195, 0 (red)
# 199, 0, 57
# 144, 12, 63
# 88, 24, 69 (dark)
# 0,0,0 (off)
def burn (strip):
    steps = 10
    g_i = 253
    g_f = 251
    r_i = 255
    r_f = 255
    b_i = 244
    b_f = 221
    # Iterate through number of steps
    for x in range(steps):
        # Iterate through pixels
        for i in range(strip.numPixels()):
            g_x = floor(g_i + x * (g_f - g_i) / steps)
            r_x = floor(r_i + x * (r_f - r_i) / steps)
            b_x = floor(b_i + x * (b_f - b_i) / steps)
            strip.setPixelColor(i, Color(g_x, r_x, b_x))
            strip.show()
            time.sleep(wait_ms/1000.0)
