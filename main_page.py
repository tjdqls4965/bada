import sys
import pymysql as p
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv
from PyQt5 import QtWidgets
import pyautogui
import threading
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import pandas as pd

# 1페이지
from orderr import orde
from loginn import log
from inqu import inq
# 2페이지/·/////////
# from cancel import stop

form_class = uic.loadUiType("total2.ui")[0]

class main_page(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gom=0
        self.ck=0
        # self.hi=self.hi.text()
        # 로그인 파일명 ddd/ 로그인 버튼명 로그인액션/ 메서드연결
        loginn.login_action.clicked.connect(self.confirm)
        self.login_section.clicked.connect(self.login_page)
        self.order_section.clicked.connect(self.order_page)
        self.inquire_section.clicked.connect(self.inquire_page)
        self.graph_btn.clicked.connect(self.stick)
        font_path = "c:\windows\Fonts\gulim.ttc"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)
        # orderr.call_btn.clicked.connect(self.call)
        # self.call()

    def stick(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute("SELECT * FROM sell2")
        ma = self.cursor.fetchall()
        k = len(ma)
        # 원래수치,
        print(ma[k - 1], ma[k - 2], ma[k - 3])


        area = ['금일','전날','이틀전']
        # 비율을 담는 리스트
        percent=[ma[k-1][0],ma[k-2][0],ma[k-3][0]]
        percent_two=[ma[k-1][1],ma[k-2][1],ma[k-3][1]]
        percent_three=[ma[k-1][2],ma[k-2][2],ma[k-3][2]]

        plt.rc('font', size=6)
        plt.figure(figsize=(15, 12))
        conv_list1 = list(percent)
        conv_list2 = list(percent_two)
        conv_list3 = list(percent_three)
        # 1개바의 너비
        bar_width = 0.2
        # 도시의 수 18개
        index = np.arange(3)

        # 판다에 있는 기능 활용, '초등학생비율, 혼인율, 1인가구' 는 우측상단에 뜨게 됨 , index=area는 지역으로 x축
        df = pd.DataFrame({'매출': conv_list1, '비용': conv_list2, '순이익': conv_list3}, index=area)
        # 바사이의 간격을 설정함
        b1 = plt.bar(index, df['매출'], bar_width, alpha=0.4, color='b', label='매출')
        b2 = plt.bar(index + bar_width, df['비용'], bar_width, alpha=0.4, color='g', label='비용')
        b3 = plt.bar(index + 2 * bar_width, df['순이익'] / 4, bar_width, alpha=0.4, color='r', label='순이익')

        plt.xticks(np.arange(bar_width, len(area) + bar_width, 1), area)
        # x축과 y축에 나타나는 비율
        plt.xlabel('날짜', size=10)
        plt.ylabel('누적매출', size=10)
        plt.legend()
        plt.show()

        plt.show()


    def inquire_page(self):
        if self.ck == 1:
            widget.setCurrentIndex(3)
        elif self.ck == 0:
            widget.setCurrentIndex(0)
    def order_page(self):
        if self.ck == 1:
            widget.setCurrentIndex(2)
            conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                             db='ham', charset='utf8')
            self.cursor = conn.cursor()
            self.cursor.execute(f"update orders set 확인='0'")
            conn.commit()

        elif self.ck == 0:
            widget.setCurrentIndex(0)

    def login_page(self):
        if not self.gom:
            # 로그인페이지
            widget.setCurrentIndex(1)
        else:
            self.id = 0
            self.ck = 0
            self.lb_name.setText("")
            self.login_section.setText('로그인')
            widget.setCurrentIndex(1)



    def confirm(self):
        self.gom = loginn.login()
        # login.clear_id()
        if self.gom !=None:
            # print(self.hi,"hihihihihihih")
            self.lb_name.setText(f"{self.gom}님 안녕하세요.")
            self.login_section.setText('로그아웃')

            self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                                  db='ham', charset='utf8')
            self.cursor = self.conn.cursor()
            self.cursor.execute(f'SELECT * FROM log WHERE ID="{self.gom}"')
            self.gom_list = self.cursor.fetchall()
            # print(self.gom_list)
            # print(self.gom_list[0][3])
            self.lb_name.setText(f"{self.gom_list[0][2]}님 안녕하세요.")
            self.ck=1
            orderr.a=self.gom_list[0][2]
            inqu.b = self.gom_list[0][2]
            # live.m=self.gom_list[0][3]
            # send.k=self.gom_list[0][3]
            # chat.r=self.gom_list[0][3]
            # subsend.sb=self.gom_list[0][3]
            # self.pushButton_4.setText('로그아웃')
        self.parent().setCurrentIndex(0)
        self.call()
        # conn = p.connect(host='localhost', port=3306, user='root', password='1234',
        #                  db='ham', charset='utf8')
        # self.cursor = conn.cursor()
        # self.cursor.execute(f"select * from orders ")
        # self.f = self.cursor.fetchall()
        # if self.gom_list[0][2] == '박성빈' and len(self.f) == len(self.f) + 1:
        #     pyautogui.alert('주문이 들어왔어요')
        #
        # threading.Timer(2, self.confirm).start()

    def call(self):

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute(f"select * from orders where 확인='5'")
        # f = self.cursor.fetchall()
        self.f = self.cursor.fetchall()

        if self.gom_list[0][2] == '박성빈' and len(self.f)!=0:
            pyautogui.alert('주문이 들어왔어요')
        else:
            print("1")
            pass
        threading.Timer(10, self.call).start()



if __name__ == "__main__":
    # form_class = uic.loadUiType("title.ui")[0]
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    # WindowClass의 인스턴스 생성
    loginn = log()
    orderr=orde()
    inqu=inq()

    myWindow = main_page()
    # 프로그램 화면을 보여주는 코드
    widget.addWidget(myWindow)
    # 로그인 페이지 파이썬 이름 ddd
    widget.addWidget(loginn)
    widget.addWidget(orderr)
    widget.addWidget(inqu)

    # widget.addWidget(cancel)
    widget.setFixedHeight(900)
    widget.setFixedWidth(1200)
    widget.show()
    # myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()