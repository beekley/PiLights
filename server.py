import time
import sys
from neopixel import *
from flask import Flask, request

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

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

#################
# Server Config #
#################

app = Flask(__name__)

### Client Serving ###

@app.route('/')
def hello_world():
    return send_from_directory('client', 'index.html')

# Serve static files from client directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('client', path)

### Lighting Routes ###

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
            colorWipe(strip, Color(255, 0, 0)) # Red wipe
            colorWipe(strip, Color(0, 255, 0)) # Blue wipe
            colorWipe(strip, Color(0, 0, 255)) # Green wipe
    elif animation == 'theaterChase':
        # if no color provided
        if color == '':
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
    elif animation == 'rainbow':
        rainbow(strip)
    elif animation == 'rainbowCycle':
        rainbowCycle(strip)
    elif animation == 'theaterChaseRainbow':
        theaterChaseRainbow(strip)
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
