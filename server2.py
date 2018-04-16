#!/usr/bin/python

import socket
import select
import re

chipsequences = ['0001', '0010', '0100', '1000']

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('localhost',12546))
server_sock.listen(1)
print("Waiting for connection...")
inputs = [server_sock]
clientAddrToChip = {}
sumMeassages = ''



while True:
    readable,writeable,ex = select.select(inputs,inputs,inputs)
    for sock in readable:
        if sock is server_sock:
            client_sock, client_addr = server_sock.accept()
            print( str(client_addr) + ' is connecting')
            inputs.append(client_sock)

        else:
            data = sock.recv(1024).decode()
            if data:
                print(data)
                name = data.split('"')[1]
                print(name)
                if len(chipsequences) != 0:
                    clientAddrToChip[name] = chipsequences.pop()
                    sock.send(clientAddrToChip[name].encode())
                else:
                    sock.send("NNNN".encode())
                print(str(clientAddrToChip))
            data = sock.recv(1024).decode()
            if data:
                print(data)
                if data in clientAddrToChip:
                    print(clientAddrToChip[data])
                    sock.send(clientAddrToChip[data].encode())
                    print("sended")
                else:
                    sock.send("nincs ilyen nevu cliens".encode())
            data = sock.recv(1024).decode()
            if data:
                print(data)

            else:
                sock.close()
                inputs.remove(sock)
server_sock.close()
#https://www.youtube.com/watch?v=XJ81CuujwYE
#https://www.youtube.com/watch?v=5plZGFd-cWc