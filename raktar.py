#!/usr/bin/python

import socket
import select
codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('localhost',12546))
server_sock.listen(1)

inputs = [server_sock]
while True:
    readable,writeable,ex = select.select(inputs,inputs,inputs)
    for sock in readable:
        if sock is server_sock:
            client_sock, client_addr = server_sock.accept()
            print("kapcsolat erkezett: ")
            print(client_addr)
            inputs.append(client_sock)
        else:
            data = sock.recv(1024)
            if data:
                print(data)
                tipus = data.split(':')[0]
                binaris = int(data.split(':')[1])
                print("binaris tipusa: " + tipus)
                print("binaris: " + binaris)
                print(codebook)
            else:
                sock.close()
                inputs.remove(sock)
server_sock.close()
