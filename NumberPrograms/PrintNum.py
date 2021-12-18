#Printing Digits on different line

def PrintNum(n):
    m = n
    while m!=0:
        d = m%10
        print(d)
        m = m//10

def checkdigits(n):
    m = str(n)
    count = 0
    for i in m:
        count += 1
    print("No of digits in the number: ",count)
    print(10**(count-1))


takeinput = int(input("Enter a number "))
PrintNum(takeinput)
checkdigits(takeinput)