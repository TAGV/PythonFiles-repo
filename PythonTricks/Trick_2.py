#Getting multiple inputs through single line from the user

while True:
    try:
        x,y = input("Enter 2 inputs separeted by comma...").split(',')
        break
    except ValueError:
        print("You need to enter 2 inputs...")
        continue

print('1st no : ' + x)
print('2nd no : ' + y)

