import copy

# Shallow copy --- This is only one level deep

mlist = [1,2,3,4,5]

cpy_list = []

cpy_list = copy.copy(mlist)

print(mlist)
print(cpy_list)

print("=======================")
# Modifying copy list elements

cpy_list[3] = 1000

print(id(mlist))
print(mlist)
print(id(cpy_list))
print(cpy_list)

print("======== Deep Copy  ===============")

# Deep copy ---------- All levels deep

nlist = [[1,2,3,4,5],[6,5,4,3,2,1],[2,3,4,5,6]]

dcpy_list = []

# dcpy_list = copy.copy(nlist) # this does not work for multi level list
dcpy_list = copy.deepcopy(nlist)

print(nlist)
print(dcpy_list)

print("=======================")

# Modifying the list

dcpy_list[2][0] = 34534563

print(id(nlist))
print(nlist)
print(id(dcpy_list))
print(dcpy_list)