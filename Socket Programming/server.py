import socket

host = 'localhost'
port = 12345

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((host, port))
print('UDP-server is loading...')

while True:
   data, addr = udp_server_socket.recvfrom(1024)
   print('Recieve from', addr, 'message:', data.decode())

   udp_server_socket.sendto(b'Hello from UPD-server!', addr)
