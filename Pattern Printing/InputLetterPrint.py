#Printing the letters and string(vertically) from the user input
import pprint


def letterPrintfunc(letter):
    rowlist = [1, 2, 3, 4, 5]
    collist_t = [1, 2, 3, 4, 5, 6]
    collist_a = [1, 2, 3, 4, 5, 6]

    if letter == 'T':
        for row in rowlist:
            for col in collist_t:
                if (row == 1 and col != 6) or (col == 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print()


    if letter == 'A':
        for row in rowlist:
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
            print()


    return None


def stringPrint(mystring):

    for let in mystring:
        letterPrintfunc(let)



user_let = input("Enter the letter to print : (T/A)\n")
letterPrintfunc(user_let)
user_str = input("Enter the string to be print :'TA' \n")
stringPrint(user_str)
