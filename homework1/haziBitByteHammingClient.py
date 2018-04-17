import socket
import sys

def byteConversion(splitted):
    str1=''
    i = 0
    while (i < len(splitted)):
        if ((splitted[i] == 'FLAG' or splitted[i] == 'ESC') and type == 'byte'):
            str1 += codebook['ESC']
        str1 += codebook[splitted[i]]
        i += 1
    return str1

def bitConversion(bitSplit):
    bitsor = ''
    i = 0
    counter = 0
    length = len(bitSplit)
    print(length)
    while (i < length):
        bitsor += bitSplit[i]
        if ( bitSplit[i] ==  '1'):
            counter += 1
            if (counter == 5):
                bitsor += '0'
                counter = 0
        else:
            counter = 0
        i += 1
    print('beszuras utan: ' + str(len(bitsor)))
    return bitsor

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',12546))
codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

type=sys.argv[1]
splitted1 = sys.argv[2].split(',')
print('splitted1: '+ str(splitted1))
str1 = byteConversion(splitted1)

if ( type=='bit'):
    bites = bitConversion(str1)
    print('convertedBits: ' + str(bites))
    str1=bites

str2 = type + ':' + codebook['FLAG'] + str1 + codebook['FLAG']
print(str2)

client_sock.send(str2.encode())
print("SENDED")
client_sock.close()
