import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime

form_class = uic.loadUiType("menu.ui")[0]
class orde(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('주문하기')
        self.table.clear()
        self.main_btn.clicked.connect(self.go_main)
        self.menu_btn.clicked.connect(self.showw)
        self.call_btn.clicked.connect(self.ord)
        self.search_btn.clicked.connect(self.search)
        self.cal_btn.clicked.connect(self.cal)
        self.cancel_btn.clicked.connect(self.cancel)




    def go_main(self):
        self.parent().setCurrentIndex(0)
    # 메뉴판
    def showw(self):
        self.table.clear()
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ham', charset='utf8')


        self.cursor = conn.cursor()
        self.cursor.execute(f'SELECT menu,menu_price FROM bom')
        self.d = self.cursor.fetchall()
        self.make_tabel()
        # conn.close()
    # 주문하기
    def ord(self):

        self.table.clear()
        self.men=self.combo_menu.currentText()
        self.am = self.combo_amount.currentText()

        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute(f"insert into ham.orders (이름,주문상품,수량,주문상태,확인) values ('{self.a}','{self.men}','{self.am}','정산안함','5')")
        print("1")
        self.cursor.execute(f"select * from ham.orders where 이름='{self.a}'")
        self.e = self.cursor.fetchall()


        #
        self.table.setRowCount(len(self.e))
        self.table.setColumnCount(len(self.e[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.e)):
            for j in range(len(self.e[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.e[i][j])))

        conn.commit()
        conn.close()
        return self.e
    # 주문 취소하기
    def cancel(self):
        self.table.clear()
        if self.a == '박성빈':
            QMessageBox.warning(self, '선택상품', '주문목록에 없음')
        else:


            self.men = self.combo_menu.currentText()
            self.am = self.combo_amount.currentText()
            self.no=[]

            conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                             db='ham', charset='utf8')
            self.cursor = conn.cursor()
            # self.cursor.execute(
            #     f"insert into ham.orders (이름,주문상품,수량,주문상태) values ('{self.a}','{self.men}','{self.am}','정산안함')")
            # print("1")
            self.cursor.execute(f"select * from orders where 이름='{self.a}'")
            self.e = self.cursor.fetchall()
            for i in range(0, len(self.e)):
                self.no.append(self.e[i][1])

            if self.men in self.no:
                self.cursor.execute(f"delete from orders where 주문상품='{self.men}'")
                conn.commit()
                QMessageBox.information(self, '취소완료', f'{self.men}')
            else:
                QMessageBox.warning(self, '선택상품', '주문목록에 없음')

            #
            self.table.setRowCount(len(self.e))
            self.table.setColumnCount(len(self.e[0]))
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            for i in range(len(self.e)):
                for j in range(len(self.e[0])):
                    self.table.setItem(i, j, QTableWidgetItem(str(self.e[i][j])))

            conn.commit()
            conn.close()




    # 메뉴 조회
    def search(self):
        self.table.clear()
        if self.a == '박성빈':
            conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                             db='ham', charset='utf8')
            self.cursor = conn.cursor()
            self.cursor.execute("select * from ham.orders")
            self.su = self.cursor.fetchall()
            if len(self.su) == 0:
                QMessageBox.warning(self, '목록없음', '목록에 없음')
            else:
                self.table.setRowCount(len(self.su))
                self.table.setColumnCount(len(self.su[0]))
                self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
                for i in range(len(self.su)):
                    for j in range(len(self.su[0])):
                        self.table.setItem(i, j, QTableWidgetItem(str(self.su[i][j])))


        else:
            conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                             db='ham', charset='utf8')
            self.cursor = conn.cursor()
            self.cursor.execute(f"select * from ham.orders where 이름='{self.a}'")
            self.e = self.cursor.fetchall()
            if len(self.e) == 0:
                QMessageBox.warning(self, '선택상품', '주문목록에 없음')
            else:
                self.table.setRowCount(len(self.e))
                self.table.setColumnCount(len(self.e[0]))
                self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
                for i in range(len(self.e)):
                    for j in range(len(self.e[0])):
                        self.table.setItem(i, j, QTableWidgetItem(str(self.e[i][j])))
    # 주문 정산하기
    def cal(self):
        self.table.clear()
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()

        self.cursor.execute(f"update orders set 주문상태 = '정산완료' where 이름 = '{self.a}'")
        conn.commit()

        self.cursor.execute(f"SELECT 주문상품,수량 FROM orders where 이름 = '{self.a}' and 주문상태 = '정산완료'")
        self.e = self.cursor.fetchall()
        # 00은 메뉴 01은 수량
        for i in range(0,len(self.e)):
            self.cursor.execute(f"update bom set sell_number=sell_number+{self.e[i][1]} where menu='{self.e[i][0]}'")
        conn.commit()

        self.cursor.execute(f"delete from orders where 주문상태='정산완료'")
        conn.commit()
        conn.close()
        QMessageBox.information(self,'정산완료','정산완료')
        self.table.clear()

    def make_tabel(self):
        self.table.setRowCount(len(self.d))
        self.table.setColumnCount(len(self.d[0]))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.d)):
            for j in range(len(self.d[0])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.d[i][j])))





if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = orde()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
