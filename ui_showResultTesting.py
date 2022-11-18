from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 900)
        Dialog.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(223, 95, 159, 200), stop:0.513812 rgba(224, 212, 107, 200), stop:1 rgba(103, 188, 228, 200))")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
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
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setStyleSheet("font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 10pt;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.result_table_1 = QtWidgets.QTableWidget(self.tab)
        self.result_table_1.setStyleSheet("border : 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 185, 204, 255), stop:0.510989 rgba(224, 219, 177, 255), stop:1 rgba(148, 202, 228, 255));\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 10pt;\n"
"\n"
"border-radius : 12px;")
        self.result_table_1.setObjectName("result_table_1")
        self.result_table_1.setColumnCount(0)
        self.result_table_1.setRowCount(0)
        self.gridLayout_4.addWidget(self.result_table_1, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.result_table_2 = QtWidgets.QTableWidget(self.tab_2)
        self.result_table_2.setObjectName("result_table_2")
        self.result_table_2.setColumnCount(0)
        self.result_table_2.setRowCount(0)
        self.gridLayout_6.addWidget(self.result_table_2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.result_table_3 = QtWidgets.QTableWidget(self.tab_3)
        self.result_table_3.setObjectName("result_table_3")
        self.result_table_3.setColumnCount(0)
        self.result_table_3.setRowCount(0)
        self.gridLayout_8.addWidget(self.result_table_3, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.loadData_button = QtWidgets.QPushButton(self.widget)
        self.loadData_button.setStyleSheet("color : rgb(255, 255, 255);\n"
"background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 185, 204, 255), stop:0.510989 rgba(224, 219, 177, 255), stop:1 rgba(148, 202, 228, 255));\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 14pt;\n"
"\n"
"border-radius : 16px;")
        self.loadData_button.setObjectName("loadData_button")
        self.horizontalLayout.addWidget(self.loadData_button)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.save_image_button = QtWidgets.QPushButton(self.widget)
        self.save_image_button.setStyleSheet("color : rgb(255, 255, 255);\n"
"background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(223, 185, 204, 255), stop:0.510989 rgba(224, 219, 177, 255), stop:1 rgba(148, 202, 228, 255));\n"
"\n"
"font-family : \'Dosis\';\n"
"font-weight : bold;\n"
"font-size : 14pt;\n"
"\n"
"border-radius : 16px;")
        self.save_image_button.setObjectName("save_image_button")
        self.horizontalLayout.addWidget(self.save_image_button)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Location 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Location 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Location3"))
        self.loadData_button.setText(_translate("Dialog", "Load Data"))
        self.save_image_button.setText(_translate("Dialog", "Save as Image"))
