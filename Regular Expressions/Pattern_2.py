import re

mystring = 'This is year 2021, and today is Sunday!!!So Enjoy!!!'

# A period matches any single character (except newline '\n').
pat_1 = re.findall('...',mystring)
pat_2 = re.findall('............',mystring)
pat_3 = re.findall('...............',mystring)

print(pat_1)
print(pat_2)
print(pat_3)