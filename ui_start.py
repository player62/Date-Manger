# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\uri42\Desktop\Date-Manger\start.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 1240)
        Dialog.setStyleSheet("background-color : rgb(54,54,54);")
        self.DM_label = QtWidgets.QLabel(Dialog)
        self.DM_label.setGeometry(QtCore.QRect(470, 30, 281, 181))
        self.DM_label.setStyleSheet("font-size : 30pt; color : rgb(255, 255, 255)")
        self.DM_label.setObjectName("DM_label")
        self.DM_label_2 = QtWidgets.QLabel(Dialog)
        self.DM_label_2.setGeometry(QtCore.QRect(460, 170, 151, 16))
        self.DM_label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.DM_label_2.setObjectName("DM_label_2")
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(450, 510, 111, 71))
        self.start_button.setStyleSheet("background-color : rgb(255, 247, 246);")
        self.start_button.setObjectName("start_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DM_label.setText(_translate("Dialog", "DM"))
        self.DM_label_2.setText(_translate("Dialog", "Date Manager"))
        self.start_button.setText(_translate("Dialog", "START"))
