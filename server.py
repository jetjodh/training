import socket
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
		data=connection.recv(256)
		if data:
			print('Hi')
			connection.send(data)
		else:
			break
finally:
	connection.close()

