class Auto:
    counter = 0

    def __init__(self,name,age):            #self: It is an alias to created instance of the class
        self.name = name                    # a1.name = name
        self.age = age                      # a1.age = age
        print("I am constructor:", self.counter)


    def pr(self):
        self.counter = self.counter + 1
        print(f'Name = {self.name}\nAge = {self.age}')
        print(f'Counter = {self.counter}')


    def __del__(self):
        print("I am destructor:",self.counter)


class Test(Auto):                                       #Inheritance of class
    def __init__(self,name,age,color):
        super(Test, self).__init__(name,age)            #Inheritance of attributes
        #self.name = name
        #self.age = age
        self.color = color
        print("I am constructor in child class")

    def pr(self):
        print(f'{self.name} {self.age} {self.color}')

    def __del__(self):
        print("I am destructor in child class")


a1 = Auto('tanmay',25)
#a1.pr()
#a1.pr()
#a1.pr()
#a1.pr()


for it in range(5):
    a1.pr()

print(dir(a1))

a2 = Auto('Tim',30)
a2.pr()
a2.pr()

t1 = Test('Roger',40,'black')
t1.pr()
t1.pr()
t1.pr()

#Basics of OOP:Start
x = 'hi'            #Creating a String class Object ...."=" operator denotes that
x.upper()           #Calling method of String class ...."." operator denotes that
