import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
print(f'Mensaje recibido: {s.recv(1024).decode()}')
s.close()
