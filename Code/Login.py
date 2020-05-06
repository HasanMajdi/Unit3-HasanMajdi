# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.Fin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_login(QDialog):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(485, 368)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(173, 255, 15);\n"
"}\n"
"\n"
"#lineEdit{\n"
"border: 1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.Username = QtWidgets.QLineEdit(Dialog)
        self.Username.setGeometry(QtCore.QRect(150, 140, 201, 31))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(Dialog)
        self.Password.setGeometry(QtCore.QRect(150, 200, 201, 31))
        self.Password.setObjectName("Password")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(190, 260, 121, 41))
        self.login_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(252, 59, 97);\n"
"background-color: rgb(17, 79, 234);")
        self.login_btn.setObjectName("login_btn")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(90, -10, 331, 121))
        self.Title.setStyleSheet("color: rgb(252, 24, 31);\n"
"font: 48pt \"Georgia\";")
        self.Title.setObjectName("Title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Username.setPlaceholderText(_translate("Dialog", "email"))
        self.Password.setPlaceholderText(_translate("Dialog", "password"))
        self.login_btn.setText(_translate("Dialog", "Log In"))
        self.Title.setText(_translate("Dialog", "OEd Inventory "))
