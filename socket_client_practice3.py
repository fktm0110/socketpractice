import socket

host = '203.250.133.88' #putty용 호스트
#host = '127.0.0.1' #파이참용 호스트
port = 10110
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}".format(server_address[0], server_address[1]))
sock.connect(server_address)

message = input("Eenter filename : ")
message = bytes(message, encoding = 'utf-8')


try :
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    data = data.decode()

    if len(data) > 1:
        print("Received from server : \n{}".format(data))
        accessMode = 'w'
        filename = message
        myFile = open(filename, accessMode)
        myFile.write(data)
        print("파일이 정상적으로 클라이언트 로컬 드라이브에 저장되었습니다.")
    else:
        print("서버에서 파일명을 찾을 수 없습니다.")

except Exception as e:
     print("Exception : {}".format(str(e)))

sock.close()