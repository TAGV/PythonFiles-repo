#Basic class Implementation
class Employee:                                                         #Convention: class name be capitalized
    def __init__(self,name,age,number):                                 #init acts as a constructor
        self.name = name
        self.age = age
        self.number = number
        self.email = self.name + '.' + str(self.age) + '@google.com'

    def print_empNo(self):                                                #self is default necessary argument
        return ('{}------{}'.format(self.name,self.number))

emp1 = Employee('Roger',30,1272)
print(emp1.email)

print(emp1.print_empNo())                       #This is same o/p as below
print(Employee.print_empNo(emp1))

emp2 = Employee('Ralph',40,1000)
print(emp2.email)

print(emp2.print_empNo())                       #This is same o/p as below
print(Employee.print_empNo(emp2))


my_emp_list = [Employee('Rock',50,1112),Employee('Josh',30,5665),Employee('Jon',65,6666)]

for it in my_emp_list:
    print(it.print_empNo(),it.email)