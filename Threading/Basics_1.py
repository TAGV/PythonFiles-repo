import threading
from threading import *
import time
import random


def addsum(n):
    result = 0
    mylist = []
    for i in range(n):
        x = random.randrange(n)
        time.sleep(0.2)
        mylist.append(x)
        result += x
    print(result)
    print(mylist)


def updateThreadList(threadlist):
    threadlist = threading.enumerate()
    print(threadlist)

def updateThreadCount(threadCount):
    threadCount = threading.active_count()
    print("Active Thread Count:",threadCount)

thread_1 = threading.Thread(target=addsum,args=(5,))
#print(id(thread_1))

thread_2 = threading.Thread(target=addsum,args=(5,))
#print(id(thread_2))

mythreadlist = []
mythreadCount = 0
#print('Active Thread Count before start = ',threading.active_count())
#mythreadlist = (threading.enumerate())
#print(mythreadlist)
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)

thread_1.start()
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)
time.sleep(0.2)
thread_2.start()

#print('Active Thread Count before join = ',threading.active_count())
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)


thread_1.join()
updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)
thread_2.join()

updateThreadCount(mythreadCount)
updateThreadList(mythreadlist)
#print('Active Threas Count after join = ',threading.active_count())