# print("   /" *2)
# age = 20;
# print("The age =",age)

# name = input("What is ur name ? ")
# print("Hello " + name)

# SimpleCalculator = Type COnversion
"""
First_Number = float(input("Enter 1st number = "))
#print("First No = " + First_Number)
Second_Number = float(input("Enter 2nd number = "))
#print("Second No = " + Second_Number)

sum = (First_Number) + (Second_Number)
print("Sum: " + str(sum))
"""
"""
#Strings
import copy
import math
import os
import pprint
import random
import re
import sys
import time

import pyperclip
"""
""""
mystring = "This is for Python"
print(mystring.upper())
print(mystring.find('for'))
print(mystring.replace('for','4'))
print('Python' in mystring)
print(mystring.lower())
print(mystring.center(20).upper())
print(mystring)
"""
# Arithmatic Operators

""""
print(10/3)
print(10//3)
print(10 ** 3)
print(10 % 3)

"""
# Comparison Operators

"""
print(3>2)
print(3<2)
print(3==3)
print(3!=2)

"""

# Logical Operators

"""
price = 10

print(price > 5 and price < 15)
print(price > 10 or price == 10)
print(not price == 10)

"""
# Exercise

"""
weight = float(input("Weight: "))
std = input("(K)g or (L)bs: ")

if  std.upper() == 'K':                             #std == 'K' or std == 'k':
    weight *= 2.20462
    print("Weight in LBS: " + str(weight))
elif std.upper() == 'L':                                               #std == 'L' or std == 'l':
    weight /= 2.20462    #0.453592
    print("Weight in Kg: " + str(weight))
else:
    print("It's a Wrong Input")

"""

# While Loops

"""
i = 1
while i <= 5:
    print(i * '*'.center(10))       # Number * String....allowed in python
    i += 1

j = 5
while j >= 1:
    print(j * '*'.center(10))
    j -= 1

"""
# Lists

"""
names = ["tan","man","lan","cat","bat"]

print(names)
print(names[0])
print(names[1])

print(names[-1])
print(names[-2])

print(names[0:3])
print(names.__len__())
names[0] = "Jon"
print(names)

"""

# List Methods

"""
nos = [1,2,3,4,5]

nos.append(6)
nos.remove(3)
nos.insert(1,10)
print(6 in nos)
print(nos)
print(len(nos))

nos.clear()
print(nos)

"""

# For Loop

"""
nos = [1,2,3,4,5]

for input in nos:
    print(input)

"""

# Range function

"""

for nos in range(1,5):
    print(nos)

print("\n")

for nos in range(5,10):
    print(nos)

print("\n")
for nos in range(5):
    print(nos)

print("\n")
for nos in range(5,10,2):
    print(nos)

"""

#Tuples : immutable lists

"""
nos = (1,2,3,3,10,5)

#nos[0] = 2 ---Not suppported

print(nos)
print(nos.count(3))
print(nos.index(10))

"""

#Try-Except blocks

"""
name = 'tanmay'
try:
    toint = int(name)
except:
    toint = -1

print('Done')

"""

#print('C:\some\name')
#print(r'C:\some\name')

# Fibonacci series:the sum of two elements defines the next
"""
a, b = 0, 1
while a < 1000:
    print(a,end=',')        # end keyword to get o/p on same line
    a, b = b, a+b
"""

#Functions

"""
def addnumbers(a,b):
    c = a + b
    return c

def Result():
    num1 = float(input("Enter 1st Number: "))
    num2 = float(input("Enter 2nd Number: "))
    result = addnumbers(num1,num2)
    return result

output = Result()
print("Result = ", output)

"""

#Smallest/Largest/Sum/Average Number

"""
smallest = None
largest = None
sum = 0
count = 0

for iter in [23,1000,2000,3,145,20]:
    print(iter, end='\t')
    sum += iter
    count += 1
    if smallest is None and largest is None:  #Check the use of "is" and "None" keyword
        smallest = iter
        largest = iter
    elif iter < smallest:
        smallest = iter
    elif iter > largest:
        largest = iter

print('\n\nSmallest No in the series = ',smallest)
print('Largest No in the series = ',largest)

print('\n\nNo of elements in the series = ',count)
print('Sum of the series = ',sum)
print('Average of the series = ',sum/count)

"""

#File Operations

"""
with open("/home/myubuntu/Desktop/Cr",'r+') as fhand:     #File is opened for appending
    char = fhand.write("\nThis is new line alsodef")
    print(char)

var1 = fhand.closed
print("\n",var1)

with open("/home/myubuntu/Desktop/Cr",'r+') as fhand:         #File is opened for reading
    for line in fhand:
        print(fhand.read(),end=' ')
    fhand.write("\nThis is the end")


var = fhand.closed
print("\n",var)

"""

#Lists

"""
mylist = ['car','bar','tar']
#print(mylist[0])

for i in mylist:
    print("This is :", i)

mylist[1] = 'gar'
print(mylist)

#print(len(mylist))

for i in range(len(mylist)):
    print(i , mylist[i])

newlist = ['war','tor']
print(newlist+mylist)

print(type(mylist))
print(dir(mylist))

"""

#List Operations

"""
mylist = [3,4,1,7,'red']
print(mylist)

print(mylist[1:3])
print(mylist[:3])
print(mylist[1:])
print(mylist[:])

stuff = mylist
stuff.append('blue')
stuff.append(5)
stuff.append('yellow')
stuff.append([3,5,6,7])
stuff.remove('blue')
print(stuff)

print("\n")

names = ['tanmay','danny','vikas','chetan']
names.sort()
print(names)

numbers = [3,56,23,67,89,22,100,-1]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))

"""

#list Program

"""
number = []

while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    number.append(float(inp))

print(number)
print("Sum:", sum(number))
print("Average:", sum(number)/len(number))

"""
#import math
#print(math.pi)

#String to List : split()

"""
mystring = 'This is new world'
mylist = mystring.split()
print(mylist)
print(len(mystring), len(mylist))

newstring = 'this;is;home'       #helpful in parsing email address
newlist = newstring.split(';')
print(newlist)
print(len(newstring),len(newlist))

#Example Program

email = 'tanmay.ghare@gmail.co.in'
test_list = email.split('.')
print(test_list)
toconvert = test_list[1]

token = toconvert.split('@')
print(token)
print('tanmay '.upper() + token[0].upper())

"""

#String to List : Program

""""
fhand = open('/home/myubuntu/Desktop/Cr')

for line in fhand:
    line = line.rstrip()
    word = line.split()
    if len(word) < 1:
        continue
    if word[0] != 'This':
        continue
    print(word[-1])

print(word)

"""
#Dictionaries

""""

mydict = dict()
mydict['ten'] = 10
mydict['nine'] = 9
print(mydict)

mydict['ten'] = mydict['ten'] + 5
print(mydict)

newdict = {'z':2,'w':3}
print(newdict)

"""

#Dictionaries:Counting: Histogram

""""
mydict = dict()
mylist = ['cat','bat','lat','cat','fat','cat','lat','lat','lat']

for iter in mylist:
    if iter not in mydict:
        mydict[iter] = 1
    else:
        mydict[iter] = mydict[iter] + 1

print(mydict)

#======Using get function==========#

newdict = dict()
newlist = ['cat','bat','lat','cat','fat','cat','lat','lat','lat']

for iter in newlist:
    newdict[iter] = newdict.get(iter,0) + 1

print(newdict)

"""
#Random No generator
""""
for iter in range(5):
    rd = random.randint(1,10)
    ts = math.pow(rd, 2)
    print(rd,"=\t",int(ts),end='')
    print("\n")

"""

#Sys.exit function
""""
nm = input()
if nm == 'exit':
    print("bye")
    sys.exit()
else:
    print("hello " + nm)
"""

#Guess The No game
"""
print("\t\t GUESS THE NUMBER GAME")

secretno = random.randint(1,20)

for guess in range(1,7):
    inputno = int(float(input("Enter the no between 1 and 20:\n")))
    if inputno > 20 or inputno < 1:
        print("Out of range")
        break
    elif inputno < secretno:
        print("You are a bit lower\n")
    elif inputno > secretno:
        print("You are a bit higher\n")
    else:
        break


if inputno == secretno:
    print("You guessed it correct in " + str(guess) + ' attempts')
else:
    print("You are unlucky. Secret no was = " + str(secretno))

print("Game Over\n")

"""

#Rock Paper Scissor game

"""
print("\t\tRocks Papers Scissorrrs....Game!!!\n")

wins,loss,tie = 0,0,0
print("Wins:",wins,"Loss:",loss,"Tie:",tie)
while True: #Loop for Whole game
    user = input("Enter Rock(r/R),Paper(p/P),Scissor(s/S),Quit(q/Q)\n")
    while True: #Loop for User Input
        if user.lower() == 'q':
            print("Game Over")
            print("Final Score = Wins:", wins, "Loss:", loss, "Tie:", tie)
            sys.exit() #Exit the Program
        elif user.lower() == 'r':
            print("User : Rock")
            break
        elif user.lower() == 'p':
            print("User : Paper")
            break
        elif user.lower() == 's':
            print("User : Scissor")
            break
        else:
            break


    machine = random.randint(1,3)
    if machine == 1:
        print("Machine : Rock")
    elif machine == 2:
        print("Machine : Paper")
    elif machine == 3:
        print("Machine : Scissor")

    if user.lower() == 'r' and machine == 1:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'p' and machine == 2:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 's' and machine == 3:
        print("Tie")
        tie = tie + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 'r' and machine == 2:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'r' and machine == 3:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 'p' and machine == 1:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 'p' and machine == 3:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

    if user.lower() == 's' and machine == 2:
        print("User Won")
        wins = wins + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)
    elif user.lower() == 's' and machine == 1:
        print("User Lost")
        loss = loss + 1
        print("Wins:",wins,"Loss:",loss,"Tie:",tie)

"""

#Fortune Teller
""""
def fortune(number):
    if number == 1:
        return "You are Fire"
    elif number == 2:
        return "You are Water"
    elif number == 3:
        return "You are Earth"

fn = random.randint(1,3)
print(fortune(fn))
"""

#Global and Local Scope and Try/Except code

""""
car = 10
sum = 9


def compute(num):
    car = 20
    global sum    #Global Var used and modified
    sum = 100
    print(car)
    print(sum)
    try:
        print(eggs)
    except NameError:
        print("NameError")
        #sys.exit()
    try:
        return (10/num)
    except ZeroDivisionError:
        print("ZeroDivisionError")

#eggs = 8
compute(0)
print(sum)

"""
#Collatz Sequence

""""

def collatz(number):
    if (number % 2) == 0:
        number = number//2
        return number
    else:
        number = (3 * number + 1)
        return number

while True:
    try:
        user = int(input())
        break
    except ValueError:
        print("Need to enter an integer")
        print("Enter Again:")
        continue

while True:
    temp = collatz(user)  # 10
    if temp != 1:
        print(temp) #10
        user = temp
        continue
    elif temp == 1:
        print(temp)
        break
"""
#ZigZag Pattern Animation(with use of range() function)
"""
try:
    while True:
        for iter in range(10,-1,-1):
            print(' '*iter,'********')
            time.sleep(0.1)
        for iter in range(1,10):
            print(' ' * iter, '********')
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
"""

#ZigZag Pattern Animation(without the use of range() function)

""""
iter = 10
try:
    while True:
        print(' ' * iter, '********')
        iter = iter - 1
        #print(iter)
        time.sleep(0.1)

        if iter == 0:
            while True:
                print(' ' * iter, '********')
                iter = iter + 1
                #print(iter)
                time.sleep(0.1)
                if iter == 10:
                    break
except KeyboardInterrupt:
    sys.exit()
"""

#list Concatenation

"""
mynames = []

while True:
    names = input("Enter The Names")
    if names == ' ':
        break
    #mynames = mynames + [names]
    mynames.append(names)

mynames.sort()
print(mynames)
print("Random choice 1: " + random.choice(mynames))
print("Random choice 2: " + random.choice(mynames))
print("Random choice 3: " + random.choice(mynames))
mynames.remove(mynames[-1])
print(mynames)

mynames.reverse()
print(mynames)

"""

#MultiDimensional List
""""
mylist = [['cat','bat','rat','dat'],[10,20,30,40],['helloood','world']]
print(mylist)

print(mylist[0])
print(mylist[1])
print(mylist[2])

print(mylist[1][1])   #integr elements are not further broken down
print(mylist[2][0][0])

newlist = ['ca','da','ra']
print(newlist[1])

cat,bat,fat = newlist   #Multiple Assignment via list
print(cat,bat,fat)

newlist = newlist + mylist
print(newlist)

del newlist[3]
print(newlist)

for index,iter in enumerate(newlist):   #Using Enumerate keyword to print index of items
    print(index,iter)
"""

#Printing letters of the word using for loop

"""
mylist = ['letter']
print(mylist)

numb = len(mylist[0]) - 1
print(numb)
for iter in mylist[0]:
    #print(iter,end=' ')
    print('*****',mylist[0][numb],'*****')
    numb = numb - 1
    if numb == 0:
        print('*****',mylist[0][numb],'*****')
        break

print("\n")
for iter in mylist[0]:
    print(mylist[0][numb],end='    ')
    numb = numb + 1
"""

#list replication

"""
mylist = [10,20,30,'as']
mylist *= 3
print(mylist)
mylist[0] *= 3
mylist[1] += 3
mylist[2] /= 3

print(mylist)

"""

#list Methods

"""
mylist = ['cat','bat','hat']
if 'cat' in mylist:
    print("True")
    print(mylist.index('cat'))

mylist.append('dfu')
print(mylist)

mylist.insert(0,'tata')
print(mylist)

mylist.remove('dfu')
print(mylist)

del mylist[1]
print(mylist)

numberlist = [2,6,1,0,6,4,7,3,3,6]
numberlist.sort()
print(numberlist)

numberlist.sort(reverse=True)
print(numberlist)

newList = ['a','A','z','Z']

newList.sort()
print(newList)

newList.sort(key=str.lower)
print(newList)

#Magic number program

print(numberlist)

index = 0
for iter in numberlist:
    print("Magic Number at index "+str(index)+"=", numberlist[random.randint(0,len(numberlist)-1)])
    index += 1

"""

#Tuple ==== Its an immutable data type

"""
tup = ('cat','bat','hat','cat','cat',1,2,3,3,3,3,3,3,3,3,3,3)
print(tup)

print(len(tup))
print(tup.count('cat'))

for iter in tup:
    print(iter,end=' ')

print("\n")
if 3 in tup:
    print(True)
    print(tup.count(3))

"""
#Comma Code Program

"""
spam = ['apples', 'bananas', 'tofu', 'cats']
cache = []


def mylist(somelist):
    for iter in somelist:
        print(iter,end=', ')
    print(len(somelist))

mylist(spam)
mylist([])

"""
#Coin Flip Streaks Program

""""
mylist = ['H','T']
newlist = []                # Empty List to store the randomly generated Heads and Tails

#Generating list of Heads & Tails

for iter in range(10000):
    item = mylist[random.randint(0, 1)]
    newlist += item

print(newlist)

#Getting the Streak count for Heads or Tails

cnt = 0                     #Counter variable to iterate through the above generated list
streaH = 0                  #Check for Head streak of 6
Hstreakcount = 0            #Counting the Head streak

streaT = 0                  #Check for Tail streak of 6
Tstreakcount = 0            #Counting the Tail streak

for it in newlist:
    if newlist[cnt] == 'H':
        streaT = 0
        streaH = streaH + 1
        if streaH == 6:
            Hstreakcount = Hstreakcount + 1
        elif streaH > 6:
            streaH = 0
    elif newlist[cnt] == 'T':
        streaH = 0
        streaT = streaT + 1
        if streaT == 6:
            Tstreakcount = Tstreakcount + 1
        elif streaT > 6:
            streaT = 0

    cnt += 1

print("HEADS streak of 6 count : ",Hstreakcount)
print("TAILS streak of 6 count : ",Tstreakcount)
print("Probability of HEADS streak of 6 count : ",Hstreakcount/100)
print("Probability of TAILS streak of 6 count : ",Tstreakcount/100)

"""

#References---List

"""
mylist = ['cat','bat','hat',[1,2,3,['a','b']]]
reflist = mylist        #Both List refer the same list values

reflist[0] = 'fat'
reflist.append('yat')

print(mylist)
print(reflist)

print(id(mylist),id(reflist))   #id function shows the numeric memory locn of the any variable

templist = copy.copy(mylist)  # The function creates a copy of the original list and stores it in new location

templist.append('rat')

print(mylist)
print(templist)

print(id(mylist),id(reflist),id(templist))

"""
#Conways Game of Life
"""
width = 10
height = 10

randomlist = ['0','-']

nextcell = []
for x in range(width):
    coloumn = []
    for y in range(height):
        if random.choice(randomlist) == '0':
            coloumn.append('0')
        else:
            coloumn.append('-')
    nextcell.append(coloumn)


print(nextcell)
print(len(nextcell))
print(len(coloumn))

while True:
    print("\n\n\n\n\n")
    currentcell = copy.deepcopy(nextcell)
    for y in range(height):
        for x in range(width):
            print(currentcell[x][y],end='    ')
        print("\t\t\t")

    for x in range(width):
        for y in range(height):
            leftcoord = (x-1)%width
            rightcoord = (x+1)%width
            abovecoord = (y-1)%height
            belowcoord = (y+1)%height

            numNeighbours = 0
            if currentcell[leftcoord][abovecoord] == '0':
                numNeighbours += 1
            if currentcell[x][abovecoord] == '0':
                numNeighbours += 1
            if currentcell[rightcoord][abovecoord] == '0':
                numNeighbours += 1
            if currentcell[rightcoord][y] == '0':
                numNeighbours += 1
            if currentcell[rightcoord][belowcoord] == '0':
                numNeighbours += 1
            if currentcell[x][belowcoord] == '0':
                numNeighbours += 1
            if currentcell[leftcoord][belowcoord] == '0':
                numNeighbours += 1
            if currentcell[leftcoord][y] == '0':
                numNeighbours += 1

            if currentcell[x][y] == '0' and (numNeighbours == 2 or numNeighbours == 3):
                nextcell[x][y] = '0'
            elif currentcell[x][y] == '-' and (numNeighbours == 3):
                nextcell[x][y] = '0'
            else:
                nextcell[x][y] = '-'

        time.sleep(1)

"""

#Dictionary

"""
mydit = {1:'cat',2:'hat'}
mydit_new = {2:'hat',1:'cat'}
print(mydit[2])

print(mydit == mydit_new)       # To Prove that dictionaries are unordered

#Birthday diary

bday = {'Tanmay':'Apr 12','Chinmay':'June 26','Asha':'April 15','Vilas':'Sept 25'}

while True:
    name = input("Enter Name to find Birthday: ")
    if name == '':
        break
    if name in bday:
        print(bday[name])
    elif name not in bday:
        print("Name not in dictionary")


print(bday)
"""
#Dictionary Methods
"""
bday = {'Tanmay':'Apr 12','Chinmay':'June 26','Asha':'April 15','Vilas':'Sept 25'}
for it in bday.keys():
    print(it)
print()
for it in bday.values():
    print(it)
print()
for it in bday.items():
    print(it)
print()
for k,v in bday.items():
    print("Key: ",k,"\t\t","Value: ",v)
print()
print(bday.keys())
print(bday.values())
print()
mylist = list(bday.keys())          # Converting dictionary to Lists
mylist += list(bday.values())
print(mylist)

print()
name = input("Enter key to search")
evaluate = (bday.get(name,0))                            #Get method
if evaluate == 0:
    print("Key needs to be added")
    value = input("Enter the value for new Key")
    bday.setdefault(name,value)                           #Setdefault method
else:
    print("The value of the key: ",bday.get(name,0))

pprint.pprint(bday)         #Used for Pretty printing in dictionaries

"""
#Counting the frequency of letters in a sentence
"""

string = 'This is going,for the vacation today ?'
count = {}

for character in string:
    count.setdefault(character,0)     # Using setdefault avoid the Key Error message
    count[character] += 1

pprint.pprint(count)
#print(count)

#Convert List to Dictionary

mylist = ['cat','bat',1,2.5,1,1,1]
list2Dict = {}
print(type(mylist))

for item in mylist:
    list2Dict.setdefault(item,0)
    list2Dict[item] += 1

print(pprint.pformat(list2Dict))

"""
#Tic Tac Toe board game

"""

tboard = {'tl':1,'tm':2,'tr':3,
          'ml':4,'mm':5,'mr':6,
          'll':7,'lm':8,'lr':9}


player1 = None
player2 = None

def checkGameWinner(board):
    for items in board.values():
        if (board['tl'] == 'X' and board['tm'] == 'X' and board['tr'] == 'X')\
                or (board['ml'] == 'X' and board['mm'] == 'X' and board['mr'] == 'X')\
                or (board['ll'] == 'X' and board['lm'] == 'X' and board['lr'] == 'X')\
                or (board['tl'] == 'X' and board['ml'] == 'X' and board['ll'] == 'X')\
                or (board['tm'] == 'X' and board['mm'] == 'X' and board['lm'] == 'X')\
                or (board['tr'] == 'X' and board['mr'] == 'X' and board['lr'] == 'X')\
                or (board['tl'] == 'X' and board['mm'] == 'X' and board['lr'] == 'X')\
                or (board['tr'] == 'X' and board['mm'] == 'X' and board['ll'] == 'X'):
            return True
        elif (board['tl'] == 'O' and board['tm'] == 'O' and board['tr'] == 'O') \
                or (board['ml'] == 'O' and board['mm'] == 'O' and board['mr'] == 'O') \
                or (board['ll'] == 'O' and board['lm'] == 'O' and board['lr'] == 'O') \
                or (board['tl'] == 'O' and board['ml'] == 'O' and board['ll'] == 'O') \
                or (board['tm'] == 'O' and board['mm'] == 'O' and board['lm'] == 'O') \
                or (board['tr'] == 'O' and board['mr'] == 'O' and board['lr'] == 'O') \
                or (board['tl'] == 'O' and board['mm'] == 'O' and board['lr'] == 'O') \
                or (board['tr'] == 'O' and board['mm'] == 'O' and board['ll'] == 'O'):
            return True
        else:
            return False



def welcomeMessg():
    print("-------Welcome to the Tic-Tac-Toe-------")

def players():
    global player1,player2
    player1 = input("Enter your name Player1:\t")
    player2 = input("Enter your name Player2:\t")

def toss():
    global player1, player2
    chance = random.randint(0,1)
    if chance == 0:
        return player1
    else:
        return player2

def printboard(board):
    print("\t\t\t\t",str(board['tl']) + '|' + str(board['tm']) + '|' + str(board['tr']))
    print("\t\t\t\t","-+-+-")
    print("\t\t\t\t",str(board['ml']) + '|' + str(board['mm']) + '|' + str(board['mr']))
    print("\t\t\t\t","-+-+-")
    print("\t\t\t\t",str(board['ll']) + '|' + str(board['lm']) + '|' + str(board['lr']))


welcomeMessg()
printboard(tboard)
players()
print("Waiting for Toss..........")
time.sleep(1)

# Playing the Game

counter = 0
secondplayer = None

firstplayer = toss()
if firstplayer == player1:
    secondplayer = player2
elif firstplayer == player2:
    secondplayer = player1

#for i in range(9):
move1 = None
while True:
    turn = 'X'
    move = input("Enter your position(tl,tm,tr,ml,mm,mr,ll,lm,lr)..."+firstplayer+"\t")
    if move == move1:
        print("Already filled. Enter another position ")
        continue
    if tboard.get(move,0) == 0:
        print("Wrong Input ")
        continue
    tboard[move] = turn
    if checkGameWinner(tboard) == True:
        print(firstplayer + " is the winner")
        break
    printboard(tboard)
    counter += 1
    if counter == 9:
        break
    if turn == 'X':
        while True:
            move1 = input("Enter your position(tl,tm,tr,ml,mm,mr,ll,lm,lr)..."+secondplayer+"\t")
            if move1 == move:
                print("Already filled. Enter another position ")
                continue
            turn = 'O'
            if tboard.get(move1,0) == 0:
                print("Wrong Input ")
                continue
            tboard[move1] = turn
            printboard(tboard)
            break
        if checkGameWinner(tboard) == True:
            print(secondplayer + " is the winner")
            break
        counter += 1
        if counter == 9:
            break

if checkGameWinner(tboard) == False:
    print("Its a Tie. Try Again!!!!")
print()
print("\t\t=======Game Over=======")
printboard(tboard)

"""
#Nested Dictionary
"""
cook = {'rice':{'whiterice':{'plate':101},'water':{'plate':102}},
        'lentils':{'yellowlentils':{'plate':103},'water':{'plate':104}},
        'vegetables':{'veggies':{'roger':105},'water':{'roger':106}}}

#print(cook['rice']['water']['plate'])
count = 0
for key,val in cook.items():
    print(val)                          #Will print 'whiterice' & 'water etc..
    for kl,vl in val.items():
        print(vl)                       #Will print 'plate'
        for kf,vf in vl.items():
            print(vf)                   #Will print 101,102.....
            store = (vl.get('plate',0))
            count += store

print(count)

"""

#Inventory Program: Fantasy Game Inventory

"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12,'spade':9}    #Dictionary

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']                  #List

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items: ",item_total)

def addToInventory(inventory, addedItems):
    for iter in addedItems:
        inventory.setdefault(iter, 0)               #List to dictionary         #String to dictionary
        inventory[iter] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','spade','spade',12,12]
mystring = "This is, a brand new world, is'nt it ?"

inv = addToInventory(inv, dragonLoot)
inv = addToInventory(inv, mystring)

displayInventory(inv)
#displayInventory(stuff)

"""
#Dictionary and List Sample Program

"""
name = input("Enter File Name... ")
handle = open(name)

mydict = dict()
totallen = 0
largestword = -1
wordlarge = None
for line in handle:
    words = line.split()
    print(words)
    totallen += (len(words))
    for iter in words:
        mydict.setdefault(iter,0)
        mydict[iter] += 1
        #mydict[iter] = mydict.get(iter,0) + 1          #This is One line implementation
        for k,v in mydict.items():
            #print(k,v)
            if v > largestword:
                largestword = v
                wordlarge = k
                print(largestword,wordlarge)


print(largestword,wordlarge)
#print(totallen)
pprint.pprint(mydict)

"""
#Strings

"""
print('Hel\'lo,Ho\'w are\'s you d\n\toing')         #Escape character
print(r'Hel\'lo,Ho\'w are\'s you d\n\toing')        #Raw String: It ignores escape character

spam = 'hellllllllllllll\"o,worl\'d'
print(spam[0:6])

mydict = {}
for iter in spam:
    print(iter,end=' ')
    mydict[iter] = mydict.get(iter,0) + 1
print('\tLength=',len(spam))
print(mydict)

name = 'Tanmay'
age = 30

print('My name is %s. I am %s years old.' % (name, age))            #Printing string using %s
print(f'My name is {name}. Next year I will be {age + 1}.')         #Printing f-strings

"""
#Ord and Char----Unicode
"""
print(ord('1'))
print(chr(55))
mystring = "A Am learning Python3!!!"
ordlist = []
chrlist = []
mydict = {}

for it in mystring:
    print(chr(ord(it)+1),end=' ')           #Conversion from ord to char

    ordlist.append(ord(it))                 #Adding to list
    chrlist.append(chr(ord(it)))

    mydict[it] = mydict.get(it,0) + 1       #Adding to dictionary

print()
print(ordlist)
print(chrlist)
print(mydict)

count = 0
for k,v in mydict.items():
    count += mydict.get(k,0)

print(count)
"""
#pyperclip.copy('Tanmay.......dahdhbfsudfdjgkfdghdfugfkngdfhgufdkgjdfgdjfgdfgdfngjdfgdkhdfgdg')

#String Methods
"""
while True:
    age = input("enter age...")
    if age.isdecimal():
        print(age)
        break
    else:
        print("Needs to be alphanumeric")

while True:
    name = input("Enter name.....")
    if (name.startswith('!!!') is False) and (name.endswith('!!!')):
        sep = name.split('!')
        print(sep[0])
        break
    else:
        print("Name should end with '!!!': ")
"""

#Split/Join/Partition String Methods

"""
stringlist = ['This','is', 'how', 'is', 'it']
joined = '!!!!'.join(stringlist)                    #join() is called on a string value and is passed a list value
joined_new = '1234'.join(joined)
print(joined)
print(stringlist)
print(joined_new)

splitlist = joined_new.split('!')                   #split() is called on a string value and returns a list of strings
print(splitlist)

newstring = "Hey, How's you doing, Arthur?"
partstring = newstring.partition('you')             #returns a tuple of three substrings for the “before,” “separator,” and “after” substrings
before, separtor, after = newstring.partition("'")
print(partstring)
print(before)
print(separtor)
print(after)

"""
# rstrip,lstrip,strip methods

"""
mystring = '              This is me!!!!              '
leftstrip = (mystring.lstrip())
rightstrip = (mystring.rstrip())
bothstrip =  (mystring.strip())

print(mystring)
print(leftstrip)
print(rightstrip)
print(bothstrip)
print(len(mystring))
print(len(leftstrip))
print(len(rightstrip))
print(len(bothstrip))

print()
mylist = []
mylist.append(mystring)
mylist.append(leftstrip)
mylist.append(rightstrip)
mylist.append(bothstrip)
#print(mylist)

print()
mydict = {}
for it in mylist:
    mydict[it] = mydict.get(it,0) + 1
for k,v in mydict.items():
    print(k,len(k))

print()
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))                   #Same Output
print(spam.strip('Spam'))                   #Same Output
print(spam.strip('pmaS'))                   #Same Output
"""

# rjust(), ljust(), and center() Methods

"""

mystring= "This is me"
rightspaced = (mystring.rjust(100,'='))
print(rightspaced)
leftspaced = (mystring.ljust(100,'='))
print(leftspaced)
center = mystring.center(50,'=')
print(center)

print()
def mypicnic(mydict,left,right):
    print("Picnic Items".center(left+right,'='))
    for k,v in mydict.items():
        print(str(k).ljust(left,'-'),str(v).rjust(right,'>'))

picnicdict = {'bag':5,'tent':2,'food':10}
mypicnic(picnicdict,50,50)

"""
#Regular Expressions-----Need More Practice

"""
mystring = "Two: times 4 equals: 8"

temp1 = re.findall('[0-9]+',mystring)
temp2 = re.findall('^T.+:',mystring)    #Greedy Matching
temp3 = re.findall('^T.+?:',mystring)   #Non Greedy Matching
print(temp1)
print(temp2)
print(temp3)

"""
#Sorted example

"""
mystring = "the lion finds the fox in the jungle and eats it alive alive alive alive alive and the lion then goes to slieep"

mydictwords = {}
mydictletters = {}
for iter in mystring:
    strip = mystring.rstrip()
    words = mystring.split()
    mydictletters[iter] = mydictletters.get(iter,0) + 1

for it in words:
    mydictwords[it] = mydictwords.get(it,0) + 1

mylistwords = []
for k,v in mydictwords.items():
    tup = (v,k)                                      #tuples created over here
    print(tup,end=" ")
    mylistwords.append(tup)                          #Creating a list of tuples
    newlist = sorted(mylistwords,reverse=True)       #Sorting the list by value in ascending order

print()
for v,k in newlist[:5]:                               #printing the first 5 elements of the Sorted list
    print(k,v)

print()
print(max(newlist))
print(min(newlist))



print()
print((words))
print(mydictwords)
print(mydictletters)
print(mylistwords)
print(newlist)

"""

#Enumerate and replace function
"""
mystring = "Wel_come t_o ye_ar 202_1"

wds = []

for it in mystring:
    wds = mystring.split()

for i,j in enumerate(wds):                  #Using the Enumerate function to print index in the list
    print(i,j)

print()
for k,l in enumerate(wds,start=10):
    print(k,l)

print(wds)
print(type(wds))

for rep in wds:
    rep = rep.replace('_','')               #Using replace function to replace parts of string
    print(rep,end='')
"""

#Some more Dictionary functions
"""
dict_a = {'t':1,'n':2}
dict_b = {'m':6,'z':100}

dict_c = {**dict_b,**dict_a}                #Merging two dictionaries

for k,v in dict_c.items():
    print(k,v)

from collections import Counter
mylist = [1,2,3,2,2,3,3,3,3,'hgf']

mydict = dict(Counter(mylist))              #Converting a list or tuple to dictionary
print(mydict)

"""
#Lambda Function: for Single line expressions only. It ceates function objects
""""
dict_a = {'t':1,'n':2,'gh':7}
dict_b = {'m':6,'z':100}

dict_c = lambda a,b: {**a,**b}                #Merging two dictionaries
print(dict_c(dict_a,dict_b))

mystring = "Two: times 4 equals: 8"

newstring = lambda teststring: re.findall('[0-9]+',teststring)
print(newstring(mystring))

def squarefunc(a):
    func = lambda a:a*a
    return func(a) + a

print(squarefunc(5))

def strsplit(mystr):
    strfun = lambda mystr:mystr.split()
    return strfun(mystr)

mystring = "I am here"
print(strsplit(mystring))

"""
#Reverse list in single line
""""
mylist = [1,2,3,4,5]

reverselist = mylist[::-1]
print(reverselist)

a,b,c,d,e = mylist              #Unpacking. Applicable to list,tuple,dict,string
print(a,b,c,d,e)

mystring = "hello"
a,b,c,d,e = mystring
print(a,b,c,d,e)
"""
#Weird Python
"""
#import this         #Displays poem
#import antigravity  #Opens web browser comic

y = 10
if (x :=  25) >= y:         #Walrus operator
    print(x)
    print(id(x))
"""

#Module : Its a single script. eg import time
#Packages : Collection of modules
#Libraries : Collection of packages. eg import numpy as np
#Frameworks : Entire Building blocks. eg Django,flask,kivy

"""
import numpy as az

num = az.random.rand(100)   #np=library, random = package, rand = function

print(len(num))
print(az.sum(num))
print(az.sum(num)/len(num))

"""

#Random Numbers Aren't Random
"""
random.seed(5)                      #The argument to function seed, denotes which random range is gonna get selected

mylist1 = []
for it in range(3):
    rn = random.randrange(3)
    #print(rn)                       #Will Print same range repeatedly
    mylist1.append(rn)

print(mylist1)

mylist2 = []
random.seed(time.time())
for it in range(3):
    rn = random.randrange(3)
    #print(rn)
    mylist2.append(rn)

print(mylist2)

counter = 0                             #This will check after how many tries the list got equalled
while True:
    time.sleep(1)
    print(mylist1)
    print(mylist2)
    if mylist1 == mylist2:
        print("Equal list encountered")
        break
    else:
        print("List not equal")
        del mylist2
        counter += 1
        mylist2 = []
        for it in range(3):
            rn = random.randrange(3)
            mylist2.append(rn)
        continue

print("Counter = ",counter)

"""

#Matplotlib graphs
"""
import numpy as np
import matplotlib.pyplot as plt




x = np.array([0,250,45,60])
y = np.array([50,100,30,10])


x1 = np.array([50,100,30,1])
y1 = np.array([0,250,45,60])
print("hello")
plt.plot(x,y,'*-.y',ms=10,mec='r',linewidth='2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph')
plt.plot(x1,y1,'*-.r',ms=10,mec='y',linewidth='2')
plt.grid()
plt.show(block=True)

"""
#Internet Basics : URL
"""
mystring = "https://www.youtube.com/watch?v=8DvywoWv6fI&t=35402s"

protocol = mystring.split("//")
web_addr = protocol[1].split('/')

host = web_addr[0]
document = web_addr[1]

print(f'Protocol : {protocol[0]}')
print(f'Host : {host}')
print(f'Document : {document}')

"""

#Any() and Zip() function
"""
mystringTrue = "This is me"
mystringFalse = ""
mylistTrue = [1,2,3,4]
mylistFalse = [False,False,0]
mydictTrue = {'t':1,'k':2}
mydictFalse = {}
mytupTrue = (3,'t')
mytupFalse = ()


print(any(mystringTrue))
print(any(mystringFalse))
print(any(mylistTrue))
print(any(mylistFalse))
print(any(mydictTrue))
print(any(mydictFalse))
print(any(mytupTrue))
print(any(mytupFalse))
print("=====================================================================")
#Zip Function
#The zip object yields n-length tuples, where n is the number of iterables
#passed as positional arguments to zip()

name = ['tanmay','rohit','samson']
age = [20,30,40]

z = list(zip(name,age))
print(z)

for n,a in z:
    print(n,a)

print(list(zip('abcdefg', range(7), range(4))))

"""

#args & kwargs
#*args and **kwargs let you write functions with a variable number of arguments in Python
#*args collects extra positional arguments as a tuple. **kwargs collects the extra keyword arguments as a dictionary

""""
def addnum(*args,**kwargs):
    print(args)
    print(kwargs)
    result = 0
    #result = sum(args)
    for i in args:
        result += i
    print(result)

    for k,v in kwargs.items():
        print(k,v)

addnum(1,2,3,4,5,6,7,8,9,10,key_1 = 3,key_2 = '4')
"""

#Sets
"""
my_set = {1,2,3,4,5,5,4,4,4,5,5,5}
my_set.add(38)
print(my_set)

print(type(my_set))
print(dir(my_set))

set_1 = {1,2,3,4,5}
set_2 = {2,3,4,5,6}
set_3 = {4,5,6,7,8}

#All operations are performed in respect to set 1
print(set_1.union(set_2,set_3))
print(set_1.intersection(set_2,set_3))
print(set_1.difference(set_3))
print(set_1.discard(5))
print(set_1)
print(set_1.update(set_2))
print(set_1)
"""

#String Replace method
"""
my_string = 'My python code for python python python strings !!!'
newstring = my_string.replace('python','Python',-1)
print(my_string)
print(newstring)
"""

#List Comprehensions
"""
mylist = [i*i for i in range(10) if i%2==0]
print(mylist)

def cube(m):
    return m*m*m

cubes = [cube(i) for i in range(10) if i%2==0]
print(cubes)

a = [1,2,3,4,5]
b = [0 if i < 3 else i for i in a]
print(b)

#Set Comprehension

mystring = "Welcome to this edition of Python practice"
unique_vowels = {i for i in mystring if i in 'aeiou'}
print(unique_vowels)

#Dictionary Comprehensions
my_dict = {i : i*i*i for i in range(10) if i % 2 == 0}
print(my_dict)

#Tuples
tupes = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(tupes)

#Nested 2d lists
matrix2d = [[i*j for i in range(5)] for j in range(3)]
print(matrix2d)
"""

#Matrix Printing
"""
days = 1

while days < 8:
    print(str(days)+":",end=" ")
    hours = 1
    while hours < 25:
        print(hours,end=" ")
        hours = hours + 1
    days = days+1
    print()

print("==================================================================================")

daysOfWeek = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
hoursofDay = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

for dw in daysOfWeek:
    print(dw + ':',end=" ")
    hours = 1
    for hours in hoursofDay:
        print(hours,end=" ")
        hours = hours + 1
    print()
"""

# Map,filter function : basic Introduction

"""
mlist = [1,2,5,8,9,12,5,2,3,-1,-5,0]

# map(function,sequence)

my_map = map(lambda x:x+2,mlist)
print(list(my_map))

# filter(function,sequence)

my_filter = filter(lambda x:x%2==0,mlist)
print(list(my_filter))

print("======================================")

mlist_new = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
my_map_sum = tuple(map(lambda x,y:x+y,mlist,mlist_new))
print(my_map_sum)
print(list(my_map_sum))

"""
# is and ==
# "==" denotes equality  (checks objects have same value)
# "is" denotes identity of the objects (checks if they have same memory locn)

"""
a = [1,2,3]
b = [1,2,3]

if a == b:
    print(True)
else:
    print(False)
print("==============")
if a is b:
    print(True)
else:
    print(False)
print("==============")

print("Memory address before assignment")
print(id(a))
print(id(b))
b = a
print("Memory address after assignment")
print(id(a))
print(id(b))

print("==============")
if a == b:
    print(True)
else:
    print(False)

print("==============")
if a is b:
    print(True)
else:
    print(False)
print("==============")

print(a)
print(b)
a[0] = 9
print(a)
print(b)

print("==============")
"""

# Unpacking : Tuples
# "_" is used to ignore variables

"""
a,b = (1,2)
print(a)
print(b)

#a,b,c,d = (1,2) #ValueError: not enough values to unpack (expected 4, got 2)
#a,b,c,d = (1,2,3,4,5)   #ValueError: too many values to unpack (expected 4)

#a,b,c = (1,2,3,4,5,6,7,8,9,10)  #ValueError: too many values to unpack (expected 3)
a,b,*c = (1,2,3,4,5,6,7,8,9,10)
print(a)
print(b)
print(c)
print("=========================")
a,b,*c,d = (1,2,3,4,5,6,7,8,9,10)
print(a)
print(b)
print(c)
print(d)

print("=========================")
a,b,*_,d = (1,2,3,4,5,6,7,8,9,10,11,22,25,75)
print(a)
print(b)
#print(c)
print(d)

"""

# Generators

"""
def gen():
    for x in range(10):
        #print(x**2)
        yield (x**2)


# 1st Method to print items of the generator func
#print(list(gen()))

# 2nd method using next pointer
my_gen = gen()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
#print(next(my_gen))         # It will cause StopIteration

# 3rd method : for loop

for n in gen():
    print(n,end=" ")
"""
# Iterating over integers
"""
num = 1236754127458675876849

my_str = str(num)

for it in my_str[::-1]:
    rev_int = int(it)
    print(rev_int,type(rev_int))

"""

# Finding and printing only unique nos

"""
def uniquenos(*args):
    mlist = []
    for num in args:
        mlist.append(num)
    print(list(set(mlist)))

uniquenos(1,2,3,4,5,5,5,5,55,6,2)
"""

