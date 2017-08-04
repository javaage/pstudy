import socket

s = socket.socket()
addr = socket.gethostname()
port = 12345

s.connect((addr,port))
print(s.recv(1024))
s.close()