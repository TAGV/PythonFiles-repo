#Eliminating repeating charcters from a string
"""
string = 'Indiaismycountry'

mydict = {}

#Finding repeating char:
for character in string:
    mydict.setdefault(character,0)
    mydict[character] += 1
print(mydict)

#Creating the elimination list
elimination_list = []
for k,v in mydict.items():
    if v > 1:
        elimination_list.append(k)

print(elimination_list)

# Printing final non-repeating charcters
for ch in string:
    if ch not in elimination_list:
        print(ch,end=' ')
"""
# Checking if number is power of 2
"""
num = 300
flag = 0
power_count = 0
temp_num = num

def divfun(num):
    numerator = num // 2
    denominator = num % 2
    return numerator,denominator

while (num > 0):
    alpha,beta = divfun(num)
    num = num//2
    power_count += 1
    #print(alpha, beta)
    if (beta == 1) and (alpha != 0):
        flag = 1
        break


if flag == 1:
    print("Number "+str(temp_num)+" is not power of 2")
else:
    print("Number "+str(temp_num)+" is power of 2")
    print('Power raised to : ',power_count-1)

"""

# Converting number to Indian standard notation

"""
num = 1_00_00_000   #10,10,23,456
mlist = []

def divide_by_thousand(num):
    numerator = num // 1000
    denominator = num % 1000
    return numerator,denominator

def divide_by_hundred(num):
    numerator = num // 100
    denominator = num % 100
    return numerator,denominator

alpha, beta = divide_by_thousand(num)
if beta == 0:
    mlist.append('000')
else:
    mlist.append(str(beta))
num = num//1000

while (num > 0):
    n,m = divide_by_hundred(num)
    if m == 0:
        mlist.append('00')
    else:
        mlist.append(str(m))
    num = num // 100
    if num == 0:
        break

#print(mlist)

rev_list = (mlist[::-1])
#print(rev_list)

mystr = ','.join(rev_list)
print(mystr)

"""

#Creating the nested lists
#[[1,2],[1,2]]
"""
mlist = []
nlist = []

for m in range(1,5):
    mlist = []
    for n in range(1,5):
        mlist.append(n)
    nlist.append(mlist)

print(nlist)
"""

# Removing the duplicate from the string

"""
mstring = "The quick quick fox jumps jumps over the cliff"

mlist = mstring.split(" ")
#print(mlist)

mdict = {}

for word in mlist:
    mdict[word] = mdict.get(word,0) + 1

    #Logic the eliminate the duplicate and keep a single copy
    if mdict[word] > 1:
        mdict[word] = 1


print(mdict)
nlist = []
for k,v in mdict.items():
    if v == 1:
        nlist.append(k)

#print(nlist)
new_string = " ".join(nlist)
print(new_string)

"""

# Printing the nos without comma at the end

## 1st Method
mlist = [1,2,3,4,5]
nlist = []

for it in mlist:
    nlist.append(str(it))

#print(nlist)

mstring = ",".join(nlist)
print(mstring)

## 2nd Method
for temp in mlist:
    if temp == mlist[-1]:
        print(temp,end='')
    else:
        print(temp,end=',')
