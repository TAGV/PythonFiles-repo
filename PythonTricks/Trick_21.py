# Removing numbers from a string

mystring = "Python 23"

#print(mystring.isdecimal())


# 1st Method
for num in mystring:
    if num.isdigit() == False:
        print(num,end="")
print()

# 2nd method
#Steps
# 1. Check for no-digit
# 2. Filter the space character from the output
# 3. Join the strings in the list
mylist = "".join(list(filter(lambda x:x != " ",[num for num in mystring if not num.isdigit()])))
print(mylist)