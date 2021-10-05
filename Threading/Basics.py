#Intro to Multithreading
import threading
import time
from threading import *

class Thread_1(Thread):                         #Inheriting from Thread class
    def run(self):                              #run() method overwritten in subclass
        for i in range(10):
            print("In Thread 1")
            time.sleep(1)

class Thread_2(Thread):
    def run(self):
        for i in range(10):
            print("In Thread 2")
            time.sleep(1)

class Thread_3(Thread):
    def run(self):
        for i in range(10):
            print("In Thread 3")
            time.sleep(1)


t1 = Thread_1()
t2 = Thread_2()
t3 = Thread_3()

t1.start()
time.sleep(0.2)                     #This is used to unsync the threads and make them run in parallel
t2.start()
time.sleep(0.2)
t3.start()
print("No of active threads at current time = ",threading.active_count())


t1.join()                           # Wait until the thread terminates
t2.join()
t3.join()

print("No of active threads at current time = ",threading.active_count())
print("Stop")