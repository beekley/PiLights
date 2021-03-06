import threading
import time
import queue
from neopixel import *
from hardware import *
import programs.strandTest as strandTest

# Queue of functions
q = queue.Queue()
t = None
running = False

def readFromQueue():
    # time.sleep(1)
    global running
    print("Processing queue.")
    while True:
        if q.empty():
            print("Queue is empty. Stopping thread.")
            running = False
            break
        item = q.get()
        print("Next in queue:", item[0].__name__, "with params:", item[1:])
        # Execute function
        item[0](*item[1:])

def push(item):
    '''
    Interface for threads to add items to the LED queue
    :param list The first item of the list is the function, the remaining are its params
    '''
    global running
    e = q.empty() and not running
    # Add item to the Queue
    q.put(item)
    # If queue was empty when called, start a hw control thread
    if e:
        print("Queue was empty. Starting new thread.")
        t = threading.Thread(target=readFromQueue)
        t.start()
        running = True

# def clear():
#     '''
#     Interface for clearing all items from a queue
#     '''

def initialize():
    '''
    Interface for starting up LED controller. This must be the first method called.
    '''
    print("Initializing LED strip.")
    # Create NeoPixel object with appropriate configuration.
    global STRIP
    STRIP = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    STRIP.begin()
    print("Initialization complete:", STRIP)

initialize()
print(STRIP)
push([strandTest.colorWipe, STRIP, Color(255, 255, 0)])
