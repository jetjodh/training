import socket
import struct
from database import dct
def get_ip():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect(("8.8.8.8",80))
	return sock.getsockname()[0]
	sock.close()
ip=get_ip()
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((ip,12345))
sock.listen(5)
connection,client_address=sock.accept()
print('Got a connection from %s'%str(client_address))
try:
	while True:
		data=connection.recv(1024)
		key=data.decode('ascii')
		if key in dct:
			print(dct[key])
			connection.sendall((dct[key]).encode('ascii'))
		else:
			dct[key]=input('Enter the name')
			print('Record Added')
			connection.sendall((dct[key]).encode('ascii'))
finally:
	connection.close()

