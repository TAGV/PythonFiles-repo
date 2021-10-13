from collections import defaultdict

#Normal dictionary

my_normal_dict = {'a':1,'b':2}
print(my_normal_dict['a'])
#print(my_normal_dict['c'])              #This gives key error



#Default Dictionary

#my_def_dict = defaultdict(int)
#my_def_dict = defaultdict(float)
#my_def_dict = defaultdict(bool)
my_def_dict = defaultdict(list)

my_def_dict['a'] = 5
my_def_dict['b'] = 10
print(my_def_dict)
print(my_def_dict['c'])                 #No error,default value of type indicated in defaultdict is set
print(my_def_dict['d'])                 #No error