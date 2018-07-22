#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'  # or 'localhosr'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSOCK = socket(AF_INET, SOCK_STREAM)
tcpCliSOCK.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSOCK.send(data.encode())
    data = tcpCliSOCK.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSOCK.close()