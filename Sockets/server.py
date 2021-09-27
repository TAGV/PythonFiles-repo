import socket

s = socket.socket()
print("Socket created...")

s.bind(('localhost',9999))      #Bind port to ip address

s.listen(3)

while True:
    c,addr = s.accept()

    name = c.recv(1024).decode()                #decode is important
    print("Connected with...",addr,name)

    c.send(bytes("Hello from OuterWorld: " + name,"utf-8"))

    c.close()