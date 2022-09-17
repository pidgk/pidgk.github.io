
import socket
host = "192.168.8.1"
for port in range(1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    value = sock.connect_ex( (host, port) )
    if value == 0:
        print("Puerto Abierto", port)
    else:
        pass
