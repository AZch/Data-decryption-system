# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designOpenTbl.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_openTbl(object):
    def setupUi(self, openTbl):
        openTbl.setObjectName("openTbl")
        openTbl.resize(861, 484)
        self.tblData = QtWidgets.QTableWidget(openTbl)
        self.tblData.setGeometry(QtCore.QRect(10, 10, 841, 431))
        self.tblData.setObjectName("tblData")
        self.tblData.setColumnCount(0)
        self.tblData.setRowCount(0)
        self.btnUpdTbl = QtWidgets.QPushButton(openTbl)
        self.btnUpdTbl.setGeometry(QtCore.QRect(590, 450, 111, 23))
        self.btnUpdTbl.setObjectName("btnUpdTbl")
        self.btnExit = QtWidgets.QPushButton(openTbl)
        self.btnExit.setGeometry(QtCore.QRect(740, 450, 111, 23))
        self.btnExit.setObjectName("btnExit")

        self.retranslateUi(openTbl)
        QtCore.QMetaObject.connectSlotsByName(openTbl)

    def retranslateUi(self, openTbl):
        _translate = QtCore.QCoreApplication.translate
        openTbl.setWindowTitle(_translate("openTbl", "Dialog"))
        self.btnUpdTbl.setText(_translate("openTbl", "Обновить"))
        self.btnExit.setText(_translate("openTbl", "Выйти"))

