# Using namedtuple is way shorter than
# defining a class manually

from collections import namedtuple

Car = namedtuple('Car','name color shade mileage')

my_car = Car('AV','red','dark',30)

print(my_car.color)
print(my_car.name)
print(my_car.mileage)
print(my_car)

for it in my_car:
    print(it,end=" ")

#my_car.color = 'blue'    Cant do this: Its immutable