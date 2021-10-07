#Remove the duplicates from the list

mylist = [1,2,3,4,5,6,23,45,12,89,100,3,4,5,23,45,35,101,'this','cat','is','mine','this']

list_no_duplicates = list(set(mylist))              #set is unique,hence all duplicate entries are removed

print(list_no_duplicates)


max_repeated = max(set(mylist),key=mylist.count)
print(max_repeated)

min_repeated = min(set(mylist),key=mylist.count)
print(min_repeated)