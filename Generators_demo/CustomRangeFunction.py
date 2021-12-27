# We will create a custom range function using generators

class MyRangeGen():
    current = 0                     #Var to store current number value
    def __init__(self,first,last):
        self.first = first
        self.last = last

    #Calling the iterator dunder method
    def __iter__(self):
        return self         #Will return the class

    #Logic for next number generation
    def __next__(self):
        if MyRangeGen.current < self.last:
            number = MyRangeGen.current
            MyRangeGen.current += 1
            return number
        raise StopIteration



g1 = MyRangeGen(0,100)
print(list(g1))