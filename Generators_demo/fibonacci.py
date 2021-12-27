from time import time

def calculate_time(func):
    def wrapper():
        t1 = time()
        func()
        t2 = time()
        print(str(t2-t1)+" seconds")
    return wrapper



def fib_generator(n):
    a=0
    b=1
    for num in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


def fib_iterator(n):
    a=0
    b=1
    result = []
    for num in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

@calculate_time
def print_fib_gen():
    n = fib_generator(1000)


@calculate_time
def print_fib_iter():
    my_iter_list = fib_iterator(1000)

print_fib_gen()
print_fib_iter()
