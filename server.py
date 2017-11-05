# -*- coding: utf-8 -*-
import sys
from neopixel import *
from flask import (Flask, request, send_from_directory)
import programs.strandTest as strandTest
import programs.off as offProgram

################
# Strip Config #
################

# LED strip configuration:
LED_COUNT = 50 # Number of LED pixels.
LED_PIN = 21 # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0 # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB # Strip type and colour ordering



#################
# Server Config #
#################

APP = Flask(__name__, static_folder='client')

### Client Serving ###

@APP.route('/')
def home_route():
    return send_from_directory(APP.static_folder, 'index.html')

# Serve static files from client directory
@APP.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(APP.static_folder, filename)

### Lighting Routes ###

@APP.route("/off", methods=['GET'])
def off():
    # Get URL param for off animation
    animation = request.args.get('animation', default='')
    sys.stderr.write('animation: ' + animation + '\n')

    if animation == 'wipe':
        offProgram.wipe(STRIP)
    elif animation == 'burn':
        offProgram.burn(STRIP)
    else:
        offProgram.quick(STRIP)
    return "Strip off"


@APP.route("/strandtest", methods=['GET'])
def StrandTest():
    # Get URL params for type and color of animation
    animation = request.args.get('animation', default='colorWipe')
    color = request.args.get('color', default='')
    sys.stderr.write('animation: ' + animation + '\n')
    sys.stderr.write('color: ' + color + '\n')

    if animation == 'colorWipe':
        # if no color provided
        if color == '':
            strandTest.colorWipe(STRIP, Color(255, 0, 0)) # Red wipe
            strandTest.colorWipe(STRIP, Color(0, 255, 0)) # Blue wipe
            strandTest.colorWipe(STRIP, Color(0, 0, 255)) # Green wipe
    elif animation == 'theaterChase':
        # if no color provided
        if color == '':
            strandTest.theaterChase(STRIP, Color(127, 127, 127))  # White theater chase
            strandTest.theaterChase(STRIP, Color(127, 0, 0))  # Red theater chase
            strandTest.theaterChase(STRIP, Color(0, 0, 127))  # Blue theater chase
    elif animation == 'rainbow':
        strandTest.rainbow(STRIP)
    elif animation == 'rainbowCycle':
        strandTest.rainbowCycle(STRIP)
    elif animation == 'theaterChaseRainbow':
        strandTest.theaterChaseRainbow(STRIP)
    else:
        return "Invalid request"

    return "Animations complete"


if __name__ == "__main__":
    # Create NeoPixel object with appropriate configuration.
    STRIP = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    STRIP.begin()
    sys.stderr.write('Server Started.\n')
    # Start server
    APP.run(host='0.0.0.0', port=4000)
