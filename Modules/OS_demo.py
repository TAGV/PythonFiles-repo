import os

# get current working directory
print(os.getcwd())

# Change the current working directory to the specified path.
os.chdir("/home/myubuntu/PycharmProjects/pythonProject")
print(os.getcwd())

# List files and folders
print(os.listdir())

with open('/home/myubuntu/PycharmProjects/pythonProject/Modules/file_walk.txt','w') as fhandle:
    for dirpath, dirnames, filename in os.walk("/home/myubuntu/PycharmProjects/pythonProject"):
        fhandle.write("Directory_Path:\t\t") + fhandle.write(dirpath) + fhandle.write("\n")
        fhandle.write("Directories:\t\t") + fhandle.write(str(dirnames)) + fhandle.write("\n")
        fhandle.write("Files:\t\t") + fhandle.write(str(filename)) + fhandle.write("\n\n")



