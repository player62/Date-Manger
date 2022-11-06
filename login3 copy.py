import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
dic_login = {}
login_cnt = 0
Lc1 = ''
Lc2 = ''
Lc3 = ''
timetable = []
login_timetable = []
location_list = []

# 시작화면 구성


class Start(QDialog):
    def __init__(self):
        super(Start, self).__init__()
        loadUi("start.ui", self)
        self.start_button.clicked.connect(self.startfunction)

    def startfunction(self):
        start = Locate_choose()
        widget.addWidget(start)
        widget.setCurrentIndex(widget.currentIndex()+1)

# 장소 선택화면 구성


class Locate_choose(QDialog):
    def __init__(self):
        super(Locate_choose, self).__init__()
        loadUi("locate_choose.ui", self)
        self.Submit_button.clicked.connect(self.Submitfunction)

    def Submitfunction(self):

        location_list.append(self.locate_1.text())  # locate에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
        location_list.append(self.locate_2.text())
        location_list.append(self.locate_3.text())
        start2 = Login()
        widget.addWidget(start2)
        widget.setCurrentIndex(widget.currentIndex()+1)

# 로그인 화면 구현


class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.Login_button.clicked.connect(self.loginfunction)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        global login_cnt
        if (login_cnt == 0):  # 최초 로그인
            ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
            PW = self.PW.text()
            dic_login[ID] = PW
            print("Login Success ID: ", ID)
            login_cnt += 1
            self.loginwindowtransfer()

        else:  # 다음 로그인
            ID = self.ID.text()  # 다시 id 받음
            if (ID in dic_login.keys()):  # 기존에 있는 id인지 확인
                PW2 = self.PW.text()  # 비밀번호 기존것과 확인
                if (PW2 == dic_login[ID]):
                    print("Login Success ID: ", ID)
                    self.loginwindowtransfer()
                else:
                    print("Wrong PW")  # 로그인 실패시 그화면 그대로

            else:  # 기존에 없는 id일
                ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
                PW = self.PW.text()
                dic_login[ID] = PW
                login_cnt += 1
                print("Login Success ID: ", ID)
                self.loginwindowtransfer()

    def loginwindowtransfer(self):  # 로그인 성공시 화면 전환을 함수로 따로 묶음
        start3 = Main()
        widget.addWidget(start3)
        widget.setCurrentIndex(widget.currentIndex()+1)


#메인 화면
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("mainwindow.ui", self)
        # 지역 선택
        for lc in location_list:
            self.locateselect_combobox.addItem(lc)  # 콤보박스에 장소 추가
            
        if len(login_timetable) != 0:
            for i in range(0, len(login_timetable)):
                if(login_timetable[i][0] == login_cnt):
                    print(login_timetable[i])

        self.gotologin_button.clicked.connect(self.returnfunction)  # 로그인으로 회귀

        self.makescedule_button.clicked.connect(self.timeselect)

    def timeselect(self):
        global login_cnt
      
   
        print(login_cnt)
        
        

        for i in self.time_table.selectedIndexes():
            print("%d %d"%(i.row()+1,i.column()+1))
            login_timetable.append([login_cnt, i.row()+1,i.column()+1])
            
        print(login_timetable)

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
mainwindow = Start()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(900)
widget.setFixedHeight(1000)
widget.show()
app.exec_()