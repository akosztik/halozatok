#!/usr/bin/python
import datetime
import socket
import select

chipsequences = ['0001', '0010', '0100', '1000']

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 12546))
server_sock.listen(1)
print("Waiting for connection...")
inputs = [server_sock]
clientAddrToChip = {}
sumMessage = ''
messages = []
lastSendedTime = datetime.datetime.now().time()


from datetime import datetime
def time_difference(time_start, time_end):
    start = datetime.strptime(time_start, "%H%M%S")
    end = datetime.strptime(time_end, "%H%M%S")
    difference = end - start
    minutes = difference.total_seconds() / 60
    print('DIFF ' + minutes)
    return int(minutes)

def createNewIntArray(original):
    retval = []
    i = 0
    while i < len(original):
        if original[i] == '-':
            retval.append(-1)
            i += 2
        else:
            retval.append(int(original[i]))
            i += 1
    return retval

def bitAddition(firt, secund):
    result = ''
    i = 0
    tempFirst = createNewIntArray(firt)
    tempSecund = createNewIntArray(secund)

    while i < len(tempFirst):
        tempInt = tempFirst[i] + tempSecund[i]
        result += str(tempInt)
        i += 1
    return result

def broadcast(result, inputs):
    for sock in inputs:
        if sock is not server_sock:
            sock.send(result.encode())

while True:
    readable, writeable, ex = select.select(inputs, inputs, inputs)
    for sock in readable:
        if sock is server_sock:
            client_sock, client_addr = server_sock.accept()
            print(str(client_addr) + ' is connected')
            inputs.append(client_sock)
            data = client_sock.recv(1024).decode()
            if data:
                name = data.split('"')[1]
                if len(chipsequences) != 0:
                    clientAddrToChip[name] = chipsequences.pop()
                    client_sock.send(clientAddrToChip[name].encode())
                else:
                    client_sock.send("NNNN".encode())
                print(str(clientAddrToChip))
        else:
            data = sock.recv(1024).decode()
            if data:
                print(data)
                if data in clientAddrToChip:
                    sock.send(clientAddrToChip[data].encode())
                    print("sended chip for encoding" + clientAddrToChip[data])
                else:
                    sock.send("nincs ilyen nevu cliens".encode())
            data = sock.recv(1024).decode()
            if data:
                print(data)
                messages.append(data)
                print(messages)
                if len(messages) == 2:
                    result = bitAddition(messages.pop(), messages.pop())
                    print('osszegzett: ' + result)
                    broadcast(result, inputs)


# nowTime = datetime.now().time()
# print(nowTime)
    #percek = time_difference(lastSendedTime, nowTime)

    # if 1:
        # print("ellenorzom")


    # from datetime import datetime
    # print(datetime.datetime.now().time())
    # FMT = '%H:%M:%S'
    # tdelta = datetime.strptime(datetime.datetime.now().time(), FMT) - datetime.strptime(lastSendedTime, FMT)
    # if (tdelta > 30):
    #     print("KULLD KI AZ UZENETET")

server_sock.close()



# https://www.youtube.com/watch?v=XJ81CuujwYE
# https://www.youtube.com/watch?v=5plZGFd-cWc

