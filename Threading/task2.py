import socket
import threading

host = 'localhost'
port = 12345

def handle_client(client_socket, addr):
    print("Connection with:", addr)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        print(f"Received from {addr}: {data.decode()}")
        client_socket.send(data) 

    client_socket.close()
    print(f"Connection closed: {addr}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Server running on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, addr))
    client_thread.start()
