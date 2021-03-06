import time
import sys
from math import floor
from neopixel import *

# Immediately shut off all lights on strip
def quick (strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

# Turn off lights on strip in sequence
def wipe (strip, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)

# Fade out lights on strip in parallel
def fade (strip, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)

# Fun burning animation
# RGB:
# 255, 253, 244 (brighter)
# 255, 241, 178 (bright)
# 255, 195, 0 (red)
# 199, 0, 57
# 144, 12, 63
# 88, 24, 69 (dark)
# 0,0,0 (off)
def burn (strip, wait_ms=5):
    # burn up
    # steps = 20
    # g_i = 241
    # g_f = 251
    # r_i = 255
    # r_f = 255
    # b_i = 178
    # b_f = 221
    # # Iterate through number of steps
    # for x in range(steps):
    #     # Iterate through pixels
    #     for i in range(strip.numPixels()):
    #         g_x = int(g_i + x * (g_f - g_i) / steps)
    #         r_x = int(r_i + x * (r_f - r_i) / steps)
    #         b_x = int(b_i + x * (b_f - b_i) / steps)
    #         strip.setPixelColor(i, Color(g_x, r_x, b_x))
    #         strip.show()
    #         sys.stderr.write(str(g_x) + ',' + str(r_x) + ',' + str(b_x) + '\n')
    #     time.sleep(wait_ms/1000.0)
    # sys.stderr.write('burn down..................\n')
    # burn down
    steps = 50
    g_i = 251
    g_f = 295
    r_i = 255
    r_f = 255
    b_i = 221
    b_f = 0
    # Iterate through number of steps
    for x in range(steps):
        # Iterate through pixels
        for i in range(strip.numPixels()):
            g_x = int(g_i + x * (g_f - g_i) / steps)
            r_x = int(r_i + x * (r_f - r_i) / steps)
            b_x = int(b_i + x * (b_f - b_i) / steps)
            strip.setPixelColor(i, Color(g_x, r_x, b_x))
            strip.show()
        sys.stderr.write(str(g_x) + ',' + str(r_x) + ',' + str(b_x) + '\n')
        time.sleep(wait_ms/1000.0)
