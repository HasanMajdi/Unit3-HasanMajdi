# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(661, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Dashbiard = QtWidgets.QPushButton(self.centralwidget)
        self.Dashbiard.setGeometry(QtCore.QRect(10, 30, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Didot")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Dashbiard.setFont(font)
        self.Dashbiard.setStyleSheet("color: rgb(168, 12, 34);\n"
                                     "font: 13pt \"Menlo\";\n"
                                     "font: italic 13pt \"rgb(252, 64, 69)\";\n"
                                     "font: 13pt \"Didot\";")
        self.Dashbiard.setObjectName("Dashbiard")
        self.Users_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Users_btn.setGeometry(QtCore.QRect(10, 80, 113, 32))
        self.Users_btn.setStyleSheet("color: rgb(252, 55, 60);\n"
                                 "color: rgb(143, 30, 44);\n"
                                 "font: 13pt \"Didot\";")
        self.Users_btn.setObjectName("Users")
        self.Equipments = QtWidgets.QPushButton(self.centralwidget)
        self.Equipments.setGeometry(QtCore.QRect(10, 130, 113, 32))
        self.Equipments.setStyleSheet("\n"
                                      "font: 13pt \"Didot\";\n"
                                      "color: rgb(136, 23, 35);")
        self.Equipments.setObjectName("Equipments")
        self.Setting = QtWidgets.QPushButton(self.centralwidget)
        self.Setting.setGeometry(QtCore.QRect(10, 180, 113, 32))
        self.Setting.setStyleSheet("font: 13pt \"Didot\";\n"
                                   "color: rgb(112, 28, 38);")
        self.Setting.setObjectName("Setting")
        self.Tabl_Items = QtWidgets.QTableWidget(self.centralwidget)
        self.Tabl_Items.setGeometry(QtCore.QRect(140, 80, 431, 201))
        self.Tabl_Items.setObjectName("Tabl_Items")
        self.Tabl_Items.setColumnCount(6)
        self.Tabl_Items.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabl_Items.setItem(0, 0, item)
        self.Title_Main = QtWidgets.QLabel(self.centralwidget)
        self.Title_Main.setGeometry(QtCore.QRect(190, 0, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_Main.setFont(font)
        self.Title_Main.setStyleSheet("color: rgb(252, 24, 31);\n"
                                      "font: 48pt \"Georgia\";")
        self.Title_Main.setObjectName("Title_Main")
        self.Confirm_Main = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_Main.setGeometry(QtCore.QRect(510, 310, 131, 32))
        self.Confirm_Main.setStyleSheet("color: rgb(145, 30, 33);")
        self.Confirm_Main.setAutoDefault(True)
        self.Confirm_Main.setDefault(True)
        self.Confirm_Main.setFlat(False)
        self.Confirm_Main.setObjectName("Confirm_Main")
        self.Revert_Main = QtWidgets.QPushButton(self.centralwidget)
        self.Revert_Main.setGeometry(QtCore.QRect(370, 310, 131, 32))
        self.Revert_Main.setStyleSheet("color: rgb(145, 30, 33);")
        self.Revert_Main.setAutoDefault(True)
        self.Revert_Main.setDefault(True)
        self.Revert_Main.setFlat(False)
        self.Revert_Main.setObjectName("Revert_Main")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Dashbiard.setText(_translate("MainWindow", "Dashboard "))
        self.Users_btn.setText(_translate("MainWindow", "Users"))
        self.Equipments.setText(_translate("MainWindow", "Equipments "))
        self.Setting.setText(_translate("MainWindow", "Setting"))
        item = self.Tabl_Items.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.Tabl_Items.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "News"))
        __sortingEnabled = self.Tabl_Items.isSortingEnabled()
        self.Tabl_Items.setSortingEnabled(False)
        self.Tabl_Items.setSortingEnabled(__sortingEnabled)
        self.Title_Main.setText(_translate("MainWindow", "OEd Inventory "))
        self.Confirm_Main.setText(_translate("MainWindow", "Confirm Changes"))
        self.Revert_Main.setText(_translate("MainWindow", "Revert Changes"))
