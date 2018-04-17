#!/usr/bin/python

import socket
import select
import re

codebook = {'FLAG': '01111110', 'A': '10000001', 'B': '00001110', 'C': '10110011', 'D': '11100110', 'ESC': '01110000'}

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('localhost',12546))
server_sock.listen(1)

inputs = [server_sock]


def removeBits(tipus):
    str1 = ''
    i = 0
    counter = 0
    while (i < len(tipus)):
        if (counter == 5 and tipus[i]=='0'):
            counter = 0
        else:
            if (tipus[i] == '1'):
                counter += 1
            else:
                counter = 0
            str1 = str1 + tipus[i]
        i += 1
    return str1


def removeFrame(binary):
    count = len(binary)
    binary = binary[8:]
    print(binary)
    count = len(binary)
    binary = binary[:count-8]
    return binary


def removeEsc(word):
    word = word.replace("ESCESC", "ESC")
    word = word.replace("ESCFLAG", "FLAG")
    return word


def byteConversion(binary):
    splittedBinary = re.findall('........', binary)
    word = ""
    for bin in splittedBinary:
        for key in codebook:
            if codebook[key] == bin:
                # print(key)
                word += key
    return word


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
            data = str(data)
            data = data.replace("b", "", 1)
            data = data.replace("'", "")
            if data:
                print(data)
                tipus = data.split(':')
                print(tipus)
                binary = tipus[1]
                type = tipus[0]
                print("binaris tipusa: " + type)
                print("binaris: " + binary)
                binary = removeFrame(binary)
                if (type=='bit'):
                    binary=removeBits(binary)
                    print("bitkonverzio utan: " + binary)
                word = byteConversion(binary)
                if (type=='byte'):
                    word = removeEsc(word)
                print("cliens altal kuldott szo: " +word)
            else:
                sock.close()
                inputs.remove(sock)
server_sock.close()
#http://szabilinux.hu/konya/konyv/4fejezet/4fadpro1.htm
