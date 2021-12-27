#Creating my first decorator

def decorate_hello(printed):
    def wrapper():
        print("*************************")
        printed()
        print("*************************")
    return wrapper

@decorate_hello
def printHello():
    print("Hello!!!")


printHello()