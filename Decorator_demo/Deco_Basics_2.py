#Creating my Second decorator

def decorate_star(printed):
    def wrapper():
        print("*******************")
        printed()
        print("*******************")
    return wrapper

def decorate_hash(printed):
    def wrapper():
        print("###################")
        printed()
        print("###################")
    return wrapper


def decorate_name(printed):
    def wrapper():
        print("Executing",printed.__name__,"function")
        printed()
        print("Function Execution finished")
    return wrapper

#Chaining of decorators

@decorate_star
@decorate_hash
def printHello():
    print("Hello!!!")

printHello()


@decorate_star
@decorate_hash
@decorate_name
def printBye():
    print("Bye!!!!")

printBye()