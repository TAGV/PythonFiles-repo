import sys

while True:
    try:
        item = input("Enter  ypur name\n")
        print(item)
        break
    except EOFError:
        #print ("EOFError")
        print(item)
        break



#sys.exit()

