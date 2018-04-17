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


def createNewIntArray(original):
    retval = []
    i = 0
    while i < len(original):
        if original[i] == '-':
            print(int(original[i + 1]) * (-1))
            retval.append(int(original[i + 1]) * (-1))
            i += 2
        else:
            retval.append(int(original[i]))
            i += 1
    return retval


def cdmaDencoding(chip, codedMessage):
    print('XXXXXX ' + codedMessage)
    retval = createNewIntArray(codedMessage)
    print(retval)
    print('YYYY ' + str(retval))
    encodedMessage = ''
    i = 0
    while i < len(retval):
        sum = 0
        for chipsplit in chip:
            print(chipsplit)
            sum += int(chipsplit) * retval[i]
            i += 1

        if (sum == 1):
            encodedMessage += '1'
        if (sum == 0):
            encodedMessage += 'N'
        if (sum == -1):
            encodedMessage += '0'
        print('>>>>>> ' + encodedMessage)
    return encodedMessage


def checkDataLenght():
    data = 'C 123456789'
    while len(data) > 10:
        data = input()
        if len(data) > 10:
            print("Az üzenetet( Az üzenet max 8 bit lehet! )! \n")
    return data


print("Add meg a cél clienst és az üzenetet( Az üzenet max 8 bit lehet! )! \n")

data = checkDataLenght()

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
decodedMessage = cdmaDencoding(chip, data)
print("decoded message: " + decodedMessage)
'''
client_sock.close()
'''
