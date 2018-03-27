import socket
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',12546))
codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

while True:
    str1= codebook['FLAG']
    i=2
    while i <len(sys.argv):
        print(sys.argv[i])
        str1+=codebook[sys.argv[i]]
        i+=1
    str1+=codebook['ESC']    
    print(str1)
    client_sock.send(str1)
    print(str1)
    data = client_sock.recv(1024)
    print(data)
    print(data)
client_sock.close()
