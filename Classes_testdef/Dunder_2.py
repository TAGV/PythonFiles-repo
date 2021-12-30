#Extending an already present class via Inheritance

import inspect
from queue import Queue
from random import Random


q1 = Queue()
print(q1)

r1 = Random()
print(r1)

#print(inspect.getsource(Queue))
#print(inspect.getsource(Random))


class My_R(Random):
    def __repr__(self):
        return f"{self.getstate()}"



r = My_R()
print(r)






