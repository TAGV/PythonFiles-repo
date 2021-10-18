#Tool for measuring execution time of small code snippets.

import timeit

def func1():
    i = 0
    while i < 100:
        i=i+1

def func2():
    for i in range(100):
        i+=1

def func3():
    mlist = [str(n) for n in range(100)]


#temp_100 = timeit.timeit(str([str(n) for n in range(1000)]),number=10000)
#rint(temp_100)

#temp_10000 = timeit.timeit(str([str(n) for n in range(1000)]),number=10000)
#print(temp_10000)

print(timeit.timeit(str(func1()),number=10000))
print(timeit.timeit(str(func2()),number=10000))
print(timeit.timeit(str(func3()),number=10000))