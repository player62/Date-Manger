import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pandas as pd
import openpyxl
import numpy as np
from pprint import pprint
dic_login = {}
login_cnt = 0

Lc1 = ''
Lc2 = ''
Lc3 = ''

member = 0

reset_1 = np.full((27), -1)
reset_2 = np.full((27), -1)
reset_3 = np.full((27), -1)
reset_4 = np.full((27), -1)
reset_5 = np.full((27), -1)
reset_6 = np.full((27), -1)
reset_7 = np.full((27), -1)
reset_8 = np.full((27), -1)  # 이걸로 재 초기화

SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6

member_schedule_1 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}
member_schedule_2 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}
member_schedule_3 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}
member_schedule_4 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}
member_schedule_5 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}
member_schedule_6 = {SUN: reset_1, MON: reset_2, TUE: reset_3,
                     WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}


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
        global Lc1
        global Lc2
        global Lc3

        Lc1 = self.locate_1.text()  # locate에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
        Lc2 = self.locate_2.text()
        Lc3 = self.locate_3.text()
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


# 메인 화면
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("mainwindow.ui", self)
        # 지역 선택
        global Lc1
        global Lc2
        global Lc3
        listlocate = [Lc1, Lc2, Lc3]
        for lc in listlocate:
            self.locateselect_combobox.addItem(lc)  # 콤보박스에 장소 추가

        self.gotologin_button.clicked.connect(self.returnfunction)  # 로그인으로 회귀

        self.makescedule_button.clicked.connect(self.timeselect)

    def timeselect(self):  # 개인별 시간 선택
        global login_cnt

        print(login_cnt)

        global member_schedule_1
        global member_schedule_2
        global member_schedule_3
        global member_schedule_4
        global member_schedule_5
        global member_schedule_6

        # x좌표 col
        # 왼쪽 위가 0,0 4사분면으로 생각하고 x축 열 /  y축 행
        if (login_cnt == 1):
            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_1[SUN][i.row()] = 1  # 해당 값 1로 대체
                if (i.column() == 1):
                    member_schedule_1[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_1[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_1[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_1[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_1[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_1[SAT][i.row()] = 1

            member_schedule_1 = pd.DataFrame(member_schedule_1)
            member_schedule_1 = np.array(member_schedule_1)
            print(member_schedule_1)

        elif login_cnt == 2:

            self.reset_2()

            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_2[SUN][i.row()] = 1  # 해당 값 1로 대체
                if (i.column() == 1):
                    member_schedule_2[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_2[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_2[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_2[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_2[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_2[SAT][i.row()] = 1
            member_schedule_2 = pd.DataFrame(member_schedule_2)
            member_schedule_2 = np.array(member_schedule_2)
            print(member_schedule_2)

        elif login_cnt == 3:

            self.reset_3()

            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_3[SUN][i.row()] = 1  # 해당 값 1로 대체
                if (i.column() == 1):
                    member_schedule_3[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_3[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_3[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_3[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_3[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_3[SAT][i.row()] = 1

            member_schedule_3 = pd.DataFrame(member_schedule_3)
            print(member_schedule_3)
        elif login_cnt == 4:

            self.reset_4()

            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_4[SUN][i.row()] = 1
                if (i.column() == 1):
                    member_schedule_4[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_4[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_4[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_4[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_4[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_4[SAT][i.row()] = 1

            member_schedule_4 = pd.DataFrame(member_schedule_4)

        elif login_cnt == 5:

            self.reset_5()

            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_5[SUN][i.row()] = 1
                if (i.column() == 1):
                    member_schedule_5[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_5[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_5[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_5[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_5[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_5[SAT][i.row()] = 1

            member_schedule_5 = pd.DataFrame(member_schedule_5)

        elif login_cnt == 6:

            self.reset_6()

            for i in self.time_table.selectedIndexes():
                if (i.column() == 0):
                    member_schedule_6[SUN][i.row()] = 1  # 해당 값 1로 대체
                if (i.column() == 1):
                    member_schedule_6[MON][i.row()] = 1
                if (i.column() == 2):
                    member_schedule_6[TUE][i.row()] = 1
                if (i.column() == 3):
                    member_schedule_6[WED][i.row()] = 1
                if (i.column() == 4):
                    member_schedule_6[THU][i.row()] = 1
                if (i.column() == 5):
                    member_schedule_6[FRI][i.row()] = 1
                if (i.column() == 6):
                    member_schedule_6[SAT][i.row()] = 1

            member_schedule_6 = pd.DataFrame(member_schedule_6)

        #new = member_schedule_1 + member_schedule_2
        # print(new)

    def reset_2(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_2[i][0:] = reset_8

    def reset_3(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_3[i][0:] = reset_8

    def reset_4(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_4[i][0:] = reset_8

    def reset_5(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_5[i][0:] = reset_8

    def reset_6(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_6[i][0:] = reset_8

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex()+1)

        """new = {}
        new = member_schedule_1 + member_schedule_2
        new = pd.DataFrame(new)
        print(new)
"""


app = QApplication(sys.argv)
mainwindow = Start()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(900)
widget.setFixedHeight(1000)
widget.show()
app.exec_()