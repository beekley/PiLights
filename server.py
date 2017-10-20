import time
import sys
from neopixel import *
from flask import (Flask, request, send_from_directory)
import programs.strandTest as strandTest

################
# Strip Config #
################

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



#################
# Server Config #
#################

app = Flask(__name__, static_folder='client')

### Client Serving ###

@app.route('/')
def home_route():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files from client directory
@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)

### Lighting Routes ###

@app.route("/off", methods=['GET'])

def Off ():
    # Get URL param for off animation
    animation = request.args.get('animation', default='colorWipe')

    if animation == 'fade':
        # to implement
        sys.stderr.write('Fading out...')
    else:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
            strip.show()
    return "Strip off"


@app.route("/strandtest", methods=['GET'])

def StrandTest ():
    # Get URL params for type and color of animation
    animation = request.args.get('animation', default='colorWipe')
    color = request.args.get('color', default='')
    sys.stderr.write('animation: ' + animation)
    sys.stderr.write('color: ' + color)

    if animation == 'colorWipe':
        # if no color provided
        if color == '':
            strandTest.colorWipe(strip, Color(255, 0, 0)) # Red wipe
            strandTest.colorWipe(strip, Color(0, 255, 0)) # Blue wipe
            strandTest.colorWipe(strip, Color(0, 0, 255)) # Green wipe
    elif animation == 'theaterChase':
        # if no color provided
        if color == '':
            strandTest.theaterChase(strip, Color(127, 127, 127))  # White theater chase
            strandTest.theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            strandTest.theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
    elif animation == 'rainbow':
        strandTest.rainbow(strip)
    elif animation == 'rainbowCycle':
        strandTest.rainbowCycle(strip)
    elif animation == 'theaterChaseRainbow':
        strandTest.theaterChaseRainbow(strip)
    else:
        return "Invalid request"

    return "Animations complete"


if __name__ == "__main__":
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    sys.stderr.write('Server Started.\n')
    # Start server
    app.run(host='0.0.0.0', port=4000)
