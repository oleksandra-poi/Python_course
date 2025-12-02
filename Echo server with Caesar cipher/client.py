import socket

host = 'localhost'
port = 12346

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

key = input("Write integer: ")
text = input("Write text: ")

message = f"{text}|{key}"

udp_client_socket.sendto(message.encode(), (host, port))

data, addr = udp_client_socket.recvfrom(1024)
print('UDP server response:', data.decode())

udp_client_socket.close()
