#!/usr/bin/python

import socket
import select

keszlet = {'kocka': 10, 'kerék': 20, 'hangszóró': 5, 'elem': 30, 'kijelző': 20}

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
                kosar={}
                szam = data.count(':')
                lista = data.split(',')
                i=0
                van=True

                while i < szam:
                    tmp = lista[i].split(':')[0]
                    item = tmp.replace('"', '').replace('{', '').replace(' ', '')
                    temp = lista[i].split(':')[1].replace('"', '').replace('}', '').replace(' ', '')
                    mennyiseg = int(temp)
                    kosar[item] = mennyiseg
                    if keszlet[item] < mennyiseg:
                        van = False
                    i += 1
                if van:
                    for key in kosar:
                        tmpMennyiseg = keszlet[key]-kosar[key]
                        if tmpMennyiseg >= 0:
                            keszlet[key]=tmpMennyiseg
                        else:
                            print("Hiba készletezéskor")
                            van = False
                    if van:
                        sock.send('OK'.encode())
                        print("vasarlas történt: " + str(kosar))
                else:
                    sock.send('NEM OKE'.encode())
                print("megmaradt készlet: " + str(keszlet))
            else:
                sock.close()
                inputs.remove(sock)
server_sock.close()

'''
https://wiki.python.org/moin/UdpCommunication
'''