#Splat Operator in Python (*, **) - Unpack Iterables
#The spat operator allows you to unpack iterable objects like lists, tuples, strings and dictionaries.

def func(a,b,c,d):
    print(a,b,c,d)

mylist = [1,2,3,7]
mydict = {'a':1,'b':2,'c':3,'d':4}

func(*mylist)
func(**mydict)

