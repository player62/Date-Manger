from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(223, 95, 159, 200), stop:0.513812 rgba(224, 212, 107, 200), stop:1 rgba(103, 188, 228, 200))")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(230, 0, 230, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius : 10px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.DateManager = QtWidgets.QLabel(self.widget)
        self.DateManager.setStyleSheet("color : rgb(0, 0, 0);\n"
"background-color : rgba(255, 255, 255, 0);\n"
"\n"
"font-family : \'Colonna MT\';\n"
"font-weight : bold;\n"
"font-size : 40pt; ")
        self.DateManager.setObjectName("DateManager")
        self.gridLayout_4.addWidget(self.DateManager, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.HowMany = QtWidgets.QLabel(self.widget_2)
        self.HowMany.setStyleSheet("font-family : \'Dosis\';\n"
"\n"
"font-size : 12pt;")
        self.HowMany.setObjectName("HowMany")
        self.horizontalLayout_6.addWidget(self.HowMany)
        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.member = QtWidgets.QSlider(self.widget_2)
        self.member.setMinimum(1)
        self.member.setMaximum(6)
        self.member.setOrientation(QtCore.Qt.Horizontal)
        self.member.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.member.setObjectName("member")
        self.horizontalLayout_6.addWidget(self.member)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.start_button = QtWidgets.QPushButton(self.widget_2)
        self.start_button.setStyleSheet("color : rgb(255, 255, 255);\n"
"background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 185, 204, 255), stop:0.510989 rgba(224, 219, 177, 255), stop:1 rgba(148, 202, 228, 255));\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 14pt;\n"
"\n"
"border-radius : 16px;")
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_5.addWidget(self.start_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(3, 5)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 270, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem8, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 270, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem9, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DateManager.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Date</p><p align=\"center\">Manager</p></body></html>"))
        self.HowMany.setText(_translate("Dialog", "How Many?"))
        self.start_button.setText(_translate("Dialog", "Ready To Date?"))
