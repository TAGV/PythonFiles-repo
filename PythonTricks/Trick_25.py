#List slicing & (shallow and deep copying the list)

mlist = [1,2,3,4,5]

# Deep copy of the list
a = mlist

#Creating a new list in place
mlist[:] = [6,7,8,9]
print(mlist)
print(a)

print(id(mlist))
print(id(a))
print(a is mlist)

print("==================")
nlist = [23,44,114]

# Shallow copy of the list
b = nlist[:]

nlist[:] = [45,67]
print(nlist)
print(b)

print(id(nlist))
print(id(b))
print(b is nlist)