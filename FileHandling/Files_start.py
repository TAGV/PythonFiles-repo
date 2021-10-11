#File Handling Basics

#fhandle = open("test_file.txt",'r')       #Reading the file
#print(fhandle.read())                   #Reads the whole file
#print(fhandle.readline())               #Reads a single Line
#print(fhandle.readline(5))               #Reads only first 5 charcters of the line

#fhwrite = open("writefile.txt",'w')             #Opens the file for Writing
#fhwrite.write("Hello ")                         #Only takes single string argument
#fhwrite.write(" Welcome to the Jungle ")
#fhwrite.writelines(["Bye"," Nobody"])           #It can take lists as arguments

#fappend = open('writefile.txt','a')                     #Opens the file for appending
#fappend.write(" This is an appended comment \n")

#fhandle.closed
#fhwrite.closed
#fappend.closed

#Copying Data between two files

print("===============Operations on a Text data file==========")

fcopy = open("EmptyTest", 'r')
print(fcopy.read())

fwrite_file = open("newfile.txt", 'w')
for data in fcopy:
    fwrite_file.write(data)

print("===============Operations on a binary data file==========")

fimgrd = open("IMG.jpg", 'rb')                       #Open the image file in binary format
#print(fimgrd.read())

fimgpst = open("image1.jpg", 'wb')                    #Create a new file in binary format
for data in fimgrd:
    #print(data,end="")
    fimgpst.write(data)

fcopy.close()
fwrite_file.close()
fimgrd.close()
fimgpst.close()

#print(fimgrd.read())                               #This will throw an error