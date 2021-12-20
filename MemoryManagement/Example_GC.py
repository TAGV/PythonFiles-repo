import gc
i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)


# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect(2) # or gc.collect(2)
print(collected)

print("Creating cycles...")
for i in range(5):
    create_cycle()

collected = gc.collect(2)

print("Garbage collected objects : ",collected)

import platform
print(platform.python_implementation())

print("====================Getting the reference count===================")

import sys
mstr = 'Helloooooo'
print("Reference count : ",sys.getrefcount(mstr))

print("====================Increasing the reference count===================")
#Increasing the reference count
newlist = []
newlist.append(mstr)
newlist.append(mstr)
print("Reference count : ",sys.getrefcount(mstr))

mydict = {}
mydict[mstr] = 1
print(mydict)
print("Reference count : ",sys.getrefcount(mstr))

newlist.extend(mydict)
print("Reference count : ",sys.getrefcount(mstr))

print("====================Decreasing the reference count===================")

#Decreasing the reference count
mydict = {}
print(mydict)
print("Reference count : ",sys.getrefcount(mstr))

newlist.clear()
print("Reference count : ",sys.getrefcount(mstr))

del mstr #Object is removed
