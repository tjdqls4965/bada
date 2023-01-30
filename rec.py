from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *
import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyautogui as pg

form_class = uic.loadUiType("gg.ui")[0]

class cla(QWidget,form_class):
    client_socket = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pus.clicked.connect(self.puss)
        self.pus.clicked.connect(self.fu)
        self.talk.clicked.connect(self.send_chat)
        self.recent_btn.clicked.connect(self.recent)
        # self.initialize_socket(ip,port)
        # self.initialize_gui()
        # self.listen_thread()
    def recent(self):
        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='cc', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM chat")
        self.ch = self.cursor.fetchall()
        print(self.ch[0][0],self.ch[0][1])
        self.lis.clear()
        # self.lis.addItem(self.ch)
        a=len(self.ch)
        print(a-10)
        # self.lis.addItem(self.ch[a-10][0]+":"+self.ch[a-10][1])
        # self.lis.addItem(self.ch[a-9][0] + ":" + self.ch[a - 9][1])
        for i in range (10,0,-1):
            self.lis.addItem(self.ch[a-i][0]+":"+self.ch[a-i][1])




        self.conn.close()

    def puss(self):
        ip='10.10.21.125'
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

        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='cc', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"INSERT INTO chat values('{self.name}','{self.l1}')")
        self.conn.commit()
        self.conn.close()
        return 'break'
    def listen_thread(self):
        t=Thread(target=self.receive_message,args=(self.client_socket,))
        t.start()

    def receive_message(self,so):
        while True:
            buf = so.recv(256)
            # self.lis.addItem(buf.decode('utf-8'))

            # 게임요청 받는사람
            self.gname=(buf.decode('utf-8')[4:])
            # 게임요청 보내는사람
            self.send_name=(buf.decode('utf-8')[0:3])
            # print(self.gname,"!!!")
            # print(self.send_name, "@@@")
            if self.name in self.gname:
                self.game_message()
                self.lis.addItem(buf.decode('utf-8'))

            else:
                self.lis.addItem(buf.decode('utf-8'))
            # if self.gname == 'Ok요' or self.na
            #     a = pg.alert(text='내용입니다', title='제목입니다', button='OK')

    def game_message(self):
        a = pg.confirm(text='게임할래?', title=f"'{self.send_name}'입니다", buttons=['OK', 'Cancel'])
        print(a)
        if a == 'OK':
            message = (self.name + ":OK요").encode('utf-8')
            self.client_socket.send(message)

        else:
            message = (self.name + ":싫어요").encode('utf-8')
            self.client_socket.send(message)

        # self.l1 = self.liner.text()
        # message = (self.name + ":" + self.l1).encode('utf-8')
        # self.client_socket.send(message)






            # self.lis.addItem(buf.decode('utf-8'))
        # so.close()










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
