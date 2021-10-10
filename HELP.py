#HELP method to retrieve the information about methods/functions in python

def GetHelp(method):
    help(method)

myinput = input("Enter the function/method, you require information about.....? \n ")
GetHelp(myinput)

