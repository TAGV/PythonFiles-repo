# Sum calculation in single line
import random
import sys


def even_or_odd(sum):
    if sum % 2 == 0:
        print("The generated sum is even.")
    else:
        print("The generated sum is odd.")

mlist = []
for x in range(5):
    y = random.randrange(1,10)
    mlist.append(y)
    sys.argv.append(y)

print(mlist)

# Sys.argv contains strings:
# which are converted to integers
# by applying map function
# then are added using the sum module

mysum = sum(map(int,sys.argv[1:]))  # python3 Trick_26.py 4 3 4 5 6 7 8 9 1 2 3 4 5 6 7
print("Sum = ",mysum)
even_or_odd(mysum)
