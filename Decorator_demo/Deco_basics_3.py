#Creating my Third decorator
# Providing arguments

def decorate_hello(printed):
    def wrapper(*args,**kwargs):
        print("*************************")
        printed(*args,**kwargs)
        print("*************************")
    return wrapper

@decorate_hello
def printHello(message):
    print(message)


printHello("Hello")