# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadExecFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadExecFile.setGeometry(QtCore.QRect(260, 30, 231, 23))
        self.btnLoadExecFile.setObjectName("btnLoadExecFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.label_4.setObjectName("label_4")
        self.lblExecFile = QtWidgets.QLabel(self.centralwidget)
        self.lblExecFile.setGeometry(QtCore.QRect(360, 10, 131, 20))
        self.lblExecFile.setText("")
        self.lblExecFile.setObjectName("lblExecFile")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 10, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lblInputTest = QtWidgets.QLabel(self.centralwidget)
        self.lblInputTest.setGeometry(QtCore.QRect(570, 10, 121, 20))
        self.lblInputTest.setText("")
        self.lblInputTest.setObjectName("lblInputTest")
        self.nameMethod = QtWidgets.QTextEdit(self.centralwidget)
        self.nameMethod.setGeometry(QtCore.QRect(160, 30, 91, 21))
        self.nameMethod.setObjectName("nameMethod")
        self.btnLoadInputTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadInputTest.setGeometry(QtCore.QRect(490, 30, 201, 23))
        self.btnLoadInputTest.setObjectName("btnLoadInputTest")
        self.txtInputTest = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtInputTest.setGeometry(QtCore.QRect(20, 190, 251, 221))
        self.txtInputTest.setObjectName("txtInputTest")
        self.tblRes = QtWidgets.QTableView(self.centralwidget)
        self.tblRes.setGeometry(QtCore.QRect(280, 190, 491, 221))
        self.tblRes.setObjectName("tblRes")
        self.btnNextMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextMethod.setGeometry(QtCore.QRect(20, 60, 161, 23))
        self.btnNextMethod.setObjectName("btnNextMethod")
        self.btnPrevMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevMethod.setGeometry(QtCore.QRect(190, 60, 161, 23))
        self.btnPrevMethod.setObjectName("btnPrevMethod")
        self.btnDelThisMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelThisMethod.setGeometry(QtCore.QRect(360, 60, 191, 23))
        self.btnDelThisMethod.setObjectName("btnDelThisMethod")
        self.btnDelAllMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelAllMethod.setGeometry(QtCore.QRect(360, 80, 191, 23))
        self.btnDelAllMethod.setObjectName("btnDelAllMethod")
        self.btnSaveThisMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveThisMethod.setGeometry(QtCore.QRect(560, 60, 211, 23))
        self.btnSaveThisMethod.setObjectName("btnSaveThisMethod")
        self.btnSaveAllMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveAllMethod.setGeometry(QtCore.QRect(560, 80, 211, 23))
        self.btnSaveAllMethod.setObjectName("btnSaveAllMethod")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label_8.setObjectName("label_8")
        self.lblNextMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblNextMethod.setGeometry(QtCore.QRect(60, 90, 121, 16))
        self.lblNextMethod.setText("")
        self.lblNextMethod.setObjectName("lblNextMethod")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 90, 47, 13))
        self.label_10.setObjectName("label_10")
        self.lblPrevMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblPrevMethod.setGeometry(QtCore.QRect(230, 90, 121, 16))
        self.lblPrevMethod.setText("")
        self.lblPrevMethod.setObjectName("lblPrevMethod")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_12.setObjectName("label_12")
        self.lblThisMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblThisMethod.setGeometry(QtCore.QRect(110, 120, 241, 16))
        self.lblThisMethod.setText("")
        self.lblThisMethod.setObjectName("lblThisMethod")
        self.btnCalcThisMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcThisMethod.setGeometry(QtCore.QRect(360, 120, 191, 23))
        self.btnCalcThisMethod.setObjectName("btnCalcThisMethod")
        self.btnSaveTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveTest.setGeometry(QtCore.QRect(560, 120, 211, 23))
        self.btnSaveTest.setObjectName("btnSaveTest")
        self.btnSaveResByte = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveResByte.setGeometry(QtCore.QRect(560, 140, 211, 23))
        self.btnSaveResByte.setObjectName("btnSaveResByte")
        self.btnCalcTo = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcTo.setGeometry(QtCore.QRect(360, 140, 131, 23))
        self.btnCalcTo.setObjectName("btnCalcTo")
        self.spnToMethod = QtWidgets.QSpinBox(self.centralwidget)
        self.spnToMethod.setGeometry(QtCore.QRect(490, 140, 61, 22))
        self.spnToMethod.setMaximum(999999999)
        self.spnToMethod.setObjectName("spnToMethod")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(280, 170, 101, 16))
        self.label_15.setObjectName("label_15")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(700, 420, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 420, 201, 21))
        self.label_16.setObjectName("label_16")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 420, 61, 21))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 420, 61, 16))
        self.label_5.setObjectName("label_5")
        self.lblMsg = QtWidgets.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(350, 420, 341, 20))
        self.lblMsg.setText("")
        self.lblMsg.setObjectName("lblMsg")
        self.btnAddMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMethod.setGeometry(QtCore.QRect(700, 10, 75, 41))
        self.btnAddMethod.setObjectName("btnAddMethod")
        self.cmbMethods = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMethods.setGeometry(QtCore.QRect(60, 30, 91, 22))
        self.cmbMethods.setObjectName("cmbMethods")
        self.txtRes = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtRes.setGeometry(QtCore.QRect(280, 190, 491, 221))
        self.txtRes.setObjectName("txtRes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
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
        self.btnLoadExecFile.setText(_translate("MainWindow", "Загрузить исполняемый файл"))
        self.label.setText(_translate("MainWindow", "Добавить метод:"))
        self.label_2.setText(_translate("MainWindow", "Метод:"))
        self.label_3.setText(_translate("MainWindow", "Название:"))
        self.label_4.setText(_translate("MainWindow", "Исполняемый файл:"))
        self.label_6.setText(_translate("MainWindow", "Входной тест:"))
        self.btnLoadInputTest.setText(_translate("MainWindow", "Загрузить тест"))
        self.btnNextMethod.setText(_translate("MainWindow", "Следующий метод:"))
        self.btnPrevMethod.setText(_translate("MainWindow", "Предыдущий метод:"))
        self.btnDelThisMethod.setText(_translate("MainWindow", "Удалить текущий метод"))
        self.btnDelAllMethod.setText(_translate("MainWindow", "Удалить все методы"))
        self.btnSaveThisMethod.setText(_translate("MainWindow", "Сохранить этот метод"))
        self.btnSaveAllMethod.setText(_translate("MainWindow", "Сохранить все методы"))
        self.label_8.setText(_translate("MainWindow", "Метод:"))
        self.label_10.setText(_translate("MainWindow", "Метод:"))
        self.label_12.setText(_translate("MainWindow", "Текущий метод:"))
        self.btnCalcThisMethod.setText(_translate("MainWindow", "Вычислить"))
        self.btnSaveTest.setText(_translate("MainWindow", "Сохранить тест"))
        self.btnSaveResByte.setText(_translate("MainWindow", "Сохранить результат в тест"))
        self.btnCalcTo.setText(_translate("MainWindow", "Вычислить до метода:"))
        self.label_14.setText(_translate("MainWindow", "Входные данные:"))
        self.label_15.setText(_translate("MainWindow", "Выходные данные:"))
        self.btnExit.setText(_translate("MainWindow", "Выход"))
        self.label_16.setText(_translate("MainWindow", "Время выполнения теста (секунды):"))
        self.label_5.setText(_translate("MainWindow", "Сообщение:"))
        self.btnAddMethod.setText(_translate("MainWindow", "Добавить \n"
"метод"))

