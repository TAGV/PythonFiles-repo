rowlist = [1,2,3,4,5]
collist_t = [1,2,3,4,5,6]
collist_a = [1,2,3,4,5,6]
collist_n = [1,2,3,4,5,6]
collist_m = [1,2,3,4,5,6]
collist_y = [1,2,3,4,5,6]

print("Name Starts".center(100,"="))
print()
for row in rowlist:
    for col in collist_t:
        if (row == 1 and col != 6) or (col == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for col in collist_a:
        if (row == 1 and col == 3):
            print("*", end=" ")
        elif (row == 2) and (col == 2 or col == 4):
            print("*", end=" ")
        elif (row == 3) and (col == 2 or col == 3 or col == 4):
            print("*", end=" ")
        elif (row == 5) and (col == 1 or col == 5):
            print("*", end=" ")
        elif (row == 4) and (col == 1 or col == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for col in collist_n:
        if col == 1 or col == 5:
            print("*", end=" ")
        elif (row==col == 2) or (row==col == 3) or (row==col == 4):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    for col in collist_m:
        if col == 1 or col == 5:
            print("*", end=" ")
        elif (row == 2) and (col == 2 or col == 4):
            print("*", end=" ")
        elif (col == 3) and (row == 3 or row == 4 or row == 5):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    for col in collist_a:
        if (row == 1 and col == 3):
            print("*", end=" ")
        elif (row == 2) and (col == 2 or col == 4):
            print("*", end=" ")
        elif (row == 3) and (col == 2 or col == 3 or col == 4):
            print("*", end=" ")
        elif (row == 5) and (col == 1 or col == 5):
            print("*", end=" ")
        elif (row == 4) and (col == 1 or col == 5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for col in collist_y:
        if (row == 1 and col % 4 == 1) or (row == 2 and col % 4 == 1):
            print("*", end=" ")
        elif (row == 3 and col % 2 == 0 and col != 6):
            print("*", end=" ")
        elif (col == 3) and (row == 5 or row == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
print()
print("Name Ends".center(100,"="))