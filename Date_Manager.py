# -*- coding: utf-8 -*-
# Import Modules
# ====================================================================================================
import sys
import os
from os import environ
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import uic
import pandas as pd
import win32com.client
from pdf2image import convert_from_path

# ====================================================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Ui_MainWindow, QtBaseClass = uic.loadUiType(BASE_DIR + r'\start.ui')

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
who = 0
newdic = {}
calendar_lc_1 = {}
calendar_lc_2 = {}
calendar_lc_3 = {}

total_schedule_to_excel_lc_1 = {}
total_schedule_to_excel_lc_2 = {}
total_schedule_to_excel_lc_3 = {}

df_1 = {}
df_2 = {}
df_3 = {}

for day in range(7):
    for time in range(27):
        for place in range(3):
            newdic[(time, day, place)] = 0


def resetLocDictionary():
    dictionary = {}
    for time in range(27):
        for day in range(7):
            for mem_num in range(6):
                dictionary[(time, day, mem_num)] = 0

    return dictionary


loc1 = resetLocDictionary()
loc2 = resetLocDictionary()
loc3 = resetLocDictionary()

member = 0

total_schedule_lc_1 = []
total_schedule_lc_2 = []
total_schedule_lc_3 = []


columns_day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

index_time = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
              '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00']

ID = ''
PW = ''

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
        member = self.member.value()
        member = int(member)
        start = Locate_choose()
        widget.addWidget(start)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ====================================================================================================

# Location Choosing Screen Configuration
# ====================================================================================================


class Locate_choose(QDialog):
    def __init__(self):
        super(Locate_choose, self).__init__()
        loadUi("location.ui", self)
        self.Submit_button.clicked.connect(self.Submitfunction)

    def Submitfunction(self):
        global worksheet_name_1
        global worksheet_name_2
        global worksheet_name_3

        locationList.append(self.locate_1.text())
        locationList.append(self.locate_2.text())
        locationList.append(self.locate_3.text())

        worksheet_name_1 = locationList[0]
        worksheet_name_2 = locationList[1]
        worksheet_name_3 = locationList[2]

        start2 = Login()
        widget.addWidget(start2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


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
        global ID
        global PW
        global login
        if (loginCount == 0):  # ?????? ?????????
            ID = self.ID.text()  # id?????? ????????? ???????????????, ????????? ????????? ?????????
            PW = self.PW.text()
            loginDict[ID] = PW
            login = list(loginDict.keys())
            print("Login Success ID: ", ID)
            loginCount += 1
            self.loginwindowtransfer()

        else:  # ?????? ?????????
            ID = self.ID.text()  # ?????? id ??????
            if (ID in loginDict.keys()):  # ????????? ?????? id?????? ??????
                PW2 = self.PW.text()  # ???????????? ???????????? ??????
                if (PW2 == loginDict[ID]):
                    print("Login Success ID: ", ID)
                    login = list(loginDict.keys())
                    self.loginwindowtransfer()
                else:
                    print("Wrong PW")  # ????????? ????????? ????????? ?????????

            else:  # ????????? ?????? id???
                ID = self.ID.text()  # id?????? ????????? ???????????????, ????????? ????????? ?????????
                PW = self.PW.text()
                loginDict[ID] = PW
                login = list(loginDict.keys())
                loginCount += 1
                print("Login Success ID: ", ID)
                self.loginwindowtransfer()

    def loginwindowtransfer(self):  # ????????? ????????? ?????? ????????? ????????? ?????? ??????
        start3 = Main()
        widget.addWidget(start3)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# ====================================================================================================

# Main Screen Configuration
# ====================================================================================================


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)
        # ?????? ??????

        for lc in locationList:
            self.locateselect_combobox.addItem(lc)  # ??????????????? ?????? ??????

        self.gotologin_button.clicked.connect(self.returnfunction)  # ??????????????? ??????

        self.makescedule_button.clicked.connect(self.timeselect)

        self.showResult_button.clicked.connect(self.showresult)

    def timeselect(self):  # ????????? ?????? ??????

        global loc1, loc2, loc3

        keylist = []

        global member
        global who

        # x?????? col
        # ?????? ?????? 0,0 4??????????????? ???????????? x??? ??? /  y??? ???

        if login[0] == ID:  # ???????????? ??? ????????? ??????
            who = 0
            self.make_schedule(keylist)

        elif login[1] == ID:  # ???????????? ??? ????????? ??????
            who = 1
            self.make_schedule(keylist)

        elif login[2] == ID: 
            who = 2
            self.make_schedule(keylist)

        elif login[3] == ID:  
            who = 3
            self.make_schedule(keylist)

        elif login[4] == ID:  
            who = 4
            self.make_schedule(keylist)

        elif login[5] == ID:  
            who = 5
            self.make_schedule(keylist)

    def make_schedule(self, keylist):
        global loc1
        global loc2
        global loc3
        global newdic

        print("%d?????? ??????" % (who+1))
        if (locationList[0] == self.locateselect_combobox.currentText()):  # 1??? ?????? ??????
            for day in range(7):
                for time in range(27):
                    loc1[(day, time, who)] = 0

            for i in self.time_table.selectedIndexes():
                keylist.append((i.row(), i.column(), who))
            for i in keylist:
                loc1[i] = 1

        elif (locationList[1] == self.locateselect_combobox.currentText()):  # 1??? ?????? ??????
            for day in range(7):
                for time in range(27):
                    loc2[(day, time, who)] = 0

            for i in self.time_table.selectedIndexes():

                keylist.append((i.row(), i.column(), who))

            for i in keylist:
                loc2[i] = 1

        elif (locationList[2] == self.locateselect_combobox.currentText()):  # 1??? ?????? ??????
            for day in range(7):
                for time in range(27):
                    loc3[(time, day, who)] = 0

            for i in self.time_table.selectedIndexes():

                keylist.append((i.row(), i.column(), who))
            for i in keylist:
                loc3[i] = 1

        for time in range(27):
            for day in range(7):
                for place in range(3):
                    newdic[(time, day, place)] = 0

        for time in range(27):
            for day in range(7):
                for mem_num in range(6):
                    newdic[(time, day, 0)] += loc1.get((time, day, mem_num))

        for time in range(27):
            for day in range(7):
                for mem_num in range(6):
                    newdic[(time, day, 1)] += loc2.get((time, day, mem_num))

        for time in range(27):
            for day in range(7):
                for mem_num in range(6):
                    newdic[(time, day, 2)] += loc3.get((time, day, mem_num))

        self.save_schedule_lc_1()
        self.save_schedule_lc_2()
        self.save_schedule_lc_3()

    def save_schedule_lc_1(self):
        global loc1
        global newdic
        global calendar_lc_1

        timelist0, timelist1, timelist2, timelist3, timelist4, timelist5, timelist6 = [
        ], [], [], [], [], [], []

        calendar_lc_1 = {'SUN': timelist0, 'MON': timelist1, 'TUE': timelist2,
                         'WED': timelist3, 'THU': timelist4, 'FRI': timelist5, 'SAT': timelist6}

        timelist = [timelist0, timelist1, timelist2,
                    timelist3, timelist4, timelist5, timelist6]

        for day in range(7):
            for time in range(27):
                timelist[day].append(newdic[(time, day, 0)])

        calendar_lc_1 = pd.DataFrame(
            calendar_lc_1, index=index_time, columns=columns_day)

    def save_schedule_lc_2(self):
        global loc2
        global newdic
        global calendar_lc_2
        timelist0, timelist1, timelist2, timelist3, timelist4, timelist5, timelist6 = [
        ], [], [], [], [], [], []

        calendar_lc_2 = {'SUN': timelist0, 'MON': timelist1, 'TUE': timelist2,
                         'WED': timelist3, 'THU': timelist4, 'FRI': timelist5, 'SAT': timelist6}

        timelist = [timelist0, timelist1, timelist2,
                    timelist3, timelist4, timelist5, timelist6]

        for day in range(7):
            for time in range(27):
                timelist[day].append(newdic[(time, day, 1)])

        calendar_lc_2 = pd.DataFrame(
            calendar_lc_2, index=index_time, columns=columns_day)

    def save_schedule_lc_3(self):
        global loc3
        global newdic
        global calendar_lc_3
        timelist0, timelist1, timelist2, timelist3, timelist4, timelist5, timelist6 = [
        ], [], [], [], [], [], []

        calendar_lc_3 = {'SUN': timelist0, 'MON': timelist1, 'TUE': timelist2,
                         'WED': timelist3, 'THU': timelist4, 'FRI': timelist5, 'SAT': timelist6}

        timelist = [timelist0, timelist1, timelist2,
                    timelist3, timelist4, timelist5, timelist6]

        for day in range(7):
            for time in range(27):
                timelist[day].append(newdic[(time, day, 2)])

        calendar_lc_3 = pd.DataFrame(
            calendar_lc_3, index=index_time, columns=columns_day)

        self.result_print()

    def color_np_custom(self, value):
        if value == 0:
            color = "#ffffff"
        elif value == 1:
            color = "#DDEED5"
        elif value == 2:
            color = "#BBDDAA"
        elif value == 3:
            color = "#99CC80"
        elif value == 4:
            color = "#77BB55"
        elif value == 5:
            color = "#55AA2B"
        elif value == 6:
            color = "#339900"
        return f'background-color:{color}'

    def result_print(self):

        global calendar_lc_1
        global calendar_lc_2
        global calendar_lc_3

        global total_schedule_to_excel_lc_1
        global total_schedule_to_excel_lc_2
        global total_schedule_to_excel_lc_3

        total_schedule_to_excel_lc_1 = pd.DataFrame(
            calendar_lc_1, index=index_time, columns=columns_day)
        total_schedule_to_excel_lc_2 = pd.DataFrame(
            calendar_lc_2, index=index_time,  columns=columns_day)
        total_schedule_to_excel_lc_3 = pd.DataFrame(
            calendar_lc_3, index=index_time, columns=columns_day)

        xlxs_dir = 'schedule.xlsx'

        with pd.ExcelWriter(xlxs_dir) as writer:
            total_schedule_to_excel_lc_1.style.applymap(self.color_np_custom).to_excel(
                writer, sheet_name=locationList[0])
            total_schedule_to_excel_lc_2.style.applymap(self.color_np_custom).to_excel(
                writer, sheet_name=locationList[1])
            total_schedule_to_excel_lc_3.style.applymap(self.color_np_custom).to_excel(
                writer, sheet_name=locationList[2])

    def returnfunction(self):
        start4 = Login()
        widget.addWidget(start4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def showresult(self):

        start5 = Result()
        widget.addWidget(start5)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Result(QDialog):
    def __init__(self):
        super(Result, self).__init__()
        loadUi("showResult.ui", self)
        self.loadData_button.clicked.connect(lambda _, xl_path=excel_file_path, sheet_name_1=locationList[0], sheet_name_2=locationList[
                                             1], sheet_name_3=locationList[2]: self.loadExcelData(xl_path, sheet_name_1, sheet_name_2, sheet_name_3))
        self.save_image_button.clicked.connect(self.shoot)
        
        for i in range(3):
            self.tabWidget.setTabText(i, locationList[i])
        
        
    
    def loadExcelData(self, excel_file_dir, worksheet_name_1, worksheet_name_2, worksheet_name_3):
        global df_1
        global df_2
        global df_3

        

        df_1 = pd.read_excel(excel_file_dir, worksheet_name_1)
        df_2 = pd.read_excel(excel_file_dir, worksheet_name_2)
        df_3 = pd.read_excel(excel_file_dir, worksheet_name_3)

        df_1.fillna('', inplace=True)
        df_1.drop(['Unnamed: 0'], axis=1, inplace=True)
        self.result_table_1.setRowCount(df_1.shape[0])
        self.result_table_1.setColumnCount(df_1.shape[1])
        self.result_table_1.setHorizontalHeaderLabels(columns_day)
        self.result_table_1.setVerticalHeaderLabels(index_time)

        for row in df_1.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                    tableItem = QTableWidgetItem(str(value))
                    self.result_table_1.setItem(row[0], col_index, tableItem)
# =====================================================================================================
        df_2.fillna('', inplace=True)
        df_2.drop(['Unnamed: 0'], axis=1, inplace=True)
        self.result_table_2.setRowCount(df_2.shape[0])
        self.result_table_2.setColumnCount(df_2.shape[1])
        self.result_table_2.setHorizontalHeaderLabels(columns_day)
        self.result_table_2.setVerticalHeaderLabels(index_time)

        for row in df_2.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                    tableItem = QTableWidgetItem(str(value))
                    self.result_table_2.setItem(row[0], col_index, tableItem)
# =====================================================================================================
        df_3.fillna('', inplace=True)
        df_3.drop(['Unnamed: 0'], axis=1, inplace=True)
        self.result_table_3.setRowCount(df_3.shape[0])
        self.result_table_3.setColumnCount(df_3.shape[1])
        self.result_table_3.setHorizontalHeaderLabels(columns_day)
        self.result_table_3.setVerticalHeaderLabels(index_time)

        for row in df_3.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                    tableItem = QTableWidgetItem(str(value))
                    self.result_table_3.setItem(row[0], col_index, tableItem)
        excel = win32com.client.dynamic.Dispatch('Excel.Application')
        #excel = win32com.gencache.EnsureDispatch('Excel.Application')
        path =  os.getcwd().replace('\'','\\') + '\\'
        excel.Visible = True
        wb = excel.Workbooks.Open(path + '\schedule.xlsx')
        wb.ExportAsFixedFormat(Type=0, Filename=path +
                               'schedule.pdf', From=1, To=3)


# ====================================================================================================


    def shoot(self):
        path =  os.getcwd().replace('\'','\\') + '\\'
        file_name = "\schedule"
        pages = convert_from_path(path + file_name + ".PDF", poppler_path=path + 'bin')
        for i, page in enumerate(pages):
            page.save(path +file_name+ "_"+ str(locationList[i])+".png", "PNG")
        


# Application Run
# ====================================================================================================
suppress_qt_warnings()

excel_file_path = 'schedule.xlsx'
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_EnableHighDpiScaling)
mainwindow = Start()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMaximumWidth(1300)
widget.setMaximumHeight(900)
widget.show()
app.exec_()
# ====================================================================================================
