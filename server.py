# server.py
import socket
import pickle
# To include dictionary contained in database.py, import database.py making sure both are in same directory 
with open('dct.pickle','rb') as f:
        dct=pickle.load(f)
def get_ip():
	"""
	Function used to find out current ip address of the server
	""" 
	# create a socket object
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect(("8.8.8.8",80))
	return sock.getsockname()[0]
	sock.close()
ip=get_ip()
print(ip)
# create a socket object
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind to the port
sock.bind((ip,12345))
# queue up to 5 requests
sock.listen(5)
# establish a connection
connection,client_address=sock.accept()
print('Got a connection from %s'%str(client_address))
try:
	while True:
		# Receive no more than 1024 bytes
		data=connection.recv(1024)
		# Data is decoded from ascii into str and stored in key
		key=data.decode('ascii')
		# Checking if the code sent is present in database
		if key in dct:
			print(dct[key])
			# Sending information associated with the code to the client
			connection.sendall((dct[key]).encode('ascii'))
		else:
			# If key is not present in the database then information is added manually
			value=input('Enter the name')
			dct.update({key:value})
			print('Record Added')
			# Newly added information is sent to client
			connection.sendall(value.encode('ascii'))
			break
finally:
	# Connection is closed
	connection.close()

