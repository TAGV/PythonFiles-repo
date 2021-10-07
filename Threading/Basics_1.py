import threading
from threading import *
import time
import random


def addsum(n):
    result = 0
    mylist = []
    for i in range(n):
        x = random.randrange(n)
        time.sleep(0.2)                     #dELAY HELPS IN Thread Switching
        mylist.append(x)
        result += x
    print(result)
    print(mylist)


def updateThreadList(threadlist):
    threadlist = threading.enumerate()      #Return a list of all Thread objects currently alive
    print(threadlist)

def updateThreadCount(threadCount):
    threadCount = threading.active_count()      #Return the number of Thread objects currently alive
    print("Active Thread Count:",threadCount)

thread_1 = threading.Thread(target=addsum,args=(5,))    #This constructor should always be called with keyword arguments
#print(id(thread_1))                                    #Memory location of the variable

thread_2 = threading.Thread(target=addsum,args=(5,))    #*args* is the argument tuple for the target invocation.
#print(id(thread_2))

mythreadlist = []                           #The list will hold the threads at any give moment of time
mythreadCount = 0                           #Will provide no of active threads at any moment

print("Main thread is running!!!")
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)

thread_1.start()                            #Start the thread's activity
print("Thread-1 starts!!!")
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)
time.sleep(0.2)
thread_2.start()
print("Thread-2 starts!!!")

print(thread_1.is_alive())
print(thread_2.is_alive())
print(thread_1.getName()+str(thread_1.native_id))
print(thread_2.getName()+str(thread_2.native_id))

updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)


thread_1.join()                             #Wait until the thread terminates
print("Thread-1 stops!!!")
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)
thread_2.join()
print("Thread-2 stops!!!")

updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)

print(thread_1.is_alive())
print(thread_2.is_alive())

print(thread_1.getName())

T = (threading.currentThread())
if T.getName() == 'MainThread':
    print(T.native_id)