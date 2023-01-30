import socket
import time
import tcping

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

svrIP = input(("Server IP(default: 10.10.21.125): "))
if svrIP =='':
    svrIP = '10.10.21.125'

port = input('port(default:80):')
if port == '':
    port = 80
else:
    port = int(port)
sock.connect((svrIP,port))
print('Connected to'+svrIP)

while True:
    msg = input("Sending message: ")

    if not msg:
        continue
    try:
        sock.send(msg.encode())
    except:
        print("연결이 종료되었습니다")
        break
    try:
        msg = sock.recv(1024)
        if not msg:
            print("연결이 종료되었습니다")
            break
        print(f'Received message: {msg.decode()}')
    except:
        print("연결이종료")
        break
sock.close()


