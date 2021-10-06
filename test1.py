item = None
while True:
    try:
        item = input("Enter  ypur name\n")
        print(item)
        break
    except EOFError:
        #print ("EOFError")
        break




