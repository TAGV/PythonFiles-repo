print("bsdfbjsncghfghcv123")
print("bsdfbjsncghfghcv123")
name = "tanmay"
print("Hello " + name,12 )


tboard = {'1':10,2:2,3:3,
          4:4,5:5,6:6,
          7:7,8:8,9:9}

print(tboard['1'])

tboard = {'tl':1,'tm':2,'tr':3,
          'ml':4,'mm':5,'mr':6,
          'll':7,'lm':8,'lr':9}

#import os
#os.makedirs("RootFolder")
#os.makedirs("Root/Dir/Test")
#fhand = open("Root/Dir/Test/twitch.py",'w')
#os.remove("Root/Dir/Test/twitch.py"

"""
x = ['ab','cd']

for i in range(len(x)):
    x[i] = x[i].upper()
    print(i)
print(x)
"""
"""
words = []

while (word := input("Enter word: ")) != 'quit':
    words.append(word)

print(words)

"""

import pandas as pd
import csv
x = pd.read_csv('testfile.csv')
print(x)
print("==============")
print(x['Name'])
print("==============")
print(x['age'])
print("==============")
print(type(x))

with open("testfile.csv",'r') as csv_read:
    x = csv.reader(csv_read)
    print(type(x))
    for line in x:
        print(line)