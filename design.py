# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadExecFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadExecFile.setGeometry(QtCore.QRect(770, 430, 271, 31))
        self.btnLoadExecFile.setObjectName("btnLoadExecFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 91, 16))
        self.label.setObjectName("label")
        self.lblType = QtWidgets.QLabel(self.centralwidget)
        self.lblType.setGeometry(QtCore.QRect(370, 20, 41, 16))
        self.lblType.setObjectName("lblType")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(370, 40, 61, 16))
        self.lblName.setObjectName("lblName")
        self.lblExecFileHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblExecFileHeader.setGeometry(QtCore.QRect(770, 410, 101, 16))
        self.lblExecFileHeader.setObjectName("lblExecFileHeader")
        self.lblExecFile = QtWidgets.QLabel(self.centralwidget)
        self.lblExecFile.setGeometry(QtCore.QRect(870, 410, 171, 16))
        self.lblExecFile.setText("")
        self.lblExecFile.setObjectName("lblExecFile")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 510, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lblInputTest = QtWidgets.QLabel(self.centralwidget)
        self.lblInputTest.setGeometry(QtCore.QRect(850, 510, 191, 16))
        self.lblInputTest.setText("")
        self.lblInputTest.setObjectName("lblInputTest")
        self.nameMethod = QtWidgets.QTextEdit(self.centralwidget)
        self.nameMethod.setGeometry(QtCore.QRect(430, 40, 221, 21))
        self.nameMethod.setObjectName("nameMethod")
        self.btnLoadInputTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadInputTest.setGeometry(QtCore.QRect(770, 530, 271, 31))
        self.btnLoadInputTest.setObjectName("btnLoadInputTest")
        self.btnNextMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnNextMethod.setGeometry(QtCore.QRect(360, 300, 31, 31))
        self.btnNextMethod.setText("")
        self.btnNextMethod.setObjectName("btnNextMethod")
        self.btnPrevMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevMethod.setGeometry(QtCore.QRect(360, 330, 31, 31))
        self.btnPrevMethod.setText("")
        self.btnPrevMethod.setObjectName("btnPrevMethod")
        self.btnDelThisMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelThisMethod.setGeometry(QtCore.QRect(360, 240, 141, 31))
        self.btnDelThisMethod.setObjectName("btnDelThisMethod")
        self.btnDelAllMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelAllMethod.setGeometry(QtCore.QRect(510, 240, 141, 31))
        self.btnDelAllMethod.setObjectName("btnDelAllMethod")
        self.lblNextMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblNextMethod.setGeometry(QtCore.QRect(410, 300, 161, 31))
        self.lblNextMethod.setObjectName("lblNextMethod")
        self.lblPrevMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblPrevMethod.setGeometry(QtCore.QRect(410, 330, 161, 31))
        self.lblPrevMethod.setObjectName("lblPrevMethod")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 280, 91, 16))
        self.label_12.setObjectName("label_12")
        self.lblThisMethod = QtWidgets.QLabel(self.centralwidget)
        self.lblThisMethod.setGeometry(QtCore.QRect(450, 280, 161, 16))
        self.lblThisMethod.setObjectName("lblThisMethod")
        self.btnCalcThisMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcThisMethod.setGeometry(QtCore.QRect(920, 370, 291, 31))
        self.btnCalcThisMethod.setObjectName("btnCalcThisMethod")
        self.btnSaveTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveTest.setGeometry(QtCore.QRect(770, 0, 161, 31))
        self.btnSaveTest.setObjectName("btnSaveTest")
        self.btnSaveResByte = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveResByte.setGeometry(QtCore.QRect(190, 0, 101, 31))
        self.btnSaveResByte.setObjectName("btnSaveResByte")
        self.btnCalcTo = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcTo.setGeometry(QtCore.QRect(1030, 640, 131, 23))
        self.btnCalcTo.setObjectName("btnCalcTo")
        self.spnToMethod = QtWidgets.QSpinBox(self.centralwidget)
        self.spnToMethod.setGeometry(QtCore.QRect(1160, 640, 41, 22))
        self.spnToMethod.setMaximum(999999999)
        self.spnToMethod.setObjectName("spnToMethod")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(660, 10, 101, 16))
        self.label_15.setObjectName("label_15")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(1050, 540, 161, 23))
        self.btnExit.setObjectName("btnExit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1050, 400, 131, 21))
        self.label_16.setObjectName("label_16")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1110, 420, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1050, 440, 61, 16))
        self.label_5.setObjectName("label_5")
        self.lblMsg = QtWidgets.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(1050, 460, 161, 16))
        self.lblMsg.setText("")
        self.lblMsg.setObjectName("lblMsg")
        self.btnAddMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMethod.setGeometry(QtCore.QRect(360, 200, 51, 41))
        self.btnAddMethod.setText("")
        self.btnAddMethod.setObjectName("btnAddMethod")
        self.cmbMethods = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMethods.setGeometry(QtCore.QRect(430, 20, 221, 22))
        self.cmbMethods.setObjectName("cmbMethods")
        self.tblInutTest = QtWidgets.QTableWidget(self.centralwidget)
        self.tblInutTest.setGeometry(QtCore.QRect(10, 30, 341, 331))
        self.tblInutTest.setObjectName("tblInutTest")
        self.tblInutTest.setColumnCount(0)
        self.tblInutTest.setRowCount(0)
        self.tblRes = QtWidgets.QTableWidget(self.centralwidget)
        self.tblRes.setGeometry(QtCore.QRect(660, 30, 551, 331))
        self.tblRes.setObjectName("tblRes")
        self.tblRes.setColumnCount(0)
        self.tblRes.setRowCount(0)
        self.btnLoadResFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadResFile.setGeometry(QtCore.QRect(770, 480, 271, 31))
        self.btnLoadResFile.setObjectName("btnLoadResFile")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 460, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lblResFile = QtWidgets.QLabel(self.centralwidget)
        self.lblResFile.setGeometry(QtCore.QRect(880, 460, 161, 16))
        self.lblResFile.setText("")
        self.lblResFile.setObjectName("lblResFile")
        self.spnTimeWait = QtWidgets.QSpinBox(self.centralwidget)
        self.spnTimeWait.setGeometry(QtCore.QRect(570, 70, 81, 22))
        self.spnTimeWait.setMaximum(999999999)
        self.spnTimeWait.setObjectName("spnTimeWait")
        self.lblTimeWait = QtWidgets.QLabel(self.centralwidget)
        self.lblTimeWait.setGeometry(QtCore.QRect(360, 70, 211, 21))
        self.lblTimeWait.setObjectName("lblTimeWait")
        self.lblBytes = QtWidgets.QLabel(self.centralwidget)
        self.lblBytes.setGeometry(QtCore.QRect(360, 100, 291, 21))
        self.lblBytes.setObjectName("lblBytes")
        self.tblChgTest = QtWidgets.QTableWidget(self.centralwidget)
        self.tblChgTest.setGeometry(QtCore.QRect(10, 370, 651, 191))
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
        self.btnAddStrEditTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddStrEditTest.setGeometry(QtCore.QRect(670, 370, 41, 31))
        self.btnAddStrEditTest.setText("")
        self.btnAddStrEditTest.setObjectName("btnAddStrEditTest")
        self.prgExec = QtWidgets.QProgressBar(self.centralwidget)
        self.prgExec.setGeometry(QtCore.QRect(1050, 520, 171, 20))
        self.prgExec.setProperty("value", 0)
        self.prgExec.setObjectName("prgExec")
        self.btnChgAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnChgAll.setGeometry(QtCore.QRect(670, 410, 91, 31))
        self.btnChgAll.setObjectName("btnChgAll")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1050, 480, 71, 16))
        self.label_19.setObjectName("label_19")
        self.lblExecuteProc = QtWidgets.QLabel(self.centralwidget)
        self.lblExecuteProc.setGeometry(QtCore.QRect(1050, 500, 171, 16))
        self.lblExecuteProc.setText("")
        self.lblExecuteProc.setObjectName("lblExecuteProc")
        self.btnOpenInputData = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenInputData.setGeometry(QtCore.QRect(110, 0, 81, 31))
        self.btnOpenInputData.setObjectName("btnOpenInputData")
        self.btnOpenResData = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenResData.setGeometry(QtCore.QRect(930, 0, 81, 31))
        self.btnOpenResData.setObjectName("btnOpenResData")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(770, 390, 91, 16))
        self.label_20.setObjectName("label_20")
        self.btnClearChgAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearChgAll.setGeometry(QtCore.QRect(670, 490, 91, 31))
        self.btnClearChgAll.setObjectName("btnClearChgAll")
        self.btnFindChgAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnFindChgAll.setGeometry(QtCore.QRect(670, 530, 91, 31))
        self.btnFindChgAll.setObjectName("btnFindChgAll")
        self.btnStartAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartAll.setGeometry(QtCore.QRect(670, 450, 91, 31))
        self.btnStartAll.setObjectName("btnStartAll")
        self.lblStartAllPos = QtWidgets.QLabel(self.centralwidget)
        self.lblStartAllPos.setGeometry(QtCore.QRect(360, 110, 291, 21))
        self.lblStartAllPos.setObjectName("lblStartAllPos")
        self.lblToCount = QtWidgets.QLabel(self.centralwidget)
        self.lblToCount.setGeometry(QtCore.QRect(360, 150, 291, 21))
        self.lblToCount.setObjectName("lblToCount")
        self.txtPosStart = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPosStart.setGeometry(QtCore.QRect(360, 130, 291, 21))
        self.txtPosStart.setObjectName("txtPosStart")
        self.txtPosEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPosEnd.setGeometry(QtCore.QRect(360, 170, 291, 21))
        self.txtPosEnd.setObjectName("txtPosEnd")
        self.btnEditMethod = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditMethod.setGeometry(QtCore.QRect(420, 200, 51, 41))
        self.btnEditMethod.setText("")
        self.btnEditMethod.setObjectName("btnEditMethod")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1050, 420, 61, 21))
        self.label_18.setObjectName("label_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ данных"))
        self.btnLoadExecFile.setText(_translate("MainWindow", "Загрузить исполняемый файл"))
        self.label.setText(_translate("MainWindow", "Добавить метод:"))
        self.lblType.setText(_translate("MainWindow", "Тип:"))
        self.lblName.setText(_translate("MainWindow", "Название:"))
        self.lblExecFileHeader.setText(_translate("MainWindow", "Исполняемый файл:"))
        self.label_6.setText(_translate("MainWindow", "Входной тест:"))
        self.btnLoadInputTest.setText(_translate("MainWindow", "Загрузить тест"))
        self.btnDelThisMethod.setText(_translate("MainWindow", ""))
        self.btnDelAllMethod.setText(_translate("MainWindow", ""))
        self.lblNextMethod.setText(_translate("MainWindow", "NO"))
        self.lblPrevMethod.setText(_translate("MainWindow", "NO"))
        self.label_12.setText(_translate("MainWindow", "Текущий метод:"))
        self.lblThisMethod.setText(_translate("MainWindow", "NO"))
        self.btnCalcThisMethod.setText(_translate("MainWindow", ""))
        self.btnSaveTest.setText(_translate("MainWindow", "Сохранить результат"))
        self.btnSaveResByte.setText(_translate("MainWindow", "Сохранить тест"))
        self.btnCalcTo.setText(_translate("MainWindow", "Вычислить до метода:"))
        self.label_14.setText(_translate("MainWindow", "Входные данные:"))
        self.label_15.setText(_translate("MainWindow", "Выходные данные:"))
        self.btnExit.setText(_translate("MainWindow", "Выход"))
        self.label_16.setText(_translate("MainWindow", "Время выполнения теста"))
        self.label_5.setText(_translate("MainWindow", "Сообщение:"))
        self.btnLoadResFile.setText(_translate("MainWindow", "Загрузить результирующий файл"))
        self.label_7.setText(_translate("MainWindow", "Файл с результатом:"))
        self.lblTimeWait.setText(_translate("MainWindow", "Максимальное время ожидания потока:"))
        self.lblBytes.setText(_translate("MainWindow", "<html><head/><body><p>Байты проверки (с последним)</p><p><br/></p></body></html>"))
        item = self.tblChgTest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Адрес байта"))
        item = self.tblChgTest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Содержимое"))
        item = self.tblChgTest.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Готово"))
        item = self.tblChgTest.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Начальное"))
        item = self.tblChgTest.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Поиск по адресу"))
        item = self.tblChgTest.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Убрать"))
        self.btnChgAll.setText(_translate("MainWindow", ""))
        self.label_19.setText(_translate("MainWindow", "Выполнение:"))
        self.btnOpenInputData.setText(_translate("MainWindow", "Развернуть"))
        self.btnOpenResData.setText(_translate("MainWindow", "Развернуть"))
        self.label_20.setText(_translate("MainWindow", "Добавить Файлы:"))
        self.btnClearChgAll.setText(_translate("MainWindow", ""))
        self.btnFindChgAll.setText(_translate("MainWindow", ""))
        self.btnStartAll.setText(_translate("MainWindow", ""))
        self.lblStartAllPos.setText(_translate("MainWindow", "с"))
        self.lblToCount.setText(_translate("MainWindow", "по"))
        self.label_18.setText(_translate("MainWindow", "(секунды):"))


