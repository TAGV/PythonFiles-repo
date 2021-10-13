from collections import Counter

#Strings
mystring = "aaaabbbcddghetrrrtsjjjjkh"
mycounterString = Counter(mystring)
print(mycounterString)                          #Creates a Dictionary

print(mycounterString.most_common(1))           #List of Tuple
print(mycounterString.most_common(1)[0])        #Tuple
print(mycounterString.most_common(1)[0][0])     #Single charcater

print(mycounterString.items())
print(mycounterString.keys())
print(mycounterString.values())
print(list(mycounterString.elements()))         #List of all items in the string

print("=====================================")

#List
myList = [2,3,3,3,3,3,4,5,'a','car',45]
mycounterList = Counter(myList)
print(mycounterList)                            #Dictionary is created


print("=====================================")

#List of Tuples
mytup = [(2,3),(3,4)]
mycountTup = Counter(mytup)
print(mycountTup)                               #Dictionary is created