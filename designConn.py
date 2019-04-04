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
        Dialog.resize(311, 402)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 310, 221, 20))
        self.label.setObjectName("label")
        self.lbl0 = QtWidgets.QLabel(Dialog)
        self.lbl0.setGeometry(QtCore.QRect(50, 30, 221, 17))
        self.lbl0.setObjectName("lbl0")
        self.lbl1 = QtWidgets.QLabel(Dialog)
        self.lbl1.setGeometry(QtCore.QRect(50, 70, 221, 17))
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(Dialog)
        self.lbl2.setGeometry(QtCore.QRect(50, 120, 221, 17))
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(Dialog)
        self.lbl3.setGeometry(QtCore.QRect(50, 170, 221, 17))
        self.lbl3.setObjectName("lbl3")
        self.lbl4 = QtWidgets.QLabel(Dialog)
        self.lbl4.setGeometry(QtCore.QRect(50, 220, 221, 17))
        self.lbl4.setObjectName("lbl4")
        self.btnTestConn = QtWidgets.QPushButton(Dialog)
        self.btnTestConn.setGeometry(QtCore.QRect(170, 270, 101, 31))
        self.btnTestConn.setObjectName("btnTestConn")
        self.btnExit = QtWidgets.QPushButton(Dialog)
        self.btnExit.setGeometry(QtCore.QRect(170, 360, 101, 31))
        self.btnExit.setObjectName("btnExit")
        self.spn4 = QtWidgets.QSpinBox(Dialog)
        self.spn4.setGeometry(QtCore.QRect(50, 240, 221, 26))
        self.spn4.setMaximum(999999999)
        self.spn4.setObjectName("spn4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 10, 181, 17))
        self.label_7.setObjectName("label_7")
        self.lblState = QtWidgets.QLabel(Dialog)
        self.lblState.setGeometry(QtCore.QRect(60, 330, 211, 17))
        self.lblState.setObjectName("lblState")
        self.txt3 = QtWidgets.QPlainTextEdit(Dialog)
        self.txt3.setGeometry(QtCore.QRect(50, 190, 221, 21))
        self.txt3.setObjectName("txt3")
        self.txt2 = QtWidgets.QPlainTextEdit(Dialog)
        self.txt2.setGeometry(QtCore.QRect(50, 140, 221, 21))
        self.txt2.setObjectName("txt2")
        self.txt1 = QtWidgets.QPlainTextEdit(Dialog)
        self.txt1.setGeometry(QtCore.QRect(50, 90, 221, 21))
        self.txt1.setObjectName("txt1")
        self.txt0 = QtWidgets.QPlainTextEdit(Dialog)
        self.txt0.setGeometry(QtCore.QRect(50, 50, 221, 21))
        self.txt0.setObjectName("txt0")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Состояние подключения:"))
        self.lbl0.setText(_translate("Dialog", "Название базы"))
        self.lbl1.setText(_translate("Dialog", "Пользователь базы"))
        self.lbl2.setText(_translate("Dialog", "Пароль к базе"))
        self.lbl3.setText(_translate("Dialog", "Хост базы"))
        self.lbl4.setText(_translate("Dialog", "Порт базы"))
        self.btnTestConn.setText(_translate("Dialog", "Проверить"))
        self.btnExit.setText(_translate("Dialog", "Выйти"))
        self.label_7.setText(_translate("Dialog", "Проверка подключения"))
        self.lblState.setText(_translate("Dialog", "не проверено"))


