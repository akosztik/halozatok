import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',12546))
codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

type=sys.argv[1]
str1=type + ':' + codebook['FLAG']
print(str1)
print("---------------")
print(sys.argv)
print("---------------")
splitted=sys.argv[2].split(',')
i=0
while (i < len(splitted)):
	print(splitted[i])
	if ( splitted[i]=='FLAG' and type=='byte'):
		str1+=codebook['ESC']
	str1+=codebook[splitted[i]]
	i+=1
str1+=codebook['FLAG']
print(str1)
client_sock.send(str1.encode())
print("SENDED")
client_sock.close()
