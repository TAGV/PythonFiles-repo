#Memory Management in Python

#Everything is an object in Python(PyObject structure implementation in Cpython)
#Pyobject contains 'refernce count' and 'object type'
#If refernce count  == 0, for a particular object, the garbage collection kicks in and the object is deleted
#Python uses private heap to store Objects
#Variable names acts as references, which are stored on stack
#Two vars pointing to same object will have same refernce id

import gc

var_1 = 20
var_2 = 20
var_3 = 20
var_4 = 45

#Current ref count for object '20' is = 3
# Reference count for integer object (value = 20) is decremented
var_1 = 40  #ref count = 2
var_2 = 40  #ref count = 1
var_3 = 40  #ref count = 0      At this point the original integer Pyobject(val = 20) is deleted via garbage collection

str1 = "Hello"
str2 = "Bye"
str3 = "Hello"

#Same memory reference address,since object is similar
print(id(var_1))
print(id(var_2))
print(id(var_3))


#Different memory reference address,since created object value is different
print(id(var_4))


print()

#Similar example for strings
print(hex(id(str1)))
print(hex(id(str3)))
print(hex(id(str2)))

print()


#List Behaviour
mlist = [1,2,3,4,5]
nlist = [1,2,3,4,5]

print(id(mlist))
print(id(nlist))

mlist.append(6)
mlist.append(7)
mlist.extend(nlist)

print(id(mlist))
print(mlist)

print()

#Dictionary

dict_a = {'a':1,'b':2,'c':3}
dict_b = {'a':1,'b':2}

print(id(dict_a))
print(id(dict_b))


dict_a.popitem()
dict_a['z'] = 7
print(dict_a)
print(id(dict_a))

collected  = gc.get_threshold()
print(collected)