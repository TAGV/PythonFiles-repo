import re

mystring = 'This is year 2021, and today is Sunday!!!So Enjoy!!!'

# Square brackets specifies a set of characters you wish to match.
pat_1 = re.findall('[abcde]',mystring)
pat_2 = re.findall('[a-e]',mystring)
pat_3 = re.findall('[0189]',mystring)
pat_4 = re.findall('[0-9]',mystring)

# You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.
pat_5 = re.findall('[^a-z]',mystring)
pat_6 = re.findall('[^01]',mystring)

print(pat_1)
print(pat_2)
print(pat_3)
print(pat_4)
print(pat_5)
print(pat_6)