import re


mystring = "This is an example: to find spaces in a string using Regex"

temp = re.findall('[\s]',mystring)

print(temp)
print(len(temp))