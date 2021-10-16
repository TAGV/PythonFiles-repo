#Class variables are variables that we set inside a class, and are shared among all instances

class Employee:
    employee_count = 0                                              #Class/Static variable
    def __init__(self,name,age,number):
        self.name = name                                            #Instance Variable
        self.age = age
        self.number = number
        self.email = self.name + '.' + str(self.age) + '@google.com'
        Employee.employee_count += 1

    def print_empNo(self):
        return ('{}------{}'.format(self.name,self.number))


print("Total No of employees : ",Employee.employee_count)
emp1 = Employee('Roger',30,1272)
print(emp1.email)

print(emp1.print_empNo())
print(Employee.print_empNo(emp1))

emp2 = Employee('Ralph',40,1000)
print(emp2.email)

print(emp2.print_empNo())
print(Employee.print_empNo(emp2))

my_emp_list = [Employee('Rock',50,1112),Employee('Josh',30,5665),Employee('Jon',65,6666)]
for it in my_emp_list:
    print(it.print_empNo(),it.email)


print("Total No of employees : ",Employee.employee_count)


#checking the namespace of the instances and the class
print("============================================================================================")

print(Employee.__dict__)                                    #namespace of the class
print(emp1.__dict__)                                        #namespace of the instance

Employee.employee_count = 40                                #Value gets modified and shared by every instance
emp1.employee_count = 20                                   #Value modified only for that particular instance

print("Total No of employees : ",emp1.employee_count)       #20         Class var is used as instance var
print("Total No of employees : ",emp2.employee_count)       #30
print()
print("Total No of employees : ",my_emp_list[0].employee_count)
print("Total No of employees : ",my_emp_list[1].employee_count)
print("Total No of employees : ",my_emp_list[2].employee_count)

#Employee.name      #Not Allowed

#Use of isinstance function

checkinstance = isinstance(emp1,Employee)
print(checkinstance)
