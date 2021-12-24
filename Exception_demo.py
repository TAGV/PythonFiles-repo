#This gives a demo of exceptions
import platform
import sys

# Example 1

try:
    file = open("requirements.txt")
    #file = open("sdfsdfsd.txt")
    #if file.name != "tant.text":
     #   raise Exception
except Exception as e:
    print(e)
    print("Error!!!")
else:
    print("In else block!!!")
    print(file.read(100))
    file.close()
    print(file.closed)
finally:
    print("Terminate")


# Example 2

# Creating subclass of Exception class
class WrongError(Exception):
    pass

platform_name = (platform.platform())

if not platform_name.startswith("Linux"):      # Try giving a different OS name to see the error
    raise WrongError(".....Wrong Platform")

print("End!!!")
