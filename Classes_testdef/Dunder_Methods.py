# Creating our own class using Dunder/Magic methods or Data model methods
import inspect

class MyPython():

    """This is a test class"""
    def __init__(self,name):
        self.name = name

    def __repr__(self):                             #This returns string
        return f"{'*** '}{self.name}{' ***'}"

    def __mul__(self, other):                       #Multiply
        if type(other) is not int:
            raise Exception("Not an integer")

        self.name *= other

    def __len__(self):
      return len(self.name)



p1 = MyPython("Roger")
print(p1)
#p1 * 'str'
p1 * 5
print(p1)
print(len(p1))

print(inspect.getsource(MyPython))  #displays the source code of a class
print(inspect.getdoc(MyPython))     #displays the doctsring of the string
