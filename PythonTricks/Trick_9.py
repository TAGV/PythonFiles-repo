#Conversion of numbers

print(int(0b110001))
print(int(0x3ff))
print(int(0o123))


def to_binary(number):
    number_to_binary = bin(int(number))[2:]                 #first two hex charcters are hidden
    print(number_to_binary)


def to_decimal(number):
    number_to_decimal = int(number,8)
    print(number_to_decimal)

def to_hexa(number):
    number_to_hexa = hex(int(number))
    print(number_to_hexa)

def to_octal(number):
    number_to_octal = oct(int(number))
    print(number_to_octal)

num = input("Enter a number to convert to binary/decimal/hexadecimal/octal....\n")
convert_to = input("Convert to binary/decimal/hexadecimal/octal....b/d/h/o...\n")
if convert_to == 'b':
    if num[:2] == '0x':
        to_binary(int(num,16))
    else:
        to_binary(num)
elif convert_to == 'd':
    to_decimal(num)
elif convert_to == 'h':
    to_hexa(num)
elif convert_to == 'o':
    to_octal(num)
else:
    print("Invalid Input!!!")

