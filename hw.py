import threading
import time
import queue

# def loop1_10():
#     for i in range(1, 11):
#         time.sleep(1)
#         print(i)
#
# threading.Thread(target=loop1_10).start()
# threading.Thread(target=loop1_10).start()

# Queue of functions
q = queue.Queue()

def readFromQueue():
    while True:
        if q.empty():
            break
        item = q.get()
        print("Next in queue:", item)
        # q.task_done()

# Hardware thread
t = threading.Thread(target=readFromQueue)

def push(item):
    '''
    Interface for threads to add items to the LED queue
    :param list The first item of the list is the function, the remaining are its params
    '''
    e = q.empty()

for i in range(10):
    q.put(i)

threading.Thread(target=readFromQueue).start()

push(1)
