import socket

s = socket.socket()

s.connect(("localhost",4000))

while msg := s.recv(1024):
    print("Received: ",msg.decode())
s.close()