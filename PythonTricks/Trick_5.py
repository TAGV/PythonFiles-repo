#*args and **kwargs let you write functions with a variable number of arguments in Python.
#For example, a design pattern you can use to extend the behavior of a parent class without having to
#replicate the full signature of its constructor in the child class.

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class AlwaysYellowCar(Car):
    def __init__(self, *args,**kwargs):
        super(AlwaysYellowCar, self).__init__(*args,**kwargs)
        self.color = 'yellow'
        print("Args = ",args)
        print("Kwargs = ",kwargs)


car_1 = AlwaysYellowCar("tesla","white")
print("=====================")
car_2 = AlwaysYellowCar(name='cadilla',color="blue")