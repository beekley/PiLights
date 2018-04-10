import threading
import time
import queue

# Queue of functions
q = queue.Queue()
t = None

def readFromQueue():
    while True:
        if q.empty():
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
    e = q.empty()
    # Add item to the Queue
    q.put(item)
    # If queue was empty when called, start a hw control thread
    if e:
        t = threading.Thread(target=readFromQueue)
        t.start()

# def clear():
#     '''
#     Interface for clearing all items from a queue
#     '''

push([print, "hello", "world"])
time.sleep(1)
push([print, "hi", "I am", 3])
