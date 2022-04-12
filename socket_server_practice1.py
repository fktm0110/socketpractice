#!/usr/bin/python3
import socket

host = ''
port = 10110
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)
sock.bind(server_address)

#while True:
print("waiting for request...")
message, client_address = sock.recvfrom(BUFF_SIZE)


try:
    message = int(message.decode())
    print("echo request from {} port {}".format(client_address[0], client_address[1]))
    if message == 0:
        print("{}은(는) 0입니다.".format(message))
    elif message % 2 == 0:
        print("{}은(는) 짝수입니다.".format(message))
    else:
        print("{}은(는) 홀수입니다.".format(message))

    sock.sendto("숫자입니다. 서버를 확인해주세요.".encode(), client_address)

except ValueError:
    print("숫자가 아닙니다.")
    sock.sendto("숫자를 입력해주세요 서버를 확인해주세요.".encode(),client_address)


sock.close()
