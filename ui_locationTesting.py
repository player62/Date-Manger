from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 900)
        Dialog.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(223, 95, 159, 200), stop:0.513812 rgba(224, 212, 107, 200), stop:1 rgba(103, 188, 228, 200))")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius : 10px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color : rgb(0, 0, 0);\n"
"background-color : rgb(255, 255, 255);\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 26pt; ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.LocationLayout = QtWidgets.QVBoxLayout()
        self.LocationLayout.setObjectName("LocationLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"font-weight : 600;\n"
"font-family : \'Dosis\';\n"
"font-size : 10pt;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.LocationLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.locate_1 = QtWidgets.QLineEdit(self.widget)
        self.locate_1.setStyleSheet("color : rgba(0, 0, 0, 240);\n"
"background-color : rgba(0, 0, 0, 0);\n"
"\n"
"font-size:8pt;\n"
"font-family : \'Dosis\';")
        self.locate_1.setObjectName("locate_1")
        self.horizontalLayout_5.addWidget(self.locate_1)
        self.LocationLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LocationLayout.addItem(spacerItem3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"font-weight : 600;\n"
"font-family : \'Dosis\';\n"
"font-size : 10pt;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.LocationLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.locate_2 = QtWidgets.QLineEdit(self.widget)
        self.locate_2.setStyleSheet("color : rgba(0, 0, 0, 240);\n"
"background-color : rgba(0, 0, 0, 0);\n"
"\n"
"font-size:8pt;\n"
"font-family : \'Dosis\';")
        self.locate_2.setObjectName("locate_2")
        self.horizontalLayout_6.addWidget(self.locate_2)
        self.LocationLayout.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LocationLayout.addItem(spacerItem6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"font-weight : 600;\n"
"font-family : \'Dosis\';\n"
"font-size : 10pt;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.LocationLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.locate_3 = QtWidgets.QLineEdit(self.widget)
        self.locate_3.setStyleSheet("color : rgba(0, 0, 0, 240);\n"
"background-color : rgba(0, 0, 0, 0);\n"
"\n"
"font-size:8pt;\n"
"font-family : \'Dosis\';")
        self.locate_3.setObjectName("locate_3")
        self.horizontalLayout_7.addWidget(self.locate_3)
        self.LocationLayout.addLayout(self.horizontalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LocationLayout.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.LocationLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.Submit_button = QtWidgets.QPushButton(self.widget)
        self.Submit_button.setStyleSheet("color : rgb(255, 255, 255);\n"
"background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 185, 204, 255), stop:0.510989 rgba(224, 219, 177, 255), stop:1 rgba(148, 202, 228, 255));\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 14pt;\n"
"\n"
"border-radius : 16px;")
        self.Submit_button.setObjectName("Submit_button")
        self.horizontalLayout_3.addWidget(self.Submit_button)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem13, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem15, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Where?"))
        self.label_2.setText(_translate("Dialog", "Location 1:"))
        self.locate_1.setPlaceholderText(_translate("Dialog", "Location 1"))
        self.label_3.setText(_translate("Dialog", "Location 2:"))
        self.locate_2.setPlaceholderText(_translate("Dialog", "Locate 2"))
        self.label_4.setText(_translate("Dialog", "Location 3:"))
        self.locate_3.setPlaceholderText(_translate("Dialog", "Locate 3"))
        self.Submit_button.setText(_translate("Dialog", "Submit"))
