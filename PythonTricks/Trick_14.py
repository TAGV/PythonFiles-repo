#List vs List Comprehension
#Time Required to process a simple list is twice that of list comprehension

from timeit import default_timer as timer
import sys

start = timer()
mylistcomp = [i*i for i in range(1_000_000)]                #Check the way of representing 1 million in more readable format
end = timer()
print("Total processing time for List comprehensions : ",str(end - start).rjust(50," "))
#print(sys.getsizeof(mylistcomp))


start = timer()
mylist = []
for i in range(1_000_000):
    mylist.append(i*i)
end = timer()
print("Total processing time for List : ",str(end - start).rjust(65," "))
#print(sys.getsizeof(mylist))                           #This will be explained while studying abt generators