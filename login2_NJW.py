# Import Modules
# ====================================================================================================
import sys
from os import environ
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import pandas as pd
import openpyxl
import numpy as np
# ====================================================================================================

# Function for Fixing Font Sizes by Screen Resolution
# ====================================================================================================
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
# ====================================================================================================

# Variables Declaration
# ====================================================================================================
loginDict = {}
loginCount = 0
login = []
locationList = []

member = 0

member_schedule_1_1 = []
member_schedule_2_1 = []
member_schedule_3_1 = []
member_schedule_4_1 = []
member_schedule_5_1 = []
member_schedule_6_1 = []
total_schedule = []

reset_1 = np.full(27, 0)
reset_2 = np.full(27, 0)
reset_3 = np.full(27, 0)
reset_4 = np.full(27, 0)
reset_5 = np.full(27, 0)
reset_6 = np.full(27, 0)
reset_7 = np.full(27, 0)
reset_8 = np.full(27, 0)  # 이걸로 재 초기화

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
# ====================================================================================================

# Start Screen Configuration
# ====================================================================================================
class Start(QDialog):
    def __init__(self):
        super(Start, self).__init__()
        loadUi("forTesting2.ui", self)
        self.start_button.clicked.connect(self.startfunction)

    def startfunction(self):
        global member
        member = self.member_num.text()
        member = int(member)
        start = Locate_choose()
        widget.addWidget(start)
        widget.setCurrentIndex(widget.currentIndex()+1)
# ====================================================================================================

# Location Choosing Screen Configuration
# ====================================================================================================
class Locate_choose(QDialog):
    def __init__(self):
        super(Locate_choose, self).__init__()
        loadUi("locationTesting.ui", self)
        self.Submit_button.clicked.connect(self.Submitfunction)

    def Submitfunction(self):
        
        locationList.append(self.locate_1.text())
        locationList.append(self.locate_2.text())
        locationList.append(self.locate_3.text())
        
        start2 = Login()
        widget.addWidget(start2)
        widget.setCurrentIndex(widget.currentIndex()+1)
# ====================================================================================================

# Login Screen Configuration
# ====================================================================================================
class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.Login_button.clicked.connect(self.loginfunction)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        global loginCount
        if (loginCount == 0):  # 최초 로그인
            ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
            PW = self.PW.text()
            loginDict[ID] = PW
            login.append(ID)
            print(login)
            print("Login Success ID: ", ID)
            loginCount += 1
            self.loginwindowtransfer()

        else:  # 다음 로그인
            ID = self.ID.text()  # 다시 id 받음
            if (ID in loginDict.keys()):  # 기존에 있는 id인지 확인
                PW2 = self.PW.text()  # 비밀번호 기존것과 확인
                if (PW2 == loginDict[ID]):
                    print("Login Success ID: ", ID)
                    login.append(ID)
                    print(login)
                    self.loginwindowtransfer()
                else:
                    print("Wrong PW")  # 로그인 실패시 그화면 그대로

            else:  # 기존에 없는 id일
                ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
                PW = self.PW.text()
                loginDict[ID] = PW
                login.append(ID)
                loginCount += 1
                print(login)
                print("Login Success ID: ", ID)
                self.loginwindowtransfer()

    def loginwindowtransfer(self):  # 로그인 성공시 화면 전환을 함수로 따로 묶음
        start3 = Main()
        widget.addWidget(start3)
        widget.setCurrentIndex(widget.currentIndex()+1)
# ====================================================================================================

# Main Screen Configuration
# ====================================================================================================
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("mainwindow.ui", self)
        # 지역 선택
        
        for lc in locationList:
            self.locateselect_combobox.addItem(lc)  # 콤보박스에 장소 추가

        self.gotologin_button.clicked.connect(self.returnfunction)  # 로그인으로 회귀

        self.makescedule_button.clicked.connect(self.timeselect)

    def timeselect(self):  # 개인별 시간 선택
        global loginCount

        print(loginCount)
        global member

        global member_schedule_1
        global member_schedule_2
        global member_schedule_3
        global member_schedule_4
        global member_schedule_5
        global member_schedule_6

        global member_schedule_1_1
        global member_schedule_2_1
        global member_schedule_3_1
        global member_schedule_4_1
        global member_schedule_5_1
        global member_schedule_6_1

        # x좌표 col
        # 왼쪽 위가 0,0 4사분면으로 생각하고 x축 열 /  y축 행
        if (loginCount == 1):

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
            member_schedule_1_1 = np.array(member_schedule_1)

        elif loginCount == 2:
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
            member_schedule_2_1 = np.array(member_schedule_2)
            
            self.result_print()

        elif loginCount == 3:

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
            member_schedule_3_1 = np.array(member_schedule_3)
            #total_schedule = member_schedule_1_1 + member_schedule_2_1 + member_schedule_3_1
            #print(total_schedule)
            self.result_print()

        elif loginCount == 4:

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
            member_schedule_4_1 = np.array(member_schedule_4)
            self.result_print()

        elif loginCount == 5:

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
            member_schedule_5_1 = np.array(member_schedule_5)
            self.result_print()

        elif loginCount == 6:

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
            member_schedule_6_1 = np.array(member_schedule_1)
            self.result_print()

    def reset_1(self):  # -1로 다시 초기화
        global reset_8
        for i in range(7):
            member_schedule_1[i][:] = reset_8

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

    def result_print(self):
        global total_schedule

        global member_schedule_1_1
        global member_schedule_2_1
        global member_schedule_3_1
        global member_schedule_4_1
        global member_schedule_5_1
        global member_schedule_6_1
        
        if (member == 1):
            total_schedule = member_schedule_1_1
            print(total_schedule)
        elif (member == 2):
            total_schedule = member_schedule_1_1 + member_schedule_2_1
            print(total_schedule)
        elif (member == 3):
            total_schedule = member_schedule_1_1 + member_schedule_2_1 + member_schedule_3_1
            print(total_schedule)
        elif (member == 4):
            total_schedule = member_schedule_1_1 + member_schedule_2_1 + member_schedule_3_1 + member_schedule_4_1
            print(total_schedule)
        elif (member == 5):
            total_schedule = member_schedule_1_1 + member_schedule_2_1 + member_schedule_3_1 + member_schedule_4_1 + member_schedule_5_1
            print(total_schedule)
        elif (member == 6):
            total_schedule = member_schedule_1_1 + member_schedule_2_1 + member_schedule_3_1 + member_schedule_4_1 + member_schedule_5_1 + member_schedule_6_1
            print(total_schedule)

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex()+1)
# ====================================================================================================

# Application Run
# ====================================================================================================
suppress_qt_warnings()
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_EnableHighDpiScaling)
mainwindow = Start()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMaximumWidth(900)
widget.setMaximumHeight(900)
widget.show()
app.exec_()
# ====================================================================================================
