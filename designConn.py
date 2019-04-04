# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designConn.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 380)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 310, 221, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 151, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 101, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 81, 17))
        self.label_6.setObjectName("label_6")
        self.btnTestConn = QtWidgets.QPushButton(Dialog)
        self.btnTestConn.setGeometry(QtCore.QRect(170, 270, 101, 31))
        self.btnTestConn.setObjectName("btnTestConn")
        self.btnExit = QtWidgets.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(170, 340, 101, 31))
        self.btnExit.setObjectName("btnExit")
        self.spnPort = QtWidgets.QSpinBox(Dialog)
        self.spnPort.setGeometry(QtCore.QRect(50, 240, 221, 26))
        self.spnPort.setObjectName("spnPort")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 10, 181, 17))
        self.label_7.setObjectName("label_7")
        self.lblState = QtWidgets.QLabel(Dialog)
        self.lblState.setGeometry(QtCore.QRect(50, 330, 221, 17))
        self.lblState.setText("")
        self.lblState.setObjectName("lblState")
        self.txtHost = QtWidgets.QPlainTextEdit(Dialog)
        self.txtHost.setGeometry(QtCore.QRect(50, 190, 221, 21))
        self.txtHost.setObjectName("txtHost")
        self.txtPsw = QtWidgets.QPlainTextEdit(Dialog)
        self.txtPsw.setGeometry(QtCore.QRect(50, 140, 221, 21))
        self.txtPsw.setObjectName("txtPsw")
        self.txtUser = QtWidgets.QPlainTextEdit(Dialog)
        self.txtUser.setGeometry(QtCore.QRect(50, 90, 221, 21))
        self.txtUser.setObjectName("txtUser")
        self.txtNameDB = QtWidgets.QPlainTextEdit(Dialog)
        self.txtNameDB.setGeometry(QtCore.QRect(50, 50, 221, 21))
        self.txtNameDB.setObjectName("txtNameDB")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Состояние подключения:"))
        self.label_2.setText(_translate("Dialog", "Название базы"))
        self.label_3.setText(_translate("Dialog", "Пользователь базы"))
        self.label_4.setText(_translate("Dialog", "Пароль к базе"))
        self.label_5.setText(_translate("Dialog", "Хост базы"))
        self.label_6.setText(_translate("Dialog", "Порт базы"))
        self.btnTestConn.setText(_translate("Dialog", "Проверить"))
        self.btnExit.setText(_translate("Dialog", "Выйти"))
        self.label_7.setText(_translate("Dialog", "Проверка подключения"))


