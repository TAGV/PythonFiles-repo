import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("In mysocket")

mysocket.connect(('data.pr4e.org',80))

mysocket.send(bytes("GET http://data.pr4e.org/romeo.txt HTTP/1.0 \n\n","utf-8"))
#cmd = 'GET https://data.pr4e.org/romeo.txt HTTPS/1.0\n\n'.encode()
#mysocket.send(cmd)

while True:
    data = mysocket.recv(512).decode()
    if len(data) < 1:
        break
    print(data)
mysocket.close()
