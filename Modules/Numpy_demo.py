import numpy as np
from numpy import random

# Creating numpy arrays
mlist = [1,2,3,4,5]
num_array_1 = np.array(mlist,dtype=np.int8)     # 1-d array

print(num_array_1)
print(type(num_array_1))
print(num_array_1.dtype)

# Creating a multidimensional array
nlist = [[1,2,3],[2,3,4],[3,4,5]]
num_arr_2 = np.array(nlist)
print(num_arr_2)

# Getting the datatype
print(num_arr_2.dtype)

# Creating a range of numbers
print(np.arange(1,10))

# Creating floating numbers
print(np.linspace(0,5,5))

# Zeros and Ones
print(np.zeros(10))     # 1-d array
print(np.zeros((2,3)))  # 2-d array

print(np.ones(10))      # 1-d array
print(np.ones((2,3)))   # 2-d array

# Getting the size of the array
print(num_arr_2.size)

# Generating random numbers
print(np.random.randint(1,10,5))            # 1-d array
print(np.random.randint(1,10,size=(2,3)))   # 2-d array
