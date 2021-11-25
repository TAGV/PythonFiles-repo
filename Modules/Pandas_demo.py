import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
pd.set_option('display.max_columns',10)
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
#print(csv_data['gender'])
#print(csv_data[['gender','reading score']])

# Adding a new coloumn

#csv_data['Language Score'] = 50

#Adding coloumn Using np array
#lang_score = np.arange(0,1000)
#csv_data['Language Score'] = lang_score

#Adding coloumn with random values
lang_random_score = np.random.randint(0,101,size=1000)
lang_random_float_score = np.random.uniform(0,100,size=1000)    #Creating random float values
csv_data['Language Score'] = lang_random_score
csv_data['Random Score'] = lang_random_float_score
#print(csv_data)

# Math operations on coloumn
print('Sum = ',csv_data['math score'].sum())
print('Mean = ',csv_data['math score'].mean())
print('Standard deviation = ',csv_data['math score'].std())
print('Count = ',csv_data['math score'].count())
print('Min = ',csv_data['math score'].min())
print('Max = ',csv_data['math score'].max())
print('Statistics for the column\n',csv_data['math score'].describe())

# Operations on rows
avg_score = (csv_data['math score']+csv_data['reading score']+csv_data['writing score'])/3
csv_data['Average Score'] = avg_score
print(csv_data.round(2)) #Rounding to 2 decimal places

# Category filter using value_count method
print(csv_data['gender'].value_counts())                # Categorize Males and females
print(csv_data['gender'].value_counts(normalize=True))  # Get percentages
#rint(csv_data.columns)
print(csv_data['parental level of education'].value_counts())


# Sorting the data frame

#print(csv_data.sort_values('Average Score'))   # Sorting in ascending order by score
#print(csv_data.sort_values('Average Score',ascending=False))   # Sorting in descending order by score

#Sorting by 2 columns
#print(csv_data.sort_values(['Random Score','Average Score']))

#Sorting in-place--permanent update to the table
print(csv_data.sort_values('Average Score',ascending=False,inplace=True))
#print(csv_data)

# Sorting by key function---Need to explore this more
#print(csv_data.sort_values('race/ethnicity',key=lambda col:col.str.lower()))


# Pivot function
# This is used to reshape the dataframe

#print(csv_data.pivot(index="Random Score",columns="parental level of education",values="Average Score"))


# Pivot Table
market_data = pd.read_excel("/home/myubuntu/PycharmProjects/supermarket_sales.xlsx")
#print(pd.pivot_table(market_data,index="Gender",aggfunc="sum"))
#print(pd.pivot_table(market_data,index="Gender",values=["Quantity","Total"],aggfunc="sum"))
#print(pd.pivot_table(market_data,index="Gender",columns="Product line",values="Total",aggfunc="sum"))

#===== Data Visualisation==========

pop_data = pd.read_csv("/home/myubuntu/PycharmProjects/population_total.csv")
#print(pop_data)

# Dropping the null values from the data
pop_data.dropna(inplace=True)
#print(pop_data)

# Creating the pivot table
pivot = pop_data.pivot(index="year",columns="country",values="population")
pivot = pivot[["India","China","Brazil","Nepal","Pakistan"]] # Assign it to the same dataframe
print(pivot)

# Plotting the data

# Line plot
pivot.plot(kind="line",xlabel="Year",ylabel="Population",title="Population(1955-2020)",figsize=(5,3))

# Save and export the plots and the dataframes
plt.savefig('/home/myubuntu/Desktop/my_line.png')
pivot.to_excel('/home/myubuntu/Desktop/line_data.xlsx')

# Bar plot
pivot_2020 = pivot[pivot.index.isin([2020])] # Creating pivot only for year 2020
pivot_2020 = pivot_2020.T    #Transposing rows and columns matrix
print(pivot_2020)

#pivot_2020.plot(kind="bar",xlabel="Year",ylabel="Population",title="Population(2020)",color="orange",figsize=(5,3))

# Creating new pivot for multiple years
years_plot = pivot[pivot.index.isin([1955,1975,1995,2005,2015,2020])]
years_plot = years_plot.T
print(years_plot)

years_plot.plot(kind="bar",xlabel="Year",ylabel="Population",title="Population(1955-2020)",figsize=(5,3))

# Save and export the plots and the dataframes
plt.savefig('/home/myubuntu/Desktop/my_bar.png')
years_plot.to_excel('/home/myubuntu/Desktop/bar_data.xlsx')

# Pie chart

# Rename the column

pivot_2020.rename(columns={2020:'2020'},inplace=True)   # Need to rename to convert from integer to string, else plot throws error

pivot_2020.plot(kind="pie",y="2020",title="Population in 2020(%)",figsize=(5,3))

# Save and export the plots and the dataframes
plt.savefig('/home/myubuntu/Desktop/my_pie.png')
pivot_2020.to_excel('/home/myubuntu/Desktop/pie_data.xlsx')


plt.show()  # Need to import matplotlib to see the plots

