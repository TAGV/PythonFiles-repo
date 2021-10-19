#HELP method to retrieve the information about methods/functions in python
import sys


def GetHelp(method):
    help(method)

while True:
    myinput = input("Enter the function/method, you require information about.....or q to Quit? \n ")
    if myinput == 'q':
        sys.exit()
    GetHelp(myinput)

