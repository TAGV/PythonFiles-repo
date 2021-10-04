#Sorting the python dictionary by value

mydict = {'a':5,'b':10,'c':3,'d':13}


mylist_ascending = sorted(mydict.items(),key=lambda x : x[1])
mylist_descending = sorted(mydict.items(),key=lambda x : x[1],reverse=True)


print(mylist_ascending)
print(mylist_descending)

print("======================================================")

mydict_alpha = {'a':"f",'b':"z",'c':"s",'d':"g"}


mylist_ascending = sorted(mydict_alpha.items(),key=lambda x : x[1])
mylist_descending = sorted(mydict_alpha.items(),key=lambda x : x[1],reverse=True)

print(mylist_ascending)
print(mylist_descending)


print("====================This is just extra practice==================================")
print(chr(65))
print(ord("z"))
print(ord("f") + ord("g"))
num = 'fg'

for ele in num:
    print(ord(ele),end="")