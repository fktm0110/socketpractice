#!/usr/bin/python3
import socket

host = ''
port = 10110
BUFF_SIZE = 1024
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("waiting for request...")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)
    accesMode = "r"
    try:
        if message:
            print("received message : {} \n".format(message.decode()))
            myFile = open(message, accesMode)
            dataFromFile = myFile.read()
            print(dataFromFile)
            data_sock.sendall(dataFromFile.encode())
            myFile.close()

    except FileNotFoundError:
        print("파일명을 찾을 수 없습니다.")

    data_sock.close()
