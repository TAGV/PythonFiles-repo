#Sorting tuples using sorted function

#tuple : (x,y,z)
my_tup = [(4,3,7),(1,2,3),(10,25,5),(100,0,4)]
print(my_tup)
print("=======================================================")

my_sorted_tupes_x = sorted(my_tup)
print("Sorting by 1st element in tup: ",my_sorted_tupes_x)

my_sorted_tupes_y = sorted(my_tup,key=lambda x:x[1])
print("Sorting by 2nd element in tup: ",my_sorted_tupes_y)

my_sorted_tupes_z = sorted(my_tup,key=lambda x:x[2])
print("Sorting by 3rd element in tup: ",my_sorted_tupes_z)

print("=======================================================")

my_sorted_tupes_rev_x = sorted(my_tup,reverse=True)
print("Reverse sort by 1st element :  ",my_sorted_tupes_rev_x)

my_sorted_tupes_rev_y = sorted(my_tup,key=lambda x:x[1],reverse=True)
print("Reverse sort by 2nd element :  ",my_sorted_tupes_rev_y)