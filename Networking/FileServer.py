import socket

host = "localhost"
port = 6767

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Internet protocol version 4

s.bind((host,port))

print("Server listening on port:",port)

s.listen(1)

c,addr = s.accept()

fileName = c.recv(1024)

try:
    with open(fileName,"rb") as f:
        content = f.read()
        c.send(content)
except FileNotFoundError:
    c.send(b"File does not exist")

c.close()