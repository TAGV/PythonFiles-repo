import numpy as np
import pandas as pd

# Notes
# 1d array is called as pandas series(indicated by 1 pair [] of square brackets)
# 2d/3d array is called as pandas dataframe(indicated by 2 pairs [[]] of square brackets)

# Creating a data frame using numpy arrays

data = np.array([[1,2],[3,4],[5,6]])
dtframe = pd.DataFrame(data,index=['row1','row2','row3'],columns=['col1','col2'])
print(dtframe)

# Creating a data frame using lists

dtlist = [[10,20],[30,40],[50,60]]
dtframelist = pd.DataFrame(dtlist,index=['row1','row2','row3'],columns=['col1','col2'])
print(dtframelist)

# Creating a data frame using dictionary

namelist = ['Roger','Ron','Jack','Aron']
agelist = [23,45,27,60]

m_dict = {'Name':namelist,'Age':agelist}
dict_frame = pd.DataFrame(m_dict)
print(dict_frame)
print()
# Creating a data frame using csv file

csv_data = pd.read_csv("/home/myubuntu/PycharmProjects/StudentsPerformance.csv")
#print(csv_data.head()) #Reading first 5 rows
#print(csv_data.head(10)) #Reading first 10 rows
#print(csv_data.tail()) #Reading last 5 rows
#print(csv_data.tail(10)) #Reading last 10 rows

# To display the whole table,enable them
#pd.set_option('display.max_rows',1000)
#pd.set_option('display.max_columns',8)
#print(csv_data)

#Basic Attributes, Functions and Methods

#print(csv_data.shape) # No of rows & colmns
#print(csv_data.index)
#print(csv_data.columns)
#print(csv_data.dtypes) #datatypes
#print(csv_data.info())  #dataframe information
#print(csv_data.describe()) #Basic statistics about the data

#print(len(csv_data))
#print(max(csv_data.index))
#print(min(csv_data.index))
#print(type(csv_data))
#print(dir(csv_data))

# Selecting a coloumn

print(csv_data['gender'])