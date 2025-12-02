import socket

def caesar_encrypt(text, key):
    encrypted_text = ""
    for symbol in text:
        if symbol.isalpha():
            code = ord(symbol)
            if symbol.isupper():
                code = (code - ord('A') + key) % 26 + ord('A')
            else:
                code = (code - ord('a') + key) % 26 + ord('a')
            encrypted_text += chr(code)
        else:
            encrypted_text += symbol
    return encrypted_text


host = 'localhost'
port = 12346

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((host, port))

print("UDP server running...")

while True:
    data, addr = udp_server_socket.recvfrom(1024)
    received = data.decode()
    text, key_string = received.split("|")
    key = int(key_string)

    print("Текст:", text)
    print("Ключ:", key)

    encrypted = caesar_encrypt(text, key)
    udp_server_socket.sendto(encrypted.encode(), addr)
