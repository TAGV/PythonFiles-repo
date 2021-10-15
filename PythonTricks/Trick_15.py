#Unpacking function arguments


def myfunc(x,y,z):
    print(x,y,z)


my_tup = (1,2,3)
my_dict = {'x':1,'y':5,'z':4}           #Keys have to be equal to x,y,z

myfunc(*my_tup)
myfunc(**my_dict)

