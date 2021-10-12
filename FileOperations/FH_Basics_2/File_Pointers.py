#Opening the file using context managers

with open("SimpleFile.txt",'r') as fhandle:
    myfile = fhandle.read(100)                  #Will read only 100 characters at a time
    print(myfile)

    print("File pointer is currently at: ",fhandle.tell())
    fhandle.seek(0)                                             #Move the file pointer to the starting position
    myfile = fhandle.read(100)
    print(myfile)

    print("===============================")
    while (len(myfile)) > 0:                    #Read only 100 chars at once
        print(myfile,end="")                    #Iteratively print 100 chars
        myfile = fhandle.read(100)              #Resetting the value,and at EOF this returns an empty string and breaks the loop
        #print("\nFile pointer is currently at: ", fhandle.tell())

print(fhandle.closed)

print("=============================================================")
with open("RegularFile.txt",'w') as fd:
    print(fd.tell())
    fd.seek(50)
    print(fd.tell())
    fd.write(" Hello, From Python")
    print(fd.tell())
    fd.seek(0)
    fd.write("Back to start..... ")
    print(fd.tell())
    fd.seek(25)
    fd.write("  Damn in middle!!!! ")
    print(fd.tell())


print(fd.closed)

print("=============================================================")
with open("FinalFiles.txt",'w') as frw:
    print(frw.tell())
    frw.seek(5)
    frw.write("Make No Noise!!!!!")
    print(frw.tell())
    frw.truncate(10)
    frw.write("Output is truncated!!!!!")
    print(frw.mode)
    print(frw.name)
    print(frw.readable())
    print(frw.tell())

print(frw.closed)