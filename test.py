import random
import threading
import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType("test.ui")[0]
class tes(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('테스트 하기')
        self.stackedWidget.setCurrentIndex(0)
        self.go_btn.clicked.connect(self.go)
        self.back_btn.clicked.connect(self.back)
        self.table.clear()
        self.main_btn.clicked.connect(self.go_main)
        self.start_btn.clicked.connect(self.star)
        self.stop_btn.clicked.connect(self.sto)
        self.restart_btn.clicked.connect(self.restar)
        self.receive_btn.clicked.connect(self.re)
        self.give_btn.clicked.connect(self.give)
        self.power = True
    def go(self):
        self.stackedWidget.setCurrentIndex(1)
    def back(self):
        self.stackedWidget.setCurrentIndex(0)



    def go_main(self):
        self.parent().setCurrentIndex(0)
    def sto(self):
        self.power = False
    def restar(self):
        self.power = True

    def make_tabel(self):
        self.table.setRowCount(len(self.d))
        self.table.setColumnCount(len(self.d[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.d)):
            for j in range(len(self.d[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.d[i][j])))


    def make_tabel2(self):
        self.table.setRowCount(len(self.bb))
        self.table.setColumnCount(len(self.bb[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.bb)):
            for j in range(len(self.bb[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.bb[i][j])))
    def give(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()

        # self.cursor.execute(f"select * from sell")
        # hg = self.cursor.fetchall()
        #
        # self.cursor.execute(f"insert into sell2 values({hg[0][0]},{hg[0][1]},{hg[0][2]})")
        # conn.commit()

        # self.cursor.execute("update sell set sale=0")
        # conn.commit()

        # self.cursor.execute("update sell set cost=0")
        # conn.commit()
        #
        # self.cursor.execute("update sell set net_sale=0")
        # conn.commit()



        self.cursor.execute("delete from test")
        conn.commit()

        a1=['pic','chechap']
        self.bo=self.combo_menu.currentText()
        if self.bo in a1:
            self.cursor.execute("update sell set cost=cost+5000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+50")
            conn.commit()
            QMessageBox.information(self, '발주', f'{self.bo} 발주완료')

        a2=['beef','chic','shrimp','hashbrown']
        if self.bo in a2:
            self.cursor.execute("update sell set cost=cost+25000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+50")
            conn.commit()

        a3=['hub','pepper','mayo','stake_sauce','tartar_sauce','derry_sauce']
        if self.bo in a3:
            self.cursor.execute("update sell set cost=cost+5000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+500")
            conn.commit()

        a4=['onion','tomato','yang','cheese']
        if self.bo in a4:
            self.cursor.execute("update sell set cost=cost+10000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+50")
            conn.commit()

        a5=['cola','sprite']
        if self.bo in a5:
            self.cursor.execute("update sell set cost=cost+24000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+30")
            conn.commit()

        if self.bo == 'sugar':
            self.cursor.execute("update sell set cost=cost+3000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+1000")
            conn.commit()

        if self.bo == 'egg':
            self.cursor.execute("update sell set cost=cost+15000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+50")
            conn.commit()

        if self.bo == 'potato':
            self.cursor.execute("update sell set cost=cost+10000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+2000")
            conn.commit()

        if self.bo == 'bun':
            self.cursor.execute("update sell set cost=cost+20000")
            conn.commit()

            self.cursor.execute(f"update inven2 set {self.bo}={self.bo}+100")
            conn.commit()
        QMessageBox.information(self, '발주', f'{self.bo} 발주완료')
        self.cursor.execute(f"select * from bom inner join inven2 on menu='{self.bo}'")
        a7 = self.cursor.fetchall()

        self.power = True

        self.table.clear()







    def re(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute("SELECT * FROM inven2")
        self.hk = self.cursor.fetchall()
        self.tablee.setRowCount(len(self.hk))
        self.tablee.setColumnCount(len(self.hk[0]))
        self.tablee.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.hk)):
            for j in range(len(self.hk[0])):
                self.tablee.setItem(i, j, QTableWidgetItem(str(self.hk[i][j])))
    def mask(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute("SELECT * FROM inven2")
        self.hk = self.cursor.fetchall()
        self.tablee.setRowCount(len(self.hk))
        self.tablee.setColumnCount(len(self.hk[0]))
        self.tablee.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.hk)):
            for j in range(len(self.hk[0])):
                self.tablee.setItem(i, j, QTableWidgetItem(str(self.hk[i][j])))

    def fa(self):
        if self.power == False:

            self.table.clear()
            return
    def star(self):
        if self.power == True:
            conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                             db='ham', charset='utf8')
            self.cursor = conn.cursor()

            self.cursor.execute("SELECT menu FROM bom")
            m = self.cursor.fetchall()
            # 메뉴
            mm = []
            for i in range(0, len(m)):
                mm.append(m[i][0])
            print(mm)
            print(len(m))

            # 수량, 메뉴선택
            am = random.randint(1, 5)
            me = random.randint(0, 13)

            self.cursor.execute(f"select * from bom inner join inven2 on menu='{mm[me]}'")
            h = self.cursor.fetchall()



            f = []
            for i in range(0, 22):
                e = h[0][25 + i] - am * (h[0][3 + i])
                f.append(e)

            self.cursor.execute("select * from el")
            element = self.cursor.fetchall()

            nn=[]
            self.cursor.execute("select * from inven2")
            self.bb = self.cursor.fetchall()
            for i in range(0,22):
                nn.append(self.bb[0][i])
                if nn[i]<6:
                    print("재고소진")
                    self.power=False
                    self.fa()
                    self.go()
                    return


            print("1")
            for i in range(0,len(element)):
                if f[i]<0:
                    f[i]=0
                self.cursor.execute(f"update inven2 set {element[i][0]}={f[i]} where {element[i][0]} >0 ")
                conn.commit()

            self.cursor.execute(f"insert into test values('테스트','{mm[me]}','{am}')")
            conn.commit()

            self.cursor.execute("select menu_price from bom")
            self.ho = self.cursor.fetchall()

            self.cursor.execute(f"update sell set sale=sale+({self.ho[me][0]}*{am})")
            conn.commit()

            # self.cursor.execute(f"update sell set cost=50000")
            # conn.commit()
            #
            # self.cursor.execute(f"select * from sell")
            # gg = self.cursor.fetchall()
            # gom=gg[0][0]-gg[0][1]
            #
            # self.cursor.execute(f"insert into sell (net_sale) values({gom})")
            # conn.commit()






            self.cursor.execute("select * from test")
            self.d = self.cursor.fetchall()
            self.make_tabel()
        threading.Timer(4, self.star).start()














if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = tes()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


