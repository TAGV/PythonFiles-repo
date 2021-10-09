#Fibonacci Series


def fibo(n):
    fib_list = []
    a,b = 0,1
    result = 0
    while a < n:
        fib_list.append(a)
        #a, b = b, a+b      #right hand side is evaluated first and then assigned to left hand
        c=a+b
        a = b
        b=c
        #print("a= ",a)
        #print("b= ",b)
    return fib_list


mylist = fibo(100)
print(mylist)

#Note:
#Python first evaluates the right-hand expression
#and stores the results on the stack, then takes those two values
#and assigns them to a and b. That means that a + b is calculated before a is changed.