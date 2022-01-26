
#Palindrome String Checker
"""
import sys

mstr = 'astrtsa'

n = (len(mstr))

first = 0
last = n-1

while (first<last):
    if mstr[first] == mstr[last]:
        first += 1
        last -= 1
    else:
        print("Not Palindrome")
        sys.exit()

print("Palindrome")

"""
#Palindrome Number Checker
"""
num = 144444441
temp = num

rev_num = 0

while(temp > 0):
    d = temp % 10 # 1 4 1
    rev_num = rev_num*10 + d #1 14 141
    temp = temp // 10 # 14 1 0

if rev_num == num:
    print("Palindrome")
else:
    print("Not Palindrome")
"""

# Fibonacci series till nth number
"""
n = 50

a,b = 0,1
print(a)
while (b<n):
    print(b)
    a,b = b,a+b

"""

# Fibonacci series of n numbers
"""
n = 50

a,b = 0,1
print(a)
counter = 0
while (counter<n):
    print(b)
    a,b = b,a+b
    counter += 1

"""

# Compressed strings
# aabb = a2b2
"""
mstr = 'aabbbcccccddddddttttaaaazzzzzfgf'

mdict = {}

for n in mstr:
    mdict[n] = mdict.get(n,0) + 1

print((mdict))

mlist = []
for k,v in mdict.items():
    mlist.append(k+str(v))

print(mlist)

compressed_str = ''.join(mlist)
print(compressed_str)

"""

# FizzBuzz using dictionary
"""
num = 100

mdict = {3:'fizz',5:'buzz'}

for n in range(1,num+1):
    res = ''
    for k,v in mdict.items():
        if n%k == 0:
            res = res + v
    if not res:
        res = str(n)
    print(res)
"""

# Least occurence of charcater in the string
"""
mstr = 'dfdfgdfgdhghfcfgdhf'

mdict = {}

for n in mstr:
    mdict[n] = mdict.get(n,0) + 1

print(mdict)
print(min(mdict,key=mdict.get))
"""

# String Formatting - Part 1
"""
mstr = 'This_is_me'

mlist = mstr.split('_')
print(mlist)

print('.'.join(mlist))

"""
# String Formatting - Part 2
"""
mstr = 'This_Is_A_Me'

mlist = []

for ch in mstr.split('_'):
    mlist.append(ch[0].lower() + ch[1:].upper())

#print(mlist)

print('.'.join(mlist))      # tHIS.iS.a.mE

"""

# 2nd highest no in list

"""
mlist = [2,4,5,7,12,67,100,32]

mlist.sort()
print(mlist[-2])
"""

# Armstrong no

# 153 = 1*1*1 + 5*5*5 + 3*3*3
"""
num = 153

temp = num
sum = 0

while temp > 0:
    d = temp % 10 #3 5
    sum = sum + (d**3)  #9 152
    temp = temp // 10 #15 1

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong No")
"""

# Armstrong no in range

# 153 = 1*1*1 + 5*5*5 + 3*3*3

"""
start = 0
end = 1000

for num in range(start,end+1):
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10 #3 5
        sum = sum + (d**3)  #9 152
        temp = temp // 10 #15 1
    if sum == num:
        print(num)

"""

# Factorial

# 145 = 1! + 4! + 5! = 1 + 24 + 120

# Krishnamurthy numbers
"""
start = 0
end = 50000

for num in range(start,end+1):
    temp = num
    sum = 0
    while temp > 0:
        fact = 1
        d = temp % 10 #5
        for i in range(1,d+1):
            fact = fact*i #5*4*3*2*1
        sum = sum + fact
        temp = temp // 10 #14

    if sum == num:
        print(num)
"""