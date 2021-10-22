# walrus operator = Assignment Expression operator

import os
#for myfile in os.listdir("/home/myubuntu/PycharmProjects/pythonProject/"):
 #   print(myfile)

file_list = []
with open("/home/myubuntu/PycharmProjects/pythonProject/Test",'r') as fhandle:  #Always provide the absolute path
    while (myfile := fhandle.read(100)):
        file_list.append(myfile)

print(file_list)
print(len(file_list))

