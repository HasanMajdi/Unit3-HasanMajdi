# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Equitable.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Equi_Table(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(576, 317)
        self.Table_Eq = QtWidgets.QTableWidget(Dialog)
        self.Table_Eq.setGeometry(QtCore.QRect(20, 50, 541, 201))
        self.Table_Eq.setObjectName("Table_Eq")
        self.Table_Eq.setColumnCount(9)
        self.Table_Eq.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Eq.setItem(0, 0, item)
        self.Confirm_Eq = QtWidgets.QPushButton(Dialog)
        self.Confirm_Eq.setGeometry(QtCore.QRect(440, 260, 131, 32))
        self.Confirm_Eq.setStyleSheet("color: rgb(145, 30, 33);")
        self.Confirm_Eq.setDefault(True)
        self.Confirm_Eq.setObjectName("Confirm_Eq")
        self.Revert_Eq = QtWidgets.QPushButton(Dialog)
        self.Revert_Eq.setGeometry(QtCore.QRect(300, 260, 131, 32))
        self.Revert_Eq.setStyleSheet("color: rgb(145, 30, 33);")
        self.Revert_Eq.setAutoDefault(True)
        self.Revert_Eq.setDefault(True)
        self.Revert_Eq.setObjectName("Revert_Eq")
        self.Back_Eq = QtWidgets.QPushButton(Dialog)
        self.Back_Eq.setGeometry(QtCore.QRect(10, 10, 61, 32))
        self.Back_Eq.setObjectName("Back_Eq")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.Table_Eq.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "ITEMS"))
        item = self.Table_Eq.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ITEMS"))
        item = self.Table_Eq.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "STORED"))
        item = self.Table_Eq.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "WHERE"))
        item = self.Table_Eq.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "WHO"))
        item = self.Table_Eq.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "EMAIL"))
        __sortingEnabled = self.Table_Eq.isSortingEnabled()
        self.Table_Eq.setSortingEnabled(False)
        self.Table_Eq.setSortingEnabled(__sortingEnabled)
        self.Confirm_Eq.setText(_translate("Dialog", "Confirm Changes"))
        self.Revert_Eq.setText(_translate("Dialog", "Revert Changes"))
        self.Back_Eq.setText(_translate("Dialog", "BACK"))
