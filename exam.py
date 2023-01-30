from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *
import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("gg.ui")[0]

class cla(QWidget,form_class):
    client_socket = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pus.clicked.connect(self.puss)
        self.pus.clicked.connect(self.fu)
        self.talk.clicked.connect(self.send_chat)
        # self.initialize_socket(ip,port)
        # self.initialize_gui()
        # self.listen_thread()
    def puss(self):
        ip='192.168.219.106'
        port = 80

        self.initialize_socket(ip,port)
        # self.lis.addItem(self.li)
        self.listen_thread()

    def initialize_socket(self, ip, port):
        self.client_socket = socket(AF_INET,SOCK_STREAM)
        remote_ip = ip
        remote_port = port
        self.client_socket.connect((remote_ip,remote_port))
    def fu(self):
        self.l2=self.liner2.text()
        self.name = self.l2
        start_name=(self.name+"님이 입장하셨습니다").encode('utf-8')
        self.client_socket.send(start_name)



    def send_chat(self):
        # senders_name = self.name_widget.get().strip()+":"
        # data = self.enter_text_widtet.get(1.0,'end').strip()
        # message = (senders_name+data).encode('utf-8')

        self.l1 = self.liner.text()
        message = (self.name+":"+self.l1).encode('utf-8')
        self.client_socket.send(message)

        return 'break'
    def listen_thread(self):
        t=Thread(target=self.receive_message,args=(self.client_socket))
        t.start

    def receive_message(self,so):
        while True:
            buf = so.recv(256)
            print(buf)
            # if not buf:
            #     break
            # self.chat_transcript_area.insert('end',buf.decode('utf-8')+'\n')


            self.lis.addItem(buf.decode('utf-8'))
        so.close()










if __name__=="__main__":

    # form_class = uic.loadUiType("title.ui")[0]
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)


    myWidget = cla()
    # 프로그램 화면을 보여주는 코드
    myWidget.show()
    # cla(ip,port)

    # myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
