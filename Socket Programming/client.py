import socket

host = 'localhost'
port = 12345

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_client_socket.sendto(b'Welcome, home!', (host, port))

data, addr = udp_client_socket.recvfrom(1024)
print('UDP server response:', data.decode())

udp_client_socket.close()
