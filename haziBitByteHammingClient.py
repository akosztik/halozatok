import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',12546))
codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

type=sys.argv[1]

def byteConversion(splitted):
    str1 = type + ':' + codebook['FLAG']
    i = 0
    while (i < len(splitted)):
        if ((splitted[i] == 'FLAG' or splitted[i] == 'ESC') and type == 'byte'):
            str1 += codebook['ESC']
        str1 += codebook[splitted[i]]
        i += 1
    str1 += codebook['FLAG']
    return str1

splitted=sys.argv[2].split(',')
str1 = byteConversion(splitted)

def bitConversion(bitSplit):
    str1 = ''
    i = 0
    counter = 0
    while (i < len(bitSplit)):
        str1= str1 + bitSplit[i]
        if ( bitSplit[i] == '1'):
            counter+=1
        if (counter == 5):
            str1 = str1 + '0'
            counter = 0
    return str1

if ( type=='bit'):
    bitSplit = str1.split('')
    str1 = bitConversion(str1)

print(str1)

client_sock.send(str1.encode())
print("SENDED")
client_sock.close()
