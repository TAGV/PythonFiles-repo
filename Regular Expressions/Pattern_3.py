import re

mystring = 'This is year 2021, and today is Sunday!!!So Enjoy!!!'


# The caret symbol ^ is used to check if a string starts with a certain character.

pat_1 = re.findall('^T',mystring)
pat_2 = re.findall('^i',mystring[5:])
pat_3 = re.findall('^!',mystring[::-1])

# The dollar symbol $ is used to check if a string ends with a certain character.

pat_4 = re.findall('!$',mystring)
pat_5 = re.findall('T$',mystring[::-1])


print(pat_1)
print(pat_2)
print(pat_3)
print(pat_4)
print(pat_5)

# Printing string in reverse
print(mystring[::-1])