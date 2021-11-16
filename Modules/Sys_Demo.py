import sys

#Shows the file path
print(sys.argv)

#Shows python PATH
print(sys.path)

# Identify Host OS
print(sys.platform)

# Shows path of python exe file
print(sys.executable)

#Modules
print(sys.modules)
print(sys.modules.keys())
print(sys.modules.values())

#Little or Big endian
print(sys.byteorder)

print(sys.stderr.write("This is an error!!!\n"))
print(sys.stdout.write("This is a regular line\n"))

#print(sys.copyright)
print(sys.version)

a = 10
b = 20.10
c = "Hello World"
d = [1,2,3,4,5]
e = {'a':1,'b':2}
f = (1,2)
print(sys.getsizeof(a),'bytes')
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(f))