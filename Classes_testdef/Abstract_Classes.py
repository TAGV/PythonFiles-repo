from abc import ABC, abstractmethod


class Theatre(ABC):  # Need to inherit from abstract class ABC

    @abstractmethod  # Error: Can't instantiate abstract class Theatre with abstract methods lights
    def lights(self): pass  # Need to implement this method in subclass


class Actor(Theatre):  # Subclassing the abstract Theatre class
    def lights(self):   # Implementing the Abstract method
        print("Lights are on")


#tw = Theatre()     # This throws an error. Abstract class cannot be instantiated
tt = Actor()
print(tt)

tt.lights()

print(help(Actor))  # Method resolution order
