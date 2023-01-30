from socket import *
from threading import *
import pymysql as p

class ser:
    def __init__(self):
        self.clients=[]
        self.final_received_message = ""
        self.s_sock = socket(AF_INET,SOCK_STREAM)
        self.ip = ''
        self.port= 80
        self.s_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s_sock.bind((self.ip,self.port))
        print("클라이언트 대기중...")
        self.s_sock.listen(100)
        self.accept_client()
    def accept_client(self):
        while True:
            client = c_socket, (ip,port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client)
            print(ip,":",str(port),'가 연결되었습니다')
            cth = Thread(target=self.receive_messages,args=(c_socket,))
            cth.start()
    def receive_messages(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(256)
                if not incoming_message:
                    break
            except:
                continue
            else:
                self.final_received_message=incoming_message.decode('utf-8')
                print(self.final_received_message,"!!!")
                self.send_all_clients(c_socket)
                socket.sendall(self.final_received_message.encode())
                # self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                #                       db='cc', charset='utf8')
                # self.cursor = self.conn.cursor()
                # self.cursor.execute(f"INSERT INTO chat values(f'{self.final_received_message}')")
                # self.conn.commit()
                # self.conn.close()


        c_socket.close()
    def send_all_clients(self, senders_socket):

        for client in self.clients:
            socket, (ip, port) = client

            # try:

            # print(self.final_received_message.encode(),"@@#@#@")
            # except:
            #     self.clients.remove(client)
            #     print("{},{}연결이 종료되었습니다".format(ip,port))

if __name__=="__main__":
    ser()

