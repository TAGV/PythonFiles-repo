#Factorial of a number

#5! = 5*4*3*2*1 = 120

def fact_num(n):
    factorial = 1
    if n == 0:
        print(factorial)
    else:
        for it in range(1,n+1):
            factorial = factorial * it
        print(factorial)

def recur_fact(n):
    if n == 0:
        return 1
    return n * recur_fact(n-1)

user_input = int(input("Please input the number to get its factorial....\n"))
fact_num(user_input)
print("========================")
print(recur_fact(user_input))