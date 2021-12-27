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
    for it in range(100_000_000):
        it*5


calculate()