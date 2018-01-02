import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(('192.168.1.10',12345))
    sock.sendall(('bye').encode('ascii'))
    print(sock.recv(256).decode('ascii'))
finally:
    sock.close()
