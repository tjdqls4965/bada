import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("inquire.ui")[0]
class inq(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('문의하기')
        self.main_btn.clicked.connect(self.go_main)
        self.qu_btn.clicked.connect(self.qu)
        self.search_btn.clicked.connect(self.search)


    def con(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')

        self.cursor = conn.cursor()



    def go_main(self):
        self.parent().setCurrentIndex(0)
    def qu(self):
        self.line=self.liner.text()
        self.men = self.combo_menu.currentText()
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.no=[]
        self.cursor.execute(f"select * from orders where 이름='{self.b}'")
        self.ord = self.cursor.fetchall()
        if len(self.ord)==0:
            print("11111^^")
            self.cursor.execute(f"insert into inquire(이름, 메뉴, 문의) values('{self.b}','{self.men}','{self.line}')")
            conn.commit()

        else:
            print("222222^^")
            for i in range(0,len(self.ord)):
                self.no.append(self.ord[i][1])

            if self.men in self.no:
                self.cursor.execute(f"insert into inquire(이름, 메뉴, 문의,주문상품) values('{self.b}','{self.men}','{self.line}','{self.men}')")
                conn.commit()
            else:
                self.cursor.execute(f"insert into inquire(이름, 메뉴, 문의) values('{self.b}','{self.men}','{self.line}')")
                conn.commit()
                conn.close()

        QMessageBox.information(self, '문의 완료', '문의 완료')
    def search(self):
        conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                         db='ham', charset='utf8')
        self.cursor = conn.cursor()
        self.cursor.execute(f"select * from inquire where 이름='{self.b}'")
        self.d=self.cursor.fetchall()
        self.make_tabel()








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
    myWindow = inq()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
