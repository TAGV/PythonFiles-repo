#Conversion of numbers

#print(int(0b110001))
#print(int(0x3ff))
#print(int(0o123))

mystring = "Welcome to Number Conversion calculator!!!"
print(mystring.upper().center(100,'=')+"\n")

def to_binary(number):
    number_to_binary = bin(int(number))[2:]                 #first two hex charcters are hidden
    print(number_to_binary)


def to_decimal(number):
    number_to_decimal = int(number)
    print(number_to_decimal)

def to_hexa(number):
    number_to_hexa = hex(int(number))[2:]
    print(number_to_hexa)

def to_octal(number):
    number_to_octal = oct(int(number))[2:]
    print(number_to_octal)

num = input("Enter a number to convert to binary:0b/decimal/hexadecimal:0x/octal:0o....\n")
convert_to = input("Convert to binary/decimal/hexadecimal/octal....b/d/h/o...\n")
if convert_to == 'b':
    if num[:2] == '0x':
        to_binary(int(num,16))
    elif num[:2] == '0o':
        to_binary(int(num,8))
    elif num[:2] == '0b':
        print(num[2:])
    else:
        to_binary(num)
elif convert_to == 'd':
    if num[:2] == '0x':
        to_decimal(int(num,16))
    elif num[:2] == '0o':
        to_decimal(int(num,8))
    elif num[:2] == '0b':
        to_decimal(int(num,2))
    else:
        to_decimal(num)
elif convert_to == 'h':
    if num[:2] == '0x':
        print(num[2:])
    elif num[:2] == '0o':
        to_hexa(int(num,8))
    elif num[:2] == '0b':
        to_hexa(int(num,2))
    else:
        to_hexa(num)
elif convert_to == 'o':
    if num[:2] == '0x':
        to_octal(int(num,16))
    elif num[:2] == '0o':
        print(num[2:])
    elif num[:2] == '0b':
        to_octal(int(num,2))
    else:
        to_octal(num)
else:
    print("Invalid Input!!!")

