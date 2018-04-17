import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 12546))
chip = 'NNNN'
name = sys.argv[1]
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


def XOR(bit, chipfogado):
    result = ''
    i = 0
    while i < len(chipfogado):
        result += str(int(chipfogado[i]) * int(bit))
        i += 1
    return result


def cdmaEncoding(chipfogado, uzenet):
    codedMessage = ''
    i = 0
    while i < len(uzenet):
        if uzenet[i] == '0':
            codedMessage += XOR('-1', chipfogado)
        else:
            codedMessage += XOR('1', chipfogado)
        i += 1
    return codedMessage


def cdmaDencoding(chip, uzenet):
    codedMessage = ''
    i = 0
    return codedMessage


print("Add meg a cél clienst és az üzenetet( Az üzenet max 8 bit lehet! )! \n")
data = input()

message = data.split(' ')
client_sock.send(message[0].encode())
data = client_sock.recv(1024).decode()

if data != 'nincs ilyen nevu cliens':
    encodoltUzenet = cdmaEncoding(data, message[1])
    print(encodoltUzenet)
    client_sock.send(encodoltUzenet.encode())
else:
    print('nincs ilyen nevu cliens')


data = client_sock.recv(1024).decode()
print("received SUMMED message: " + str(data))

'''
client_sock.close()
'''