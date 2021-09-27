import socket

c = socket.socket()
print("This is client...")

c.connect(("localhost",9999))               #Client socket does not need binding. It only connects to the server

name = input("Enter your name.... ")
c.send(bytes(name,"utf-8"))

print(c.recv(1024).decode())