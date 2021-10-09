#Race condition happens when 2 or more threads try to modify the same variable at same time

import threading
from threading import *
import time
import random

counter = 0

def changeCounter(lock):
    global counter

    #lock.acquire()                              #Lock is aquired, hence program will not switch to other thread
    with lock:                                  #using 'with' keyword we can avoid acquire and release
        local_counter = counter
        local_counter += 1
        #time.sleep(0.1)                               #Program switches to another thread
        counter = local_counter
    #lock.release()

lock = Lock()

print("Start Value of counter = ",counter)

thread_1 = threading.Thread(target=changeCounter,args=(lock,))
thread_2 = threading.Thread(target=changeCounter,args=(lock,))



thread_1.start()
print(threading.enumerate())
#time.sleep(1)                      #With this sleep you can resolve the race condition, but this is not an effective approach
thread_2.start()
print(threading.enumerate())



thread_1.join()
thread_2.join()

print("End Value of counter = ",counter)








