from PyQt5 import QtWidgets, QtGui, QtCore

import designOpenTbl
from Constants import *


class OpenTblWnd(QtWidgets.QDialog, designOpenTbl.Ui_openTbl):
    def __init__(self, tbl, isTest, parentClass):
        super(OpenTblWnd, self).__init__()
        self.setupUi(self)
        self.btnExit.clicked.connect(self.closeWnd)

        self.tblData.setColumnCount(tbl.columnCount())
        self.tblData.setRowCount(tbl.rowCount())
        for i in range(tbl.rowCount()):
            for j in range(tbl.columnCount()):
                self.tblData.setItem(i, j,
                                         QtWidgets.QTableWidgetItem(tbl.item(i, j)))
        #self.tblData.resizeColumnsToContents()
        self.parentClass = parentClass
        self.__initBtnImg()
        self.isTest = isTest
        if not isTest:
            self.tblChgTest.setEnabled(False)
            self.btnFindChgAll.setEnabled(False)
            self.btnStartAll.setEnabled(False)
            self.btnChgAll.setEnabled(False)
            self.btnClearChgAll.setEnabled(False)
            self.btnAddStrEditTest.setEnabled(False)
            self.tblData.setHorizontalHeaderLabels([
                StrConst.сolumnNameFun, StrConst.columnNameRes, StrConst.columnByte, StrConst.columnLocByte
            ])
            self.tblData.horizontalHeaderItem(0).setToolTip(StrConst.сolumnNameFun)
            self.tblData.horizontalHeaderItem(1).setToolTip(StrConst.columnNameRes)
            self.tblData.horizontalHeaderItem(2).setToolTip(StrConst.columnByte)
            self.tblData.horizontalHeaderItem(3).setToolTip(StrConst.columnLocByte)
            self.tblData.resizeColumnsToContents()
        else:
            self.btnAddStrEditTest.clicked.connect(self.addToThisTbl)
            self.btnClearChgAll.clicked.connect(self.chgClearAll)
            self.btnChgAll.clicked.connect(self.chgAll)
            self.btnStartAll.clicked.connect(self.chgStartAll)
            self.btnFindChgAll.clicked.connect(self.chgFindAll)
            self.updChgTbl(parentClass.dataChgVal)
        self.btnUpdTbl.setVisible(False)

    def __initBtnImg(self):
        identDiv = 10
        self.btnAddStrEditTest.setIcon(QtGui.QIcon(icons.addByteChange))
        self.btnAddStrEditTest.setIconSize(self.__getQSize(identDiv, self.btnAddStrEditTest))

        self.btnClearChgAll.setIcon(QtGui.QIcon(icons.delAllByteChanges))
        self.btnClearChgAll.setIconSize(self.__getQSize(identDiv, self.btnClearChgAll))

        # self.btnDelAllMethod.setIcon(QtGui.QIcon(icons.delAllMethods))
        self.btnChgAll.setIcon(QtGui.QIcon(icons.confirmAllByteChanges))
        self.btnChgAll.setIconSize(self.__getQSize(identDiv, self.btnChgAll))

        self.btnStartAll.setIcon(QtGui.QIcon(icons.startAllByteChanges))
        self.btnStartAll.setIconSize(self.__getQSize(identDiv, self.btnStartAll))

        self.btnFindChgAll.setIcon(QtGui.QIcon(icons.searchAllByteChanges))
        self.btnFindChgAll.setIconSize(self.__getQSize(identDiv, self.btnFindChgAll))

    def __getQSize(self, indentDiv, widget):
        return QtCore.QSize(widget.size().width() - widget.size().width() / indentDiv,
                         widget.size().height() - widget.size().height() / indentDiv
                        )

    def closeWnd(self):
        if self.isTest:
            rowChgTblCount = self.tblChgTest.rowCount()
            self.parentClass.dataChgVal = {}
            for i in range(rowChgTblCount):
                self.parentClass.dataChgVal[str(i)] = self.tblChgTest.cellWidget(i, 0).toPlainText() + \
                                                             "->" + self.tblChgTest.cellWidget(i, 1).toPlainText()
        self.close()

    ''' Добавление новых кнопок и полей для изменения входных данных '''
    def addToThisTbl(self):
        self.addStrToEditTest(self.tblChgTest)

    def addStrToEditTest(self, tbl):
        self.addWithStartData(tbl, "0", "00")

    def addWithStartData(self, tbl, posStr, byteStr):
        identDiv = 10
        rowPosition = tbl.rowCount()
        tbl.insertRow(rowPosition)

        # Поля для позиции
        txtEditPosition = QtWidgets.QTextEdit(tbl)
        txtEditPosition.setText(posStr)
        tbl.setCellWidget(rowPosition, 0, txtEditPosition)

        # Поле для нового значения
        txtEditNewVal = QtWidgets.QTextEdit(tbl)
        txtEditNewVal.setText(byteStr)
        tbl.setCellWidget(rowPosition, 1, txtEditNewVal)

        # Кнопка применения введенных изменений
        btn = QtWidgets.QPushButton(tbl)
        btn.setText('')
        btn.setIcon(QtGui.QIcon(icons.confirmByteChange))
        #btn.setIconSize(self.__getQSize(identDiv, btn))
        tbl.setCellWidget(rowPosition, 2, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__chgValueTestData(txtEditPosition, txtEditNewVal)
        )

        # Кнопка отмены изменений
        btn = QtWidgets.QPushButton(tbl)
        btn.setText('')
        btn.setIcon(QtGui.QIcon(icons.startByteChange))
        #btn.setIconSize(self.__getQSize(identDiv, btn))
        tbl.setCellWidget(rowPosition, 3, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__cnclValueTestData(txtEditPosition, txtEditNewVal)
        )

        # Кнопка поиска байта по адресу
        btn = QtWidgets.QPushButton(tbl)
        btn.setText('')
        btn.setIcon(QtGui.QIcon(icons.searchByteChange))
        #btn.setIconSize(self.__getQSize(identDiv, btn))
        tbl.setCellWidget(rowPosition, 4, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__getValByAddr(txtEditPosition, txtEditNewVal)
        )

        # Кнопка удаления строки
        btn = QtWidgets.QPushButton(tbl)
        btn.setText('')
        btn.setIcon(QtGui.QIcon(icons.delByteChange))
        #btn.setIconSize(self.__getQSize(identDiv, btn))
        tbl.setCellWidget(rowPosition, 5, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__delRowChgTbl(tbl.currentRow())
        )

        tbl.resizeColumnsToContents()

    ''' Получить значение по адресу в тестовых данных '''
    def __getValByAddr(self, txtEditPosition, txtEditVal):
        try:
            if self.__checkChgField(txtEditPosition, txtEditVal):
                findVal = self.parentClass.workApi.currTestData.getValByPos(hexPos=txtEditPosition.toPlainText())
                txtEditVal.setText(findVal)
                self.lblMsg.setText(msgChgNum.confirmFind)
        except:
            self.lblMsg.setText(msgChgNum.badAction)

    def __delRowChgTbl(self, row):
        self.tblChgTest.removeRow(row)

    def updChgTbl(self, data):
        try:
            count = 0
            # True, тк как читаем до тех пор, пока в данных записи будут
            while True:
                self.addWithStartData(self.tblChgTest, data[str(count)].split("->")[0], data[str(count)].split("->")[1])
                count += 1
        except:
            pass

    def chgAll(self):
        for i in range(self.tblChgTest.rowCount()):
            self.tblChgTest.cellWidget(i, 2).click()

    def chgStartAll(self):
        for i in range(self.tblChgTest.rowCount()):
            self.tblChgTest.cellWidget(i, 3).click()

    def chgFindAll(self):
        for i in range(self.tblChgTest.rowCount()):
            self.tblChgTest.cellWidget(i, 4).click()

    def chgClearAll(self):
        self.tblChgTest.setRowCount(0)


    ''' Проверка полей при изменении/поиске/откате тестовых данных '''
    def __checkChgField(self, txtEditPosition, txtEditNewVal):
        # Проверка на пустоту полей
        if txtEditPosition.toPlainText() == "" or txtEditNewVal.toPlainText() == "":
            self.lblMsg.setText(msgChgNum.emptyField)
            return False
        # Проверка на валидность позиции
        intNum = -1
        try:
            intNum = int(txtEditPosition.toPlainText(), 16)
        except:
            try:
                if txtEditPosition.toPlainText()[-1] == 'h':
                    intNum = int(txtEditPosition.toPlainText()[:-1], 16)
            except:
                self.lblMsg.setText(msgChgNum.badPosition)
                return False
        if intNum >= len(self.parentClass.workApi.currTestData.getLstTestData()):
            self.lblMsg.setText(msgChgNum.badPosition)
            return False
        txtEditPosition.setText(hex(intNum)[2:])

        # Проверка на валидность нового значения
        try:
            intNum = int(txtEditNewVal.toPlainText(), 16)
        except:
            self.lblMsg.setText(msgChgNum.badHexNum)
            return False
        txtEditNewVal.setText(hex(intNum)[2:])
        return True

    ''' Изменение тестовых данных '''
    def __chgValueTestData(self, txtEditPosition, txtEditNewVal):
        try:
            if self.__checkChgField(txtEditPosition, txtEditNewVal):
                self.parentClass.workApi.currTestData.chgValue(hexPos=txtEditPosition.toPlainText(), newVal=txtEditNewVal.toPlainText())
                self.updTblInputTest()
                self.lblMsg.setText(msgChgNum.confirmChg)
        except:
            self.lblMsg.setText(msgChgNum.badAction)

    ''' откат изменений в тестовых данных '''
    def __cnclValueTestData(self, txtEditPosition, txtEditNewVal):
        try:
            if self.__checkChgField(txtEditPosition, txtEditNewVal):
                self.parentClass.workApi.currTestData.backStartValue(hexPos=txtEditPosition.toPlainText())
                self.updTblInputTest()
                self.lblMsg.setText(msgChgNum.confirmCancelChg)
        except:
            self.lblMsg.setText(msgChgNum.badAction)
