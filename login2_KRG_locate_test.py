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
import copy
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
new_login = []
locationList = []

member = 0

member_schedule_1_1 = []
member_schedule_2_1 = []
member_schedule_3_1 = []
member_schedule_4_1 = []
member_schedule_5_1 = []
member_schedule_6_1 = []

total_schedule_lc_1 = []
total_schedule_lc_2 = []
total_schedule_lc_3 = []

reset_1 = np.full(27, 0)
reset_2 = np.full(27, 0)
reset_3 = np.full(27, 0)
reset_4 = np.full(27, 0)
reset_5 = np.full(27, 0)
reset_6 = np.full(27, 0)
reset_7 = np.full(27, 0)
reset_8 = np.full(27, 0)  # 이걸로 재 초기화

columns_day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
index_time = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
              '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00']

SUN = 0
MON = 1
TUE = 2
WED = 3
THU = 4
FRI = 5
SAT = 6
ID = ''
PW = ''

calendar = {SUN: reset_1, MON: reset_2, TUE: reset_3,
            WED: reset_4, THU: reset_5, FRI: reset_6, SAT: reset_7}

member_schedule_1_lc_1 = copy.deepcopy(calendar)
member_schedule_2_lc_1 = copy.deepcopy(calendar)
member_schedule_3_lc_1 = copy.deepcopy(calendar)
member_schedule_4_lc_1 = copy.deepcopy(calendar)
member_schedule_5_lc_1 = copy.deepcopy(calendar)
member_schedule_6_lc_1 = copy.deepcopy(calendar)

member_schedule_1_lc_2 = copy.deepcopy(calendar)
member_schedule_2_lc_2 = copy.deepcopy(calendar)
member_schedule_3_lc_2 = copy.deepcopy(calendar)
member_schedule_4_lc_2 = copy.deepcopy(calendar)
member_schedule_5_lc_2 = copy.deepcopy(calendar)
member_schedule_6_lc_2 = copy.deepcopy(calendar)

member_schedule_1_lc_3 = copy.deepcopy(calendar)
member_schedule_2_lc_3 = copy.deepcopy(calendar)
member_schedule_3_lc_3 = copy.deepcopy(calendar)
member_schedule_4_lc_3 = copy.deepcopy(calendar)
member_schedule_5_lc_3 = copy.deepcopy(calendar)
member_schedule_6_lc_3 = copy.deepcopy(calendar)
# ====================================================================================================

# Start Screen Configuration
# ====================================================================================================


class Start(QDialog):
    def __init__(self):
        super(Start, self).__init__()
        loadUi("start.ui", self)
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
        loadUi("locate_choose.ui", self)
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
        global new_login
        global ID
        global PW
        if (loginCount == 0):  # 최초 로그인
            ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
            PW = self.PW.text()
            loginDict[ID] = PW
            login.append(ID)
            for ID in login:
                if ID not in new_login:
                    new_login.append(ID)
            print(new_login)

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
                    for ID in login:
                        if ID not in new_login:
                            new_login.append(ID)
                    print(new_login)
                    self.loginwindowtransfer()
                else:
                    print("Wrong PW")  # 로그인 실패시 그화면 그대로

            else:  # 기존에 없는 id일
                ID = self.ID.text()  # id에서 텍스트 가져오겠다, 그리고 변수에 넣겠다
                PW = self.PW.text()
                loginDict[ID] = PW
                login.append(ID)
                for ID in login:
                    if ID not in new_login:
                        new_login.append(ID)
                loginCount += 1
                print(new_login)
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
        # print(loginCount)
        global member

        global member_schedule_1_lc_1
        global member_schedule_2_lc_1
        global member_schedule_3_lc_1
        global member_schedule_4_lc_1
        global member_schedule_5_lc_1
        global member_schedule_6_lc_1

        global member_schedule_1_lc_2
        global member_schedule_2_lc_2
        global member_schedule_3_lc_2
        global member_schedule_4_lc_2
        global member_schedule_5_lc_2
        global member_schedule_6_lc_2

        global member_schedule_1_lc_3
        global member_schedule_2_lc_3
        global member_schedule_3_lc_3
        global member_schedule_4_lc_3
        global member_schedule_5_lc_3
        global member_schedule_6_lc_3

        # print(member_schedule_6_1) 여기까지 0
        # x좌표 col
        # 왼쪽 위가 0,0 4사분면으로 생각하고 x축 열 /  y축 행


# 장소 테스트
        if new_login[0] == ID:  # 돌아와도 그 유저만 수정
            self.reset_1()
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_1_lc_1[SUN][i.row()] == 1):
                            member_schedule_1_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_1_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_1_lc_1[MON][i.row()] == 1):
                            member_schedule_1_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_1_lc_1[TUE][i.row()] == 1):
                            member_schedule_1_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_1_lc_1[WED][i.row()] == 1):
                            member_schedule_1_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_1_lc_1[THU][i.row()] == 1):
                            member_schedule_1_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_1_lc_1[FRI][i.row()] == 1):
                            member_schedule_1_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_1_lc_1[SAT][i.row()] == 1):
                            member_schedule_1_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_1_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택

                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_1_lc_2[SUN][i.row()] == 1):
                            member_schedule_1_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_1_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_1_lc_2[MON][i.row()] == 1):
                            member_schedule_1_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_1_lc_2[TUE][i.row()] == 1):
                            member_schedule_1_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_1_lc_2[WED][i.row()] == 1):
                            member_schedule_1_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_1_lc_2[THU][i.row()] == 1):
                            member_schedule_1_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_1_lc_2[FRI][i.row()] == 1):
                            member_schedule_1_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_1_lc_2[SAT][i.row()] == 1):
                            member_schedule_1_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_1_lc_2[SAT][i.row()] = 1

            elif (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_1_lc_3[SUN][i.row()] == 1):
                            member_schedule_1_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_1_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_1_lc_3[MON][i.row()] == 1):
                            member_schedule_1_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_1_lc_3[TUE][i.row()] == 1):
                            member_schedule_1_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_1_lc_3[WED][i.row()] == 1):
                            member_schedule_1_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_1_lc_3[THU][i.row()] == 1):
                            member_schedule_1_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_1_lc_3[FRI][i.row()] == 1):
                            member_schedule_1_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_1_lc_3[SAT][i.row()] == 1):
                            member_schedule_1_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_1_lc_3[SAT][i.row()] = 1

        elif new_login[1] == ID:  # 돌아와도 그 유저만 수정 #2번유저
            self.reset_2()
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_2_lc_1[SUN][i.row()] == 1):
                            member_schedule_2_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_2_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_2_lc_1[MON][i.row()] == 1):
                            member_schedule_2_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_2_lc_1[TUE][i.row()] == 1):
                            member_schedule_2_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_2_lc_1[WED][i.row()] == 1):
                            member_schedule_2_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_2_lc_1[THU][i.row()] == 1):
                            member_schedule_2_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_2_lc_1[FRI][i.row()] == 1):
                            member_schedule_2_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_2_lc_1[SAT][i.row()] == 1):
                            member_schedule_2_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_2_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_2_lc_2[SUN][i.row()] == 1):
                            member_schedule_2_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_2_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_2_lc_2[MON][i.row()] == 1):
                            member_schedule_2_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_2_lc_2[TUE][i.row()] == 1):
                            member_schedule_2_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_2_lc_2[WED][i.row()] == 1):
                            member_schedule_2_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_2_lc_2[THU][i.row()] == 1):
                            member_schedule_2_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_2_lc_2[FRI][i.row()] == 1):
                            member_schedule_2_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_2_lc_2[SAT][i.row()] == 1):
                            member_schedule_2_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_2_lc_2[SAT][i.row()] = 1

            if (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_2_lc_3[SUN][i.row()] == 1):
                            member_schedule_2_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_2_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_2_lc_3[MON][i.row()] == 1):
                            member_schedule_2_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_2_lc_3[TUE][i.row()] == 1):
                            member_schedule_2_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_2_lc_3[WED][i.row()] == 1):
                            member_schedule_2_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_2_lc_3[THU][i.row()] == 1):
                            member_schedule_2_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_2_lc_3[FRI][i.row()] == 1):
                            member_schedule_2_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_2_lc_3[SAT][i.row()] == 1):
                            member_schedule_2_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_2_lc_3[SAT][i.row()] = 1

        elif new_login[2] == ID:  # 돌아와도 그 유저만 수정 # 3번유저
            self.reset_3()
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_3_lc_1[SUN][i.row()] == 1):
                            member_schedule_3_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_3_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_3_lc_1[MON][i.row()] == 1):
                            member_schedule_3_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_3_lc_1[TUE][i.row()] == 1):
                            member_schedule_3_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_3_lc_1[WED][i.row()] == 1):
                            member_schedule_3_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_3_lc_1[THU][i.row()] == 1):
                            member_schedule_3_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_3_lc_1[FRI][i.row()] == 1):
                            member_schedule_3_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_3_lc_1[SAT][i.row()] == 1):
                            member_schedule_3_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_3_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_3_lc_2[SUN][i.row()] == 1):
                            member_schedule_3_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_3_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_3_lc_2[MON][i.row()] == 1):
                            member_schedule_3_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_3_lc_2[TUE][i.row()] == 1):
                            member_schedule_3_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_3_lc_2[WED][i.row()] == 1):
                            member_schedule_3_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_3_lc_2[THU][i.row()] == 1):
                            member_schedule_3_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_3_lc_2[FRI][i.row()] == 1):
                            member_schedule_3_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_3_lc_2[SAT][i.row()] == 1):
                            member_schedule_3_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_3_lc_2[SAT][i.row()] = 1

            if (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_3_lc_3[SUN][i.row()] == 1):
                            member_schedule_3_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_3_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_3_lc_3[MON][i.row()] == 1):
                            member_schedule_3_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_3_lc_3[TUE][i.row()] == 1):
                            member_schedule_3_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_3_lc_3[WED][i.row()] == 1):
                            member_schedule_3_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_3_lc_3[THU][i.row()] == 1):
                            member_schedule_3_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_3_lc_3[FRI][i.row()] == 1):
                            member_schedule_3_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_3_lc_3[SAT][i.row()] == 1):
                            member_schedule_3_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_3_lc_3[SAT][i.row()] = 1

        elif new_login[3] == ID:  # 돌아와도 그 유저만 수정 #4번유저
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_4_lc_1[SUN][i.row()] == 1):
                            member_schedule_4_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_4_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_4_lc_1[MON][i.row()] == 1):
                            member_schedule_4_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_4_lc_1[TUE][i.row()] == 1):
                            member_schedule_4_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_4_lc_1[WED][i.row()] == 1):
                            member_schedule_4_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_4_lc_1[THU][i.row()] == 1):
                            member_schedule_4_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_4_lc_1[FRI][i.row()] == 1):
                            member_schedule_4_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_4_lc_1[SAT][i.row()] == 1):
                            member_schedule_4_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_4_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_4_lc_2[SUN][i.row()] == 1):
                            member_schedule_4_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_4_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_4_lc_2[MON][i.row()] == 1):
                            member_schedule_4_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_4_lc_2[TUE][i.row()] == 1):
                            member_schedule_4_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_4_lc_2[WED][i.row()] == 1):
                            member_schedule_4_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_4_lc_2[THU][i.row()] == 1):
                            member_schedule_4_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_4_lc_2[FRI][i.row()] == 1):
                            member_schedule_4_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_4_lc_2[SAT][i.row()] == 1):
                            member_schedule_4_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_4_lc_2[SAT][i.row()] = 1

            if (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_4_lc_3[SUN][i.row()] == 1):
                            member_schedule_4_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_4_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_4_lc_3[MON][i.row()] == 1):
                            member_schedule_4_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_4_lc_3[TUE][i.row()] == 1):
                            member_schedule_4_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_4_lc_3[WED][i.row()] == 1):
                            member_schedule_4_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_4_lc_3[THU][i.row()] == 1):
                            member_schedule_4_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_4_lc_3[FRI][i.row()] == 1):
                            member_schedule_4_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_4_lc_3[SAT][i.row()] == 1):
                            member_schedule_4_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_4_lc_3[SAT][i.row()] = 1

        elif new_login[2] == ID:  # 돌아와도 그 유저만 수정 #5번유저
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_5_lc_1[SUN][i.row()] == 1):
                            member_schedule_5_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_5_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_5_lc_1[MON][i.row()] == 1):
                            member_schedule_5_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_5_lc_1[TUE][i.row()] == 1):
                            member_schedule_5_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_5_lc_1[WED][i.row()] == 1):
                            member_schedule_5_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_5_lc_1[THU][i.row()] == 1):
                            member_schedule_5_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_5_lc_1[FRI][i.row()] == 1):
                            member_schedule_5_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_5_lc_1[SAT][i.row()] == 1):
                            member_schedule_5_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_5_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_5_lc_2[SUN][i.row()] == 1):
                            member_schedule_5_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_5_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_5_lc_2[MON][i.row()] == 1):
                            member_schedule_5_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_5_lc_2[TUE][i.row()] == 1):
                            member_schedule_5_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_5_lc_2[WED][i.row()] == 1):
                            member_schedule_5_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_5_lc_2[THU][i.row()] == 1):
                            member_schedule_5_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_5_lc_2[FRI][i.row()] == 1):
                            member_schedule_5_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_5_lc_2[SAT][i.row()] == 1):
                            member_schedule_5_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_5_lc_2[SAT][i.row()] = 1

            if (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_5_lc_3[SUN][i.row()] == 1):
                            member_schedule_5_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_5_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_5_lc_3[MON][i.row()] == 1):
                            member_schedule_5_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_5_lc_3[TUE][i.row()] == 1):
                            member_schedule_5_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_5_lc_3[WED][i.row()] == 1):
                            member_schedule_5_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_5_lc_3[THU][i.row()] == 1):
                            member_schedule_5_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_5_lc_3[FRI][i.row()] == 1):
                            member_schedule_5_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_5_lc_3[SAT][i.row()] == 1):
                            member_schedule_5_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_5_lc_3[SAT][i.row()] = 1

        elif new_login[5] == ID:  # 돌아와도 그 유저만 수정 #6번 유저
            if (locationList[0] == self.locateselect_combobox.currentText()):  # 1번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_6_lc_1[SUN][i.row()] == 1):
                            member_schedule_6_lc_1[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_6_lc_1[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_6_lc_1[MON][i.row()] == 1):
                            member_schedule_6_lc_1[MON][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_6_lc_1[TUE][i.row()] == 1):
                            member_schedule_6_lc_1[TUE][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_6_lc_1[WED][i.row()] == 1):
                            member_schedule_6_lc_1[WED][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_6_lc_1[THU][i.row()] == 1):
                            member_schedule_6_lc_1[THU][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_6_lc_1[FRI][i.row()] == 1):
                            member_schedule_6_lc_1[FRI][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_6_lc_1[SAT][i.row()] == 1):
                            member_schedule_6_lc_1[SAT][i.row()] = 0
                        else:
                            member_schedule_6_lc_1[SAT][i.row()] = 1

            if (locationList[1] == self.locateselect_combobox.currentText()):  # 2번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_6_lc_2[SUN][i.row()] == 1):
                            member_schedule_6_lc_2[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_6_lc_2[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_6_lc_2[MON][i.row()] == 1):
                            member_schedule_6_lc_2[MON][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_6_lc_2[TUE][i.row()] == 1):
                            member_schedule_6_lc_2[TUE][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_6_lc_2[WED][i.row()] == 1):
                            member_schedule_6_lc_2[WED][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_6_lc_2[THU][i.row()] == 1):
                            member_schedule_6_lc_2[THU][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_6_lc_2[FRI][i.row()] == 1):
                            member_schedule_6_lc_2[FRI][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_6_lc_2[SAT][i.row()] == 1):
                            member_schedule_6_lc_2[SAT][i.row()] = 0
                        else:
                            member_schedule_6_lc_2[SAT][i.row()] = 1

            if (locationList[2] == self.locateselect_combobox.currentText()):  # 3번 장소 선택
                for i in self.time_table.selectedIndexes():
                    if (i.column() == 0):
                        if (member_schedule_6_lc_3[SUN][i.row()] == 1):
                            member_schedule_6_lc_3[SUN][i.row()] = 0
                        else:
                            # 해당 값 1로 대체
                            member_schedule_6_lc_3[SUN][i.row()] = 1
                    if (i.column() == 1):
                        if (member_schedule_6_lc_3[MON][i.row()] == 1):
                            member_schedule_6_lc_3[MON][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[MON][i.row()] = 1
                    if (i.column() == 2):
                        if (member_schedule_6_lc_3[TUE][i.row()] == 1):
                            member_schedule_6_lc_3[TUE][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[TUE][i.row()] = 1
                    if (i.column() == 3):
                        if (member_schedule_6_lc_3[WED][i.row()] == 1):
                            member_schedule_6_lc_3[WED][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[WED][i.row()] = 1
                    if (i.column() == 4):
                        if (member_schedule_6_lc_3[THU][i.row()] == 1):
                            member_schedule_6_lc_3[THU][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[THU][i.row()] = 1
                    if (i.column() == 5):
                        if (member_schedule_6_lc_3[FRI][i.row()] == 1):
                            member_schedule_6_lc_3[FRI][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[FRI][i.row()] = 1
                    if (i.column() == 6):
                        if (member_schedule_6_lc_3[SAT][i.row()] == 1):
                            member_schedule_6_lc_3[SAT][i.row()] = 0
                        else:
                            member_schedule_6_lc_3[SAT][i.row()] = 1

        self.result_process()

        # 여기에 엑셀 불러오기 구현

    def reset_1(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_1_lc_1[i][:] = reset_8
            member_schedule_1_lc_2[i][:] = reset_8
            member_schedule_1_lc_3[i][:] = reset_8

    def reset_2(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_2_lc_1[i][:] = reset_8
            member_schedule_2_lc_2[i][:] = reset_8
            member_schedule_2_lc_3[i][:] = reset_8

    def reset_3(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_3_lc_1[i][:] = reset_8
            member_schedule_3_lc_2[i][:] = reset_8
            member_schedule_3_lc_3[i][:] = reset_8

    def reset_4(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_4_lc_1[i][:] = reset_8
            member_schedule_4_lc_2[i][:] = reset_8
            member_schedule_4_lc_3[i][:] = reset_8

    def reset_5(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_5_lc_1[i][:] = reset_8
            member_schedule_5_lc_2[i][:] = reset_8
            member_schedule_5_lc_3[i][:] = reset_8

    def reset_6(self):  # 0으로 다시 초기화
        for i in range(7):
            member_schedule_6_lc_1[i][:] = reset_8
            member_schedule_6_lc_2[i][:] = reset_8
            member_schedule_6_lc_3[i][:] = reset_8

    def result_process(self):

        global total_schedule_lc_1
        global total_schedule_lc_2
        global total_schedule_lc_3

        global member_schedule_1_lc_1
        global member_schedule_2_lc_1
        global member_schedule_3_lc_1
        global member_schedule_4_lc_1
        global member_schedule_5_lc_1
        global member_schedule_6_lc_1

        global member_schedule_1_lc_2
        global member_schedule_2_lc_2
        global member_schedule_3_lc_2
        global member_schedule_4_lc_2
        global member_schedule_5_lc_2
        global member_schedule_6_lc_2

        global member_schedule_1_lc_3
        global member_schedule_2_lc_3
        global member_schedule_3_lc_3
        global member_schedule_4_lc_3
        global member_schedule_5_lc_3
        global member_schedule_6_lc_3

        member_schedule_1_lc_1 = pd.DataFrame(member_schedule_1_lc_1)
        member_schedule_1_lc_1_print = np.array(member_schedule_1_lc_1)

        member_schedule_1_lc_2 = pd.DataFrame(member_schedule_1_lc_2)
        member_schedule_1_lc_2_print = np.array(member_schedule_1_lc_2)

        member_schedule_1_lc_3 = pd.DataFrame(member_schedule_1_lc_3)
        member_schedule_1_lc_3_print = np.array(member_schedule_1_lc_3)

        member_schedule_2_lc_1 = pd.DataFrame(member_schedule_2_lc_1)
        member_schedule_2_lc_1_print = np.array(member_schedule_2_lc_1)

        member_schedule_2_lc_2 = pd.DataFrame(member_schedule_1_lc_2)
        member_schedule_2_lc_2_print = np.array(member_schedule_1_lc_2)

        member_schedule_2_lc_3 = pd.DataFrame(member_schedule_2_lc_3)
        member_schedule_2_lc_3_print = np.array(member_schedule_2_lc_3)

        member_schedule_3_lc_1 = pd.DataFrame(member_schedule_3_lc_1)
        member_schedule_3_lc_1_print = np.array(member_schedule_3_lc_1)

        member_schedule_3_lc_2 = pd.DataFrame(member_schedule_3_lc_2)
        member_schedule_3_lc_2_print = np.array(member_schedule_3_lc_2)

        member_schedule_3_lc_3 = pd.DataFrame(member_schedule_3_lc_3)
        member_schedule_3_lc_3_print = np.array(member_schedule_3_lc_3)

        member_schedule_4_lc_1 = pd.DataFrame(member_schedule_4_lc_1)
        member_schedule_4_lc_1_print = np.array(member_schedule_4_lc_1)

        member_schedule_4_lc_2 = pd.DataFrame(member_schedule_4_lc_2)
        member_schedule_4_lc_2_print = np.array(member_schedule_4_lc_2)

        member_schedule_4_lc_3 = pd.DataFrame(member_schedule_4_lc_3)
        member_schedule_4_lc_3_print = np.array(member_schedule_4_lc_3)

        member_schedule_5_lc_1 = pd.DataFrame(member_schedule_5_lc_1)
        member_schedule_5_lc_1_print = np.array(member_schedule_5_lc_1)

        member_schedule_5_lc_2 = pd.DataFrame(member_schedule_5_lc_2)
        member_schedule_5_lc_2_print = np.array(member_schedule_5_lc_2)

        member_schedule_5_lc_3 = pd.DataFrame(member_schedule_5_lc_3)
        member_schedule_5_lc_3_print = np.array(member_schedule_5_lc_3)

        member_schedule_6_lc_1 = pd.DataFrame(member_schedule_6_lc_1)
        member_schedule_6_lc_1_print = np.array(member_schedule_6_lc_1)

        member_schedule_6_lc_2 = pd.DataFrame(member_schedule_6_lc_2)
        member_schedule_6_lc_2_print = np.array(member_schedule_6_lc_2)

        member_schedule_6_lc_3 = pd.DataFrame(member_schedule_6_lc_3)
        member_schedule_6_lc_3_print = np.array(member_schedule_6_lc_3)

        if (member == 1):
            total_schedule_lc_1 = member_schedule_1_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print
            self.result_print()

        elif (member == 2):
            total_schedule_lc_1 = member_schedule_1_lc_1_print + member_schedule_2_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print + member_schedule_2_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print + member_schedule_2_lc_3_print
            self.result_print()

        elif (member == 3):
            total_schedule_lc_1 = member_schedule_1_lc_1_print + \
                member_schedule_2_lc_1_print + member_schedule_3_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print + \
                member_schedule_2_lc_2_print + member_schedule_3_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print + \
                member_schedule_2_lc_3_print + member_schedule_3_lc_3_print
            self.result_print()

        elif (member == 4):
            total_schedule_lc_1 = member_schedule_1_lc_1_print + member_schedule_2_lc_1_print + \
                member_schedule_3_lc_1_print + member_schedule_4_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print + member_schedule_2_lc_2_print + \
                member_schedule_3_lc_2_print + member_schedule_4_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print + member_schedule_2_lc_3_print + \
                member_schedule_3_lc_3_print + member_schedule_4_lc_3_print
            self.result_print()
        elif (member == 5):
            total_schedule_lc_1 = member_schedule_1_lc_1_print + member_schedule_2_lc_1_print + \
                member_schedule_3_lc_1_print + \
                member_schedule_4_lc_1_print + member_schedule_5_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print + member_schedule_2_lc_2_print + \
                member_schedule_3_lc_2_print + \
                member_schedule_4_lc_2_print + member_schedule_5_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print + member_schedule_2_lc_3_print + \
                member_schedule_3_lc_3_print + \
                member_schedule_4_lc_3_print + member_schedule_5_lc_3_print
            self.result_print()
        elif (member == 6):
            total_schedule_lc_1 = member_schedule_1_lc_1_print + member_schedule_2_lc_1_print + member_schedule_3_lc_1_print + \
                member_schedule_4_lc_1_print + \
                member_schedule_5_lc_1_print + member_schedule_6_lc_1_print
            total_schedule_lc_2 = member_schedule_1_lc_2_print + member_schedule_2_lc_2_print + member_schedule_3_lc_2_print + \
                member_schedule_4_lc_2_print + \
                member_schedule_5_lc_2_print + member_schedule_6_lc_2_print
            total_schedule_lc_3 = member_schedule_1_lc_3_print + member_schedule_2_lc_3_print + member_schedule_3_lc_3_print + \
                member_schedule_4_lc_3_print + \
                member_schedule_5_lc_3_print + member_schedule_6_lc_3_print

            self.result_print()

    def result_print(self):
        global total_schedule_lc_1
        global total_schedule_lc_2
        global total_schedule_lc_3
        
        total_schedule_to_excel_lc_1 = pd.DataFrame(
            total_schedule_lc_1, index=index_time, columns=columns_day)
        total_schedule_to_excel_lc_2 = pd.DataFrame(
            total_schedule_lc_2, index=index_time, columns=columns_day)
        total_schedule_to_excel_lc_3 = pd.DataFrame(
            total_schedule_lc_2, index=index_time, columns=columns_day)

        print(total_schedule_to_excel_lc_1)
        print(total_schedule_to_excel_lc_2)
        print(total_schedule_to_excel_lc_3)
        xlxs_dir = 'sample.xlsx'
        with pd.ExcelWriter(xlxs_dir) as writer:
            total_schedule_to_excel_lc_1.to_excel(
                writer, sheet_name=locationList[0])
            total_schedule_to_excel_lc_2.to_excel(
                writer, sheet_name=locationList[1])
            total_schedule_to_excel_lc_3.to_excel(
                writer, sheet_name=locationList[2])

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        loadUi("show_result", self)
# ====================================================================================================


# Application Run
# ====================================================================================================
suppress_qt_warnings()
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_EnableHighDpiScaling)
mainwindow = Start()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(900)
widget.setFixedHeight(1000)
widget.show()
app.exec_()
# ====================================================================================================