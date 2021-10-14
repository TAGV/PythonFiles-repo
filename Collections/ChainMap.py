#A ChainMap groups multiple dicts (or other mappings) together
#to create a single, updateable view.

from collections import ChainMap

mydict = {'a':1,'b':2,'c':3}
newdict = {'d':4,'e':5,'f':6}

mCM = ChainMap(mydict,newdict)

print(mCM)


for k,v in mCM.items():
    print(k,v)



#help(ChainMap)