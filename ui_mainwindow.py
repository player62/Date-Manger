# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\uri42\Desktop\Date-Manger\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(900, 900)
        mainwindow.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(223, 95, 159, 200), stop:0.513812 rgba(224, 212, 107, 200), stop:1 rgba(103, 188, 228, 200));")
        self.widget = QtWidgets.QWidget(mainwindow)
        self.widget.setGeometry(QtCore.QRect(150, 40, 600, 850))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius : 10px;")
        self.widget.setObjectName("widget")
        self.makescedule_button = QtWidgets.QPushButton(self.widget)
        self.makescedule_button.setGeometry(QtCore.QRect(270, 802, 75, 23))
        self.makescedule_button.setStyleSheet("color : rgb(54, 54, 54);\n"
"background-color: rgba(255, 255, 255, 240);\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 10pt;\n"
"\n"
"border-radius : 8px;")
        self.makescedule_button.setObjectName("makescedule_button")
        self.locateselect_combobox = QtWidgets.QComboBox(self.widget)
        self.locateselect_combobox.setGeometry(QtCore.QRect(110, 800, 150, 30))
        self.locateselect_combobox.setStyleSheet("background-color: rgba(255, 255, 255, 240);\n"
"\n"
"font-weight : 400;\n"
"font-family : \'Dosis\';\n"
"font-size : 11pt;\n"
"\n"
"border-radius : 4px;")
        self.locateselect_combobox.setEditable(False)
        self.locateselect_combobox.setIconSize(QtCore.QSize(16, 16))
        self.locateselect_combobox.setFrame(True)
        self.locateselect_combobox.setObjectName("locateselect_combobox")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 19, 540, 771))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(27)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(67)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(34)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.where_label = QtWidgets.QLabel(self.widget)
        self.where_label.setGeometry(QtCore.QRect(30, 800, 80, 30))
        self.where_label.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"font-weight : 600;\n"
"font-family : \'Dosis\';\n"
"font-size : 14pt;")
        self.where_label.setObjectName("where_label")
        self.widget_2 = QtWidgets.QWidget(mainwindow)
        self.widget_2.setGeometry(QtCore.QRect(150, 5, 140, 30))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255, 240);\n"
"\n"
"border-radius : 10px;")
        self.widget_2.setObjectName("widget_2")
        self.gotologin_button = QtWidgets.QPushButton(self.widget_2)
        self.gotologin_button.setGeometry(QtCore.QRect(10, 2, 120, 25))
        self.gotologin_button.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"font-weight : 600;\n"
"font-family : \'Dosis\';\n"
"font-size : 10pt;")
        self.gotologin_button.setObjectName("gotologin_button")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Dialog"))
        self.makescedule_button.setText(_translate("mainwindow", "PushButton"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainwindow", "09:00"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("mainwindow", "09:30"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("mainwindow", "10:00"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("mainwindow", "10:30"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("mainwindow", "11:00"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("mainwindow", "11:30"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("mainwindow", "12:00"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("mainwindow", "12:30"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("mainwindow", "13:00"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("mainwindow", "13:30"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("mainwindow", "14:00"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("mainwindow", "14:30"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("mainwindow", "15:00"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("mainwindow", "15:30"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("mainwindow", "16:00"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("mainwindow", "16:30"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("mainwindow", "17:00"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("mainwindow", "17:30"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("mainwindow", "18:00"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("mainwindow", "18:30"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("mainwindow", "19:00"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("mainwindow", "19:30"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("mainwindow", "20:00"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("mainwindow", "20:30"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("mainwindow", "21:00"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("mainwindow", "21:30"))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("mainwindow", "22:00"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainwindow", "S"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainwindow", "M"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainwindow", "T"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainwindow", "W"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainwindow", "T"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("mainwindow", "F"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("mainwindow", "S"))
        self.where_label.setText(_translate("mainwindow", "Location"))
        self.gotologin_button.setText(_translate("mainwindow", "← Back to Login"))
