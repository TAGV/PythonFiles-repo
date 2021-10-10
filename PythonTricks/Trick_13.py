#Inserting & Removing elements in list via slicing

def Insert_at_start(mlist,item):
    mlist[0:0] = item
    print(mlist)

def Insert_at_end(mlist,item):
    mlist[len(mlist):len(mlist)] = item
    print(mlist)

def Insert_at_index(mlist,item,index):
    mlist[index:index] = item
    print(mlist)

def Remove_by_index(mlist,index):
    mlist.pop(index)
    print(mlist)

def Remove_by_item(mlist,item):
    mlist.remove(item)
    print(mlist)

def DeleteList(mlist,index1=None,index2=None):
    del mlist[index1:index2]
    print(mlist)

mylist = ['apples','oranges','bananas']

Insert_at_start(mylist,['mangoes'])         #Need those square brackets,since we are appending a list item
Insert_at_end(mylist,['pears'])

Insert_at_index(mylist,['avocado'],1)
Insert_at_index(mylist,['avocado'],2)
Insert_at_index(mylist,['avocado'],-1)

Remove_by_index(mylist,3)
Remove_by_item(mylist,'oranges')

DeleteList(mylist,2,4)
DeleteList(mylist)

print("=======================================")

mylist_numbers = [1,2,3,4,5]

Insert_at_start(mylist_numbers,[76])
Insert_at_end(mylist_numbers,[80])
Insert_at_index(mylist_numbers,[100],3)
Insert_at_index(mylist_numbers,[1000],-1)

Remove_by_index(mylist_numbers,3)
Remove_by_item(mylist_numbers,1000)

DeleteList(mylist_numbers,2,4)
DeleteList(mylist_numbers)