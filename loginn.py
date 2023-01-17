import pymysql as p
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("login.ui")[0]
class log(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(1)
        self.setWindowTitle('로그인하기')
        self.join_btn.clicked.connect(self.join)
        self.move_login.clicked.connect(self.login_stack)
        self.join_page.clicked.connect(self.join_stack)
        self.login_action.clicked.connect(self.login)
        self.main_btn.clicked.connect(self.go_main)
        self.member = False
        # DB 연결

    def join_stack(self):
        self.stackedWidget.setCurrentIndex(0)
    def login_stack(self):
        self.stackedWidget.setCurrentIndex(1)
    def go_main(self):
        self.parent().setCurrentIndex(0)


    def login(self):
        print("2222")
        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ham', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT ID,PS FROM log')
        self.id_data=self.cursor.fetchall()
        # self.cursor.execute('SELECT 비밀번호 FROM log')
        # self.ps_data=self.cursor.fetchall()
        # print(self.id_data)
        self.login_id=self.id_2.text()
        # print(self.login_id)
        self.login_ps=self.ps_2.text()
        # print(self.login_ps)
        # for i in self.name_data:
        #     if self.name == i[0] :

        # self.cursor.execute('SELECT 이름 FROM log')
        # self.name_data = self.cursor.fetchall()
        # for i in self.name_data:
        #     if self.name == i[0] :
        #         print("성빈성빈성빈")
        #         print(self.name_data)
        #         print("11")
        #         print("로그인 성공")


        for i in self.id_data:
            if self.login_id == i[0] and self.login_ps == i[1]:
                print("11")
                print(i[0],i[1],"dududdudu")
                # print(self.b)
                print("로그인 성공")
                # print(self.name)
                # self.go_main()
                # self.parent().setCurrentIndex(0)
                # page 바꾸고
                return self.login_id

            # if self.login_ps in self.ps_data:
            #     print("22")
            # else:
            #     print("로그인 성공!!!!!!")












    def join(self):
        self.conn = p.connect(host='localhost', port=3306, user='root', password='1234',
                              db='ham', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM log')
        self.b = self.cursor.fetchall()
        self.id=self.id_join.text()
        self.ps=self.ps_join.text()
        self.ps_look=self.ps_look.text()
        self.name=self.name_join.text()
        self.id_list=[]
        # print(self.id_list)


        for i in range(0,len(self.b)):
            self.id_list.append(self.b[i][0])
        print(self.id_list)


        # print(self.name_data)
        # if self.name in self.name_data:
        #     print("***********")
        # else:
        #     print("############")


        # self.cursor.execute('SELECT ID FROM log')
        # print(self.c)
        if self.id != '' and self.ps != '' and self.ps_look != '' and self.name != '':
            QMessageBox.information(self, '요건충족', 'dsadsa')
            if self.id in self.id_list:
                QMessageBox.warning(self, '아이디 중복', '중복 아이디 오류')
                print("중복!!!!!!!")
            else:
                QMessageBox.information(self, '통과 아이디', '중복확인 성공')
                print("아이디 통과 @@@@")
                if self.ps != self.ps_look:
                    QMessageBox.warning(self, '비밀번호 오류', '오류 비밀번호')
                else:
                    QMessageBox.information(self, '회원가입 완료', '맞음 비밀번호')
                    self.cursor.execute("set SQL_SAFE_UPDATES = 0")
                    # self.cursor.execute(f'update log set ID="{self.id}",PS="{self.ps}" WHERE 이름="{self.name}"')
                    # insert into log values('b', '1', '김철수', '손님');
                    self.cursor.execute(f'insert into log values("{self.id}","{self.ps}","{self.name}","손님")')
                    # print(self.name,self.id,self.ps)
                    # print(self.b[0][0],self.b[0][1])
                    # print(self.b)
                    #
                    # self.cursor.execute("set SQL_SAFE_UPDATES = 1")
                    self.conn.commit()
                    self.conn.close()



                # self.cursor.execute(f'SELECT ID, 비밀번호, 이름 FROM log where 이름 = 김기태')





        else:
            QMessageBox.warning(self, '필수요소', 'sdasdsa')  # 이거나옴







if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = log()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
