import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 12346))

print("Add meg a szükséges elemek listáját! \n")
data = input()
print(data)
client_sock.send(str(data).encode())
data = client_sock.recv(1024).decode()
print(data)

client_sock.close()