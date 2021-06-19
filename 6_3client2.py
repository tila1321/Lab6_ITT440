import socket

ClientSocket = socket.socket()
IP = '192.168.56.110'
port = 5567

print('Waiting for connection')
try:
    ClientSocket.connect((IP, port))
except socket.error as e:
    print(str(e))



Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input = input('')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))


ClientSocket.close()
