import socket

host = '203.250.133.88' #putty용 호스트
#host = '127.0.0.1' #파이참용 호스트
port = 10111
BUFF_SIZE =128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)
try :
    message = input("Enter message : ")
    bytes_sent = sock.sendto(message.encode(), server_address)

    data, address = sock.recvfrom(BUFF_SIZE)
    print("Received from server : {} ".format((data.decode())))

except Exception as e:
        print("Exception : {}".format(str(e)))

sock.close()