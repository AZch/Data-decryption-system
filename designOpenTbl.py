# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designOpenTbl.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_openTbl(object):
    def setupUi(self, openTbl):
        openTbl.setObjectName("openTbl")
        openTbl.resize(823, 682)
        self.tblData = QtWidgets.QTableWidget(openTbl)
        self.tblData.setGeometry(QtCore.QRect(0, 10, 821, 431))
        self.tblData.setObjectName("tblData")
        self.tblData.setColumnCount(0)
        self.tblData.setRowCount(0)
        self.btnUpdTbl = QtWidgets.QPushButton(openTbl)
        self.btnUpdTbl.setGeometry(QtCore.QRect(580, 450, 111, 23))
        self.btnUpdTbl.setObjectName("btnUpdTbl")
        self.btnExit = QtWidgets.QPushButton(openTbl)
        self.btnExit.setGeometry(QtCore.QRect(700, 650, 121, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnClearChgAll = QtWidgets.QPushButton(openTbl)
        self.btnClearChgAll.setGeometry(QtCore.QRect(750, 570, 71, 31))
        self.btnClearChgAll.setText("")
        self.btnClearChgAll.setObjectName("btnClearChgAll")
        self.btnFindChgAll = QtWidgets.QPushButton(openTbl)
        self.btnFindChgAll.setGeometry(QtCore.QRect(750, 610, 71, 31))
        self.btnFindChgAll.setText("")
        self.btnFindChgAll.setObjectName("btnFindChgAll")
        self.btnChgAll = QtWidgets.QPushButton(openTbl)
        self.btnChgAll.setGeometry(QtCore.QRect(750, 490, 71, 31))
        self.btnChgAll.setText("")
        self.btnChgAll.setObjectName("btnChgAll")
        self.btnStartAll = QtWidgets.QPushButton(openTbl)
        self.btnStartAll.setGeometry(QtCore.QRect(750, 530, 71, 31))
        self.btnStartAll.setText("")
        self.btnStartAll.setObjectName("btnStartAll")
        self.btnAddStrEditTest = QtWidgets.QPushButton(openTbl)
        self.btnAddStrEditTest.setGeometry(QtCore.QRect(750, 450, 41, 31))
        self.btnAddStrEditTest.setText("")
        self.btnAddStrEditTest.setObjectName("btnAddStrEditTest")
        self.tblChgTest = QtWidgets.QTableWidget(openTbl)
        self.tblChgTest.setGeometry(QtCore.QRect(0, 450, 741, 191))
        self.tblChgTest.setObjectName("tblChgTest")
        self.tblChgTest.setColumnCount(6)
        self.tblChgTest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblChgTest.setHorizontalHeaderItem(5, item)
        self.lblMsg = QtWidgets.QLabel(openTbl)
        self.lblMsg.setGeometry(QtCore.QRect(10, 656, 681, 21))
        self.lblMsg.setText("")
        self.lblMsg.setObjectName("lblMsg")

        self.retranslateUi(openTbl)
        QtCore.QMetaObject.connectSlotsByName(openTbl)

    def retranslateUi(self, openTbl):
        _translate = QtCore.QCoreApplication.translate
        openTbl.setWindowTitle(_translate("openTbl", "Dialog"))
        self.btnUpdTbl.setText(_translate("openTbl", "Обновить"))
        self.btnExit.setText(_translate("openTbl", "Закрыть"))
        item = self.tblChgTest.horizontalHeaderItem(0)
        item.setText(_translate("openTbl", "Адрес байта"))
        item = self.tblChgTest.horizontalHeaderItem(1)
        item.setText(_translate("openTbl", "Содержимое"))
        item = self.tblChgTest.horizontalHeaderItem(2)
        item.setText(_translate("openTbl", "Готово"))
        item = self.tblChgTest.horizontalHeaderItem(3)
        item.setText(_translate("openTbl", "Начальное"))
        item = self.tblChgTest.horizontalHeaderItem(4)
        item.setText(_translate("openTbl", "Поиск по адресу"))
        item = self.tblChgTest.horizontalHeaderItem(5)
        item.setText(_translate("openTbl", "Убрать"))


