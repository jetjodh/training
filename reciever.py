import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.43.3',9989))
sock.sendall(b'bye')
print(sock.recv(256))
sock.close()
