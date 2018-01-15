import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
code=420
try:
    sock.connect(('192.168.223.52',12345))
    sock.send(str(code).encode("ascii"))
    print(sock.recv(1024).decode('ascii'))
finally:
    sock.close()
