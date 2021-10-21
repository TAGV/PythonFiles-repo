# Basic class Implementation
class Employee:
    bonus = 0.1

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = self.name + '.' + str(self.age) + '@google.com'

    def print_empNo(self):
        return ('{}------{}'.format(self.name, self.salary))

    def apply_bonus(self):
        self.salary += int(self.salary * self.bonus)


class Developer(Employee):
    bonus = 0.2

    def __init__(self, name, age, salary, lang):
        super().__init__(name, age, salary)
        # Employee.__init__(self,name,age,salary)            #This is another way of inheriting the methods
        self.lang = lang


class Manager(Employee):

    def __init__(self, name, age, salary, employeeList=None):
        super().__init__(name, age, salary)
        if employeeList == None:
            self.employeeList = []
        else:
            self.employeeList = employeeList

    def addEmployee(self,emp):
        self.employeeList.append(emp)

    def removeEmployee(self,emp):
        self.employeeList.remove(emp)

    def numEmployees(self):
        print(f'No of employees under manager {self.name} are {len(self.employeeList)}')

    def printEmployeeList(self):
        for it in self.employeeList:
            print('---->',it.name)

dev1 = Developer("Roger", 30, 50000, 'Python')
print(dev1.name, dev1.email, dev1.lang)

print(dev1.salary)
dev1.apply_bonus()
print(dev1.salary)

emp1 = Employee("Jon", 50, 80000)
print(emp1.salary)
emp1.apply_bonus()
print(emp1.salary)

dev2 = Developer("Lauren", 32, 60000, 'Python')
dev3 = Developer("Ralph", 34, 60000, 'Python')

print("===========================")

mng = Manager("Harry", 30, 50000,[dev1,dev2])
print(mng.name,mng.age,mng.email,mng.salary)

mng.addEmployee(dev3)
mng.removeEmployee(dev2)
mng.printEmployeeList()
mng.numEmployees()

print("===========================")

mng_1 = Manager("Novak", 55, 90000,[])
print(mng_1.name,mng_1.age,mng_1.email,mng_1.salary)
mng_1.addEmployee(dev2)
mng_1.printEmployeeList()
mng_1.numEmployees()

print("===========================")
print(mng_1.salary)
mng_1.apply_bonus()
print(mng_1.salary)

# print(help(Developer))                          # Shows the method resolution order
