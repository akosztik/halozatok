import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',12546))
chip = 'NNNN'
name=sys.argv[1]
str1 = 'I AM "' + name + '" .MY SEQ?'
client_sock.send(str1.encode())
data = client_sock.recv(1024).decode()
print(data)
if data == 'NNNN':
    print("több kapcsolatot nem tudott fogadni a server! \n")
    client_sock.close()
else:
    print("chipet kaptam: " + str(data))
    chip = str(data)

def cdmaEncoding(chipfogado, uzenet):
    codedMessage = ''
    i = 0
    while i<len(uzenet):
        if uzenet[i] == '0':
            transformed = int('-1')
            codedMessage += str(transformed*int(chipfogado))

        else:
            transformed = int('1')
            codedMessage += str(transformed * int(chipfogado))
        i += 1
    return codedMessage


print("Add meg a cél clienst és az üzenetet! \n")
data = input()
fogado = data.split(' ')[0]
uzenet = data.split(' ')[1]
client_sock.send(fogado.encode())
data = client_sock.recv(1024).decode()
print(data)
if data != 'nincs ilyen nevu cliens':
    chipfogado = int(data)
    print(chipfogado)
else:
    print('nincs ilyen nevu cliens')

encodoltUzenet = cdmaEncoding(chipfogado, uzenet)
print(encodoltUzenet)
'''
client_sock.send(encodoltUzenet)
data = client_sock.recv(1024)
print(data)
'''

client_sock.close()
