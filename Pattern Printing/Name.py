#Name Printing Vertical

for row in range(5):
    for col in range(5):
        if (row == 0) or (col == 2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()
for row in range(5):
    for col in range(5):
        if (row == 0 and col == 2):
            print("*", end=" ")
        elif (row == 1) and (col == 1 or col == 3):
            print("*", end=" ")
        elif (row == 2) and (col == 1 or col == 2 or col == 3):
            print("*", end=" ")
        elif (row == 4) and (col == 0 or col == 4):
            print("*", end=" ")
        elif (row == 3) and (col == 0 or col == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

for row in range(5):
    for col in range(5):
        if col == 0 or col == 4:
            print("*", end=" ")
        elif (row==col == 1) or (row==col == 2) or (row==col == 3):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(5):
    for col in range(5):
        if col == 0 or col == 4:
            print("*", end=" ")
        elif (row == 1) and (col == 1 or col == 3):
            print("*", end=" ")
        elif (col == 2) and (row == 2 or row == 3 or row == 4):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(5):
    for col in range(5):
        if (row == 0 and col == 2):
            print("*", end=" ")
        elif (row == 1) and (col == 1 or col == 3):
            print("*", end=" ")
        elif (row == 2) and (col == 1 or col == 2 or col == 3):
            print("*", end=" ")
        elif (row == 4) and (col == 0 or col == 4):
            print("*", end=" ")
        elif (row == 3) and (col == 0 or col == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

for row in range(5):
    for col in range(5):
        if (row == 0 and col % 4 == 0) or (row+col == 5 and col != 1):
            print("*", end=" ")
        elif (row - col == 1 and col != 3):
            print("*", end=" ")
        elif (row == 4 and col == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
