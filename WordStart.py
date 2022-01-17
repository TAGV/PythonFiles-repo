# Checking the words starting with 'A' or 'a'

with open("wordfile.txt",'r') as fhand:
    word = (fhand.readline().split())
    for wd in word:
        if wd.startswith('A') or wd.startswith('a'):
            print(wd)
