#!/usr/bin/python

import socket
import select

keszlet = {'kocka':10,'kerék':20,'hangszóró':5, 'elem':30, 'kijelző':20}

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 12346))
server_sock.listen(1)
print("Waiting for connection...")
inputs = [server_sock]

while True:
    readable,writeable,ex = select.select(inputs,inputs,inputs)
    for sock in readable:
        if sock is server_sock:
            client_sock, client_addr = server_sock.accept()
            print(client_addr)
            inputs.append(client_sock)
        else:
            data = sock.recv(1024).decode()
            if data:
                print(data)
                szam = data.count(':')
                lista = data.split(',')
                i=0
                van=True
                while(i<=szam):
                    item = lista[i].split(':')[0]
                    mennyiseg = int(lista[i].split(':')[1])
                    if (keszlet[item] < mennyiseg):
                        van=False

                if (van):
                    sock.send('OK'.encode())
                else:
                    sock.send('NEM OKE'.encode())
                print(keszlet)
            else:
                sock.close()
                inputs.remove(sock)
server_sock.close()