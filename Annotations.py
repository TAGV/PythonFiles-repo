# Type annotations — also known as type signatures — are used to indicate the
# datatypes of variables and input/outputs of functions and methods

# Static typed — performs type checking at compile-time and requires datatype declarations.
# Dynamic typed — performs type checking at runtime and does not require datatype declarations.

# Without using type annotations
def add(x,y):
    return x + y


num = add(5,3)
print(num)

str = add('cheat','sheet')
print(str)


# Using type annotations

def add_at(x:int,y:int)->int:
    return x + y

num = add_at(6,6.6)
print(type(num),num)

str = add_at('cheat','sheet')
print(type(str),str)
