from time import time

def calculate_time(func):
    def wrapper():
        t1 = time()
        func()
        t2 = time()
        print(str(t2-t1)+" seconds")
    return wrapper

@calculate_time
def calculate():
    print("This is a generator")        #This is more efficient,incase of large range of data
    for it in range(100_000_00):
        it*5

@calculate_time
def calculate2():
    print("This is a iterator")
    for it in list(range(100_000_00)):
        it*5

calculate()
calculate2()