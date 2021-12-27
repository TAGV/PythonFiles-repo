#Creating my Fourth decorator
# Providing arguments

def smart_division(divide):
    def wrapper(a,b):
        if b == 0:
            print("Division by zero not allowed!!!")
            return None
        return divide(a,b)
    return wrapper

@smart_division
def dividenum(a,b):
    return a/b


result_1 = dividenum(15,0)
print(result_1)

result_2 = dividenum(3,8)
print(result_2)