from collections import namedtuple

#Returns a new subclass of tuple with named fields.

Coords = namedtuple('Coords','Value1,Value2')
cd = Coords(100,-10)
print(cd.Value1,cd.Value2)

sum = cd.Value1 + cd.Value2
print(sum)

mydict = cd._asdict()               #Conversion to dictionary
print(mydict)

x,y=(Coords(**mydict))              #Converting back from Dictionary
print(x,y)
