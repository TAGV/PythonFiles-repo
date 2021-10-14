#Testing my package added in: "~/.local/lib/python3.8/site-packages/random_list"

from random_list import randlist as rl

#help(rl)

mylist = []
mylist = rl.random_list(10,100)
print(mylist)

res = 0
for it in mylist:
    res += it

print("Sum of nos in list = ",res)