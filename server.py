import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(f'Got connection from: {addr}\tSocket: {c}')
    msg = 'Gracias por conectarte.'
    c.send(msg.encode())
    c.close()
