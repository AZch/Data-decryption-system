import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import threading
import time
import json
import traceback

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from WorkApi import WorkApi
from Constants import msgWarning
from Constants import msgConfirm
from Constants import msgError
from Constants import StrRetConts
from Constants import jsonWord
from Constants import NumConst
from Constants import StrConst
from Constants import msgChgNum
from Constants import typeMethod

import design  # Это наш конвертированный файл дизайна
import designOpenTbl
from OpenTblWnd import OpenTblWnd

class MainWnd(QtWidgets.QMainWindow, design.Ui_MainWindow):
    ''' Сигнналы (должны быть объявлены здесь) для обновления данных и таблицы при выполнении метода '''
    sgnUpdExec = QtCore.pyqtSignal(int, str, int, name='sgnUpdExec')
    sgnUpdTbl = QtCore.pyqtSignal(name='sgnUpdTbl')

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.countMethod = 0

        self.cmbMethods.addItems([typeMethod.typeCheck, typeMethod.typeBruteForce,
                                  typeMethod.typeRandom, typeMethod.typeCompBase])
        self.__initAPI()
        self.__initBtn()
        self.__initSgn()
        self.__initResTbl()
        self.__initDataFromCfg()
        self.workApi.setFactoryCheck()

    def __initDataFromCfg(self):
        file = open(jsonWord.configName, 'r')
        with file:
            data = file.read()
            self.jsonData = json.loads(data)
            self.currCfg = self.jsonData[jsonWord.readCfg]
            self.currCfgMethods = self.jsonData[self.currCfg][jsonWord.readCfgMethods]
            self.currCfgFiles = self.jsonData[self.currCfg][jsonWord.readCfgFiles]
            self.currCfgChgVal = self.jsonData[self.currCfg][jsonWord.readCfgChgVal]

            self.workApi.loadJSONMethods(dataStr=self.jsonData[self.currCfgMethods])
            self.updateAfterSelect()
            self.workApi.loadJSONFiles(dataStr=self.jsonData[self.currCfgFiles])
            self.updTblInputTest()
            self.updNameFiles()
            self.updChgTbl(self.jsonData[self.currCfgChgVal])

    ''' Инициализация таблицы с результатом '''
    def __initResTbl(self):
        self.tblRes.setColumnCount(NumConst.countColumnRes)
        self.tblRes.setHorizontalHeaderLabels([
            StrConst.сolumnNameFun, StrConst.columnNameRes, StrConst.columnByte, StrConst.columnLocByte
        ])
        self.tblRes.horizontalHeaderItem(0).setToolTip(StrConst.сolumnNameFun)
        self.tblRes.horizontalHeaderItem(1).setToolTip(StrConst.columnNameRes)
        self.tblRes.horizontalHeaderItem(2).setToolTip(StrConst.columnByte)
        self.tblRes.horizontalHeaderItem(3).setToolTip(StrConst.columnLocByte)
        self.tblRes.resizeColumnsToContents()

    ''' Инициализация API '''
    def __initAPI(self):
        self.workApi = WorkApi()

    ''' Инициализация сигналов '''
    def __initSgn(self):
        self.sgnUpdExec.connect(self.__sgnUpdExec, QtCore.Qt.QueuedConnection)
        self.sgnUpdTbl.connect(self.__sgnUpdTbl, QtCore.Qt.QueuedConnection)

    ''' Инициализация кнопок '''
    def __initBtn(self):
        self.cmbMethods.activated[str].connect(self.setFactory)
        self.btnLoadExecFile.clicked.connect(self.loadExecFile)
        self.btnExit.clicked.connect(self.__exitForm)
        self.btnLoadInputTest.clicked.connect(self.loadInputTestFile)
        self.btnAddMethod.clicked.connect(self.addMethod)
        self.btnCalcThisMethod.clicked.connect(self.calcThisMethod)
        self.btnNextMethod.clicked.connect(self.nextMethod)
        self.btnPrevMethod.clicked.connect(self.prevMethod)
        self.btnSaveTest.clicked.connect(self.saveTestRes)
        self.btnSaveResByte.clicked.connect(self.saveTestResByte)
        self.btnDelThisMethod.clicked.connect(self.delMethod)
        self.btnDelAllMethod.clicked.connect(self.delMethods)
        self.btnCalcTo.clicked.connect(self.calcTo)
        self.btnSaveThisMethod.clicked.connect(self.saveMethod)
        self.btnSaveAllMethod.clicked.connect(self.saveAllMethod)
        self.btnLoadMethods.clicked.connect(self.loadMethod)
        self.btnLoadResFile.clicked.connect(self.loadTestResFile)
        self.btnAddStrEditTest.clicked.connect(self.addStrToEditTest)
        self.btnOpenInputData.clicked.connect(self.openNewWndInputTest)
        self.btnOpenResData.clicked.connect(self.openNewWndResData)

    ''' Сигнал обновления данных при выполнении метода '''
    def __sgnUpdExec(self, newValuePrg, newMsg, newValueLcd):
        self.lblExecuteProc.setText(newMsg)
        self.lcdNumber.display(newValueLcd)
        try:
            self.prgExec.setValue(newValuePrg)
        except:
            self.prgExec.setValue(100)

    ''' Сигнла обновления таблицы при выполении метода '''
    def __sgnUpdTbl(self):
        self.setResTable(res=self.workApi.dataForTable())

    ''' Добавление новых кнопок и полей для изменения входных данных '''
    def addStrToEditTest(self):
        self.addWithStartData("0", "00")

    def addWithStartData(self, posStr, byteStr):
        rowPosition = self.tblChgTest.rowCount()
        self.tblChgTest.insertRow(rowPosition)

        # Поля для позиции
        txtEditPosition = QtWidgets.QTextEdit(self.tblChgTest)
        txtEditPosition.setText(posStr)
        self.tblChgTest.setCellWidget(rowPosition, 0, txtEditPosition)

        # Поле для нового значения
        txtEditNewVal = QtWidgets.QTextEdit(self.tblChgTest)
        txtEditNewVal.setText(byteStr)
        self.tblChgTest.setCellWidget(rowPosition, 1, txtEditNewVal)

        # Кнопка применения введенных изменений
        btn = QtWidgets.QPushButton(self.tblChgTest)
        btn.setText('Готово')
        self.tblChgTest.setCellWidget(rowPosition, 2, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__chgValueTestData(txtEditPosition, txtEditNewVal)
        )

        # Кнопка отмены изменений
        btn = QtWidgets.QPushButton(self.tblChgTest)
        btn.setText('Начальное')
        self.tblChgTest.setCellWidget(rowPosition, 3, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__cnclValueTestData(txtEditPosition, txtEditNewVal)
        )

        # Кнопка поиска байта по адресу
        btn = QtWidgets.QPushButton(self.tblChgTest)
        btn.setText('Получить')
        self.tblChgTest.setCellWidget(rowPosition, 4, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__getValByAddr(txtEditPosition, txtEditNewVal)
        )

        # Кнопка удаления строки
        btn = QtWidgets.QPushButton(self.tblChgTest)
        btn.setText('Убрать')
        self.tblChgTest.setCellWidget(rowPosition, 5, btn)
        btn.clicked.connect(
            lambda *args, rowPosition=rowPosition: self.__delRowChgTbl(self.tblChgTest.currentRow())
        )

        self.tblRes.resizeColumnsToContents()

    def __delRowChgTbl(self, row):
        self.tblChgTest.removeRow(row)

    def updChgTbl(self, data):
        try:
            count = 0
            # True, тк как читаем до тех пор, пока в данных записи будут
            while True:
                self.addWithStartData(data[str(count)].split("->")[0], data[str(count)].split("->")[1])
                count += 1
        except:
            pass

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
        if intNum >= len(self.workApi.currTestData.getLstTestData()):
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
                self.workApi.currTestData.chgValue(hexPos=txtEditPosition.toPlainText(), newVal=txtEditNewVal.toPlainText())
                self.updTblInputTest()
                self.lblMsg.setText(msgChgNum.confirmChg)
        except:
            self.lblMsg.setText(msgChgNum.badAction)

    ''' откат изменений в тестовых данных '''
    def __cnclValueTestData(self, txtEditPosition, txtEditNewVal):
        try:
            if self.__checkChgField(txtEditPosition, txtEditNewVal):
                self.workApi.currTestData.backStartValue(hexPos=txtEditPosition.toPlainText())
                self.updTblInputTest()
                self.lblMsg.setText(msgChgNum.confirmCancelChg)
        except:
            self.lblMsg.setText(msgChgNum.badAction)

    def makeCfg(self):
        dataToCfg = {}
        dataToCfg[jsonWord.readCfg] = self.currCfg
        dataToCfg[self.currCfg] = {}
        dataToCfg[self.currCfg][jsonWord.readCfgMethods] = self.currCfgMethods
        dataToCfg[self.currCfg][jsonWord.readCfgFiles] = self.currCfgFiles
        dataToCfg[self.currCfg][jsonWord.readCfgChgVal] = self.currCfgChgVal

        dataToCfg[self.currCfgMethods] = self.workApi.exportAllMethods()

        dataToCfg[self.currCfgFiles] = {}
        dataToCfg[self.currCfgFiles][jsonWord.testFile] = self.workApi.testDataWay
        dataToCfg[self.currCfgFiles][jsonWord.execFile] = self.workApi.execFileName
        dataToCfg[self.currCfgFiles][jsonWord.endResFile] = self.workApi.resDataWay

        rowChgTblCount = self.tblChgTest.rowCount()
        dataToCfg[self.currCfgChgVal] = {}
        for i in range(rowChgTblCount):
            dataToCfg[self.currCfgChgVal][str(i)] = self.tblChgTest.cellWidget(i, 0).toPlainText() + \
                                                    "->" + self.tblChgTest.cellWidget(i, 1).toPlainText()
        return dataToCfg

    def __compareDataInCfg(self, firstData, secondData):
        firstDataStr = str(firstData)
        secondDataStr = str(secondData)
        if len(firstDataStr) != len(secondDataStr):
            return False
        for i in range(len(firstDataStr)):
            if firstDataStr[i] != secondDataStr[i]:
                return False
        return True

    def compareCfg(self, firstCfg, secondCfg):
        if not self.__compareDataInCfg(firstCfg[self.currCfgMethods], secondCfg[self.currCfgMethods]):
            return False
        if not self.__compareDataInCfg(firstCfg[self.currCfgFiles], secondCfg[self.currCfgFiles]):
            return False
        if not self.__compareDataInCfg(firstCfg[self.currCfgChgVal], secondCfg[self.currCfgChgVal]):
            return False
        return True

    ''' Закрытие формы '''
    def __exitForm(self):
        dataToCfg = self.makeCfg()
        if not self.compareCfg(dataToCfg, self.jsonData):
            qMessBox = QtWidgets.QMessageBox
            if qMessBox.question(self, 'Перезапись конфига', 'С последнего запуска вы внесли изменения в программу, '
                                                             'перезаписать конфиг с текущими значениями?',
                                 qMessBox.Yes | qMessBox.No) == qMessBox.Yes:
                fileCfg = open(jsonWord.configName, 'w')
                fileCfg.write(json.dumps(dataToCfg))
                fileCfg.close()

        QtCore.QCoreApplication.instance().quit()

    ''' Получить значение по адресу в тестовых данных '''
    def __getValByAddr(self, txtEditPosition, txtEditVal):
        try:
            if self.__checkChgField(txtEditPosition, txtEditVal):
                findVal = self.workApi.currTestData.getValByPos(hexPos=txtEditPosition.toPlainText())
                txtEditVal.setText(findVal)
                self.lblMsg.setText(msgChgNum.confirmFind)
        except:
            self.lblMsg.setText(msgChgNum.badAction)

    ''' Разворачивание теста '''
    def openNewWndInputTest(self):
        self.dialogTest = OpenTblWnd(self.tblInutTest)
        self.dialogTest.show()

    def openNewWndResData(self):
        self.dialogRes = OpenTblWnd(self.tblRes)
        self.dialogRes.show()

    """ Работа с файлами """
    ''' Выбор файла для сохранения '''
    def loadTestResFile(self):
        wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
        self.workApi.setWayResData(wayFile=wayFile)
        waySplit = wayFile.split('/')
        self.lblResFile.setText(waySplit[len(waySplit) - 1])

    ''' Сохранение результата '''
    def saveTestRes(self):
        try:
            wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
            file = open(wayFile, 'w')
            if file == '':
                return self.lblMsg.setText(msgWarning.noFileLoad)
            file.write(self.workApi.saveResData())
            file.close()
            self.lblMsg.setText(msgConfirm.saveFile)
        except:
            self.lblMsg.setText(msgError.saveFile)

    ''' Сохранение теста в файл '''
    def saveTestResByte(self):
        try:
            wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
            file = open(wayFile, 'w')
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            file.write(self.workApi.saveResDataByte())
            file.close()
            self.lblMsg.setText(msgConfirm.saveFile)
        except:
            self.lblMsg.setText(msgError.saveFile)

    ''' Загрузка '''
    def loadExecFile(self):
        try:
            self.lblExecFile.clear()
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите исполняемый файл')[0]
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            self.workApi.setExecFileName(wayFile=file)
            waySplit = file.split('/')
            self.lblExecFile.setText(waySplit[len(waySplit) - 1])
            self.lblMsg.setText(msgConfirm.loadFile)
        except:
            self.lblMsg.setText(msgError.loadFile)

    ''' Обновление таблицы с входным тестом '''
    def updTblInputTest(self):
        try:
            matrixTest = self.workApi.currTestData.makeMatrixData()
            self.tblInutTest.setColumnCount(len(matrixTest[0]))
            self.tblInutTest.setRowCount(len(matrixTest))
            for i in range(len(matrixTest)):
                for j in range(len(matrixTest[i])):
                    self.tblInutTest.setItem(i, j,
                                             QtWidgets.QTableWidgetItem(matrixTest[i][j]))
            self.tblInutTest.resizeColumnsToContents()
        except:
            pass

    ''' Загрузка входного теста '''
    def loadInputTestFile(self):
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите тестовый пример')[0]
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            waySplit = file.split('/')
            self.lblInputTest.setText(waySplit[len(waySplit) - 1])
            try :
                loadFile = open(file, 'r')
                with loadFile:
                    data = loadFile.read()
                    #self.txtInputTest.setText(data)
                    self.workApi.loadData(data=data, fileWay=file)

                    self.updTblInputTest()
            except:
                self.lblInputTest.clear()
                self.txtInputTest.clear()
                return self.lblMsg.setText(msgError.loadFile)
            self.lblMsg.setText(msgConfirm.loadFile)
        except:
            self.lblMsg.setText(msgError.loadFile)

    def updNameFiles(self):
        try:
            file = self.workApi.testDataWay
            waySplit = file.split('/')
            self.lblInputTest.setText(waySplit[len(waySplit) - 1])
        except:
            pass
        try:
            file = self.workApi.execFileName
            waySplit = file.split('/')
            self.lblExecFile.setText(waySplit[len(waySplit) - 1])
        except:
            pass
        try:
            file = self.workApi.resDataWay
            waySplit = file.split('/')
            self.lblResFile.setText(waySplit[len(waySplit) - 1])
        except:
            pass


    """ Работа с методами """
    ''' Сохранение метода '''
    def saveMethod(self):
        try:
            wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
            file = open(wayFile, 'w')
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            file.write(json.dumps(self.workApi.exportMethod()))
            file.close()
            self.lblMsg.setText(msgConfirm.saveFile)
        except:
            self.lblMsg.setText(msgError.saveFile)

    ''' Загрузка метода(ов) '''
    def loadMethod(self):
        try:
            self.lblExecFile.clear()
            file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл с методами')[0]
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            try :
                loadFile = open(file, 'r')
                with loadFile:
                    data = loadFile.read()
                    self.workApi.loadJSONMethods(dataStr=json.loads(data))
            except:
                return self.lblMsg.setText(msgError.loadFile)
            self.lblMsg.setText(msgConfirm.loadFile)
            self.updateAfterSelect()
        except:
            self.lblMsg.setText(msgError.loadFile)

    ''' Сохранение всех методов '''
    def saveAllMethod(self):
        try:
            wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
            file = open(wayFile, 'w')
            if file == '' :
                return self.lblMsg.setText(msgWarning.noFileLoad)
            currMethod = self.workApi.currMethod
            self.workApi.goStartMethod()
            countMethods = 1
            data = {}
            data[jsonWord.method + str(countMethods)] = self.workApi.exportMethod()
            while self.workApi.goNextMethod() != StrRetConts.retBat:
                countMethods += 1
                data[jsonWord.method + str(countMethods)] = self.workApi.exportMethod()
            file.write(json.dumps(data))
            file.close()
            self.lblMsg.setText(msgConfirm.saveFile)
            self.workApi.currMethod = currMethod
        except:
            self.lblMsg.setText(msgError.saveFile)

    ''' Удаление метода '''
    def delMethod(self):
        try:
            if self.workApi.delMethod() == StrRetConts.retBat:
                raise ValueError()
            self.updateAfterSelect()
            self.lblMsg.setText(msgConfirm.delMethod)
            self.countMethod -= 1
            self.updateAfterSelect()
        except:
            self.lblMsg.setText(msgError.delMethod)

    ''' Удаление методов '''
    def delMethods(self):
        try:
            if self.workApi.delMethod() == StrRetConts.retBat:
                raise ValueError()
            while self.workApi.delMethod() != StrRetConts.retBat:
                pass
            self.lblMsg.setText(msgConfirm.delMethods)
            self.countMethod = 0
            self.updateAfterSelect()
        except:
            self.lblMsg.setText(msgError.delMethods)

    ''' Вычисление до метода '''
    def calcTo(self):
        try:
            if self.countMethod < self.spnToMethod.value():
                return self.lblMsg.setText(msgWarning.toMachMethods)
            countCalc = self.spnToMethod.value()
            goPrev = True
            while countCalc > 0:
                countCalc -= 1
                self.workApi.calcMethod()
                self.workApi.saveResDataByte()
                if self.workApi.goNextMethod() == StrRetConts.retBat:
                    goPrev = False
            if goPrev:
                self.workApi.goPrevMethod()
            self.lblMsg.setText(msgConfirm.successCalc)
            self.updateAfterSelect()
        except:
            self.lblMsg.setText(msgError.successCalc)

    ''' Задание фабрик методов '''
    def setFactory(self, text):
        if (text == typeMethod.typeCheck):
            self.workApi.setFactoryCheck()
            self.lblStartAllPos.setText('c')
            self.lblToCount.setText('по')
        elif (text == typeMethod.typeBruteForce):
            self.workApi.setFactoryBruteForce()
            self.lblStartAllPos.setText('Позиции (16 ричная, без 0х и h)')
            self.lblToCount.setText('Количество раз,-1 полный перебор')
        elif (text == typeMethod.typeRandom):
            self.workApi.setFactoryRandom()
            self.lblStartAllPos.setText('Позиции (16 ричная, без 0х и h)')
            self.lblToCount.setText('Количество раз')
        elif (text == typeMethod.typeCompBase):
            self.workApi.setFactoryCompBase()
            self.lblStartAllPos.setText('')
            self.lblToCount.setText('')
        else:
            self.workApi.clearFactory()
            return self.lblMsg.setText(msgWarning.noReleaseMethod)
        self.lblMsg.setText(msgConfirm.setReleaseMethod)

    def getArrPos(self):
        strLst = self.txtPosStart.toPlainText().split()
        intLst = list()
        for pos in strLst:
            intLst.append(int('0x' + pos, 16))
        return intLst

    def makeArrParam(self):
        if str(self.cmbMethods.currentText()) == typeMethod.typeCheck:
            return [self.nameMethod.toPlainText(), self.spnCountThread.value(),
                     int(self.txtPosStart.toPlainText()), int(self.txtPosEnd.toPlainText()),
                     self.spnSleepWork.value(), self.spnTimeWait.value()]
        elif str(self.cmbMethods.currentText()) == typeMethod.typeBruteForce:
            return [self.nameMethod.toPlainText(), self.spnCountThread.value(),
                    self.spnTimeWait.value(), self.getArrPos(), int(self.txtPosEnd.toPlainText())]
        elif str(self.cmbMethods.currentText()) == typeMethod.typeRandom:
            return [self.nameMethod.toPlainText(), self.spnCountThread.value(),
                    self.spnTimeWait.value(), self.getArrPos(), int(self.txtPosEnd.toPlainText())]
        elif str(self.cmbMethods.currentText()) == typeMethod.typeCompBase:
            return [self.nameMethod.toPlainText(), self.spnTimeWait.value()]
        else:
            return []

    ''' Добавление метода '''
    def addMethod(self):
        try:
            if self.nameMethod.toPlainText() == '' or self.workApi.createMethod(self.makeArrParam()) == StrRetConts.retBat:
                return self.lblMsg.setText(msgError.addMethod)
            self.updateAfterSelect()
            self.lblMsg.setText(msgConfirm.addMethod)
            self.countMethod += 1
        except:
            print('Ошибка:\n', traceback.format_exc())
            self.lblMsg.setText(msgError.addMethod)

    ''' Переход между методами '''
    def nextMethod(self):
        try:
            if self.workApi.goNextMethod() == StrRetConts.retBat:
                raise ValueError()
            self.updateAfterSelect()
            self.lblMsg.setText(msgConfirm.changeMethod)
        except:
            self.lblMsg.setText(msgWarning.noNextMethod)

    def prevMethod(self):
        try:
            if self.workApi.goPrevMethod() == StrRetConts.retBat:
                raise ValueError()
            self.updateAfterSelect()
            self.lblMsg.setText(msgConfirm.changeMethod)
        except:
            self.lblMsg.setText(msgWarning.noPrevMethod)

    ''' Вычисление по выбранному методу '''
    def calcThisMethod(self):
        try:
            res = self.workApi.calcMethod()
            newThread = threading.Thread(target=self.updateCalc, args=[self.workApi, self.sgnUpdExec,
                                                                       self.getAllBtnArray(), self.sgnUpdTbl])
            newThread.start()
            if res == StrRetConts.retBat:
                raise ValueError()
        except:
            print('Ошибка:\n', traceback.format_exc())
            self.lblMsg.setText(msgError.successCalc)

    ''' Получить все кнопки которые надо заблокировать на время вычисления '''
    def getAllBtnArray(self):
        return [self.btnCalcThisMethod, self.btnCalcTo, self.btnNextMethod, self.btnPrevMethod,
                self.btnSaveResByte, self.btnSaveThisMethod, self.btnSaveAllMethod,
                self.btnDelThisMethod, self.btnDelAllMethod, self.btnLoadMethods, self.btnAddMethod,
                self.btnLoadResFile, self.btnLoadExecFile, self.btnLoadInputTest,
                self.tblChgTest, self.btnAddStrEditTest, self.btnChgAll, self.btnClearChgAll, self.btnFindChgAll]

    ''' Обновление данных формы во время работы метода '''
    def updateCalc(self, workApi, sgnUpdExec, arrayBtnLock, sgnUpdTbl):
        startTime = time.time()
        try:
            for btn in arrayBtnLock:
                btn.setEnabled(False)
            maxByte = workApi.getMaxCountByte()
            oldThisCountByte = workApi.getThisCalcByte() - 1
            while (workApi.checkEndCalc()):
                if oldThisCountByte != workApi.getThisCalcByte():
                    sgnUpdExec.emit((workApi.getThisCalcByte() + 1) * 100 / maxByte,
                                    "Вычисление! номер байта: " +
                                     str(workApi.getThisCalcByte() + 1) + " / " + str(maxByte),
                                    int(time.time() - startTime)
                                    )
                    sgnUpdTbl.emit()
                    oldThisCountByte = workApi.getThisCalcByte()
            for btn in arrayBtnLock:
                btn.setEnabled(True)
            if workApi.getThisCalcByte() == maxByte:
                msgSend = msgConfirm.successCalc
            else:
                msgSend = msgError.successCalc
            sgnUpdExec.emit(0,
                            msgSend,
                            int(time.time() - startTime)
                            )
            sgnUpdTbl.emit()
        except:
            for btn in arrayBtnLock:
                btn.setEnabled(True)
            sgnUpdExec.emit(0,
                            msgError.successCalc,
                            int(time.time() - startTime)
                            )
            sgnUpdTbl.emit()

    ''' Задать в результирующую таблицу данные '''
    def setResTable(self, res):
        try:
            self.tblRes.setRowCount(0)
            i = 0
            moreStr = res.split('\n')
            self.tblRes.setRowCount(len(moreStr))
            for str in moreStr:
                dataStr = str.split('|')
                self.tblRes.setItem(i, 0, QtWidgets.QTableWidgetItem(dataStr[0]))
                self.tblRes.setItem(i, 1, QtWidgets.QTableWidgetItem(dataStr[1]))
                self.tblRes.setItem(i, 2, QtWidgets.QTableWidgetItem(dataStr[2]))
                self.tblRes.setItem(i, 3, QtWidgets.QTableWidgetItem(dataStr[3]))
                i += 1
            self.tblRes.resizeColumnsToContents()
        except:
            self.tblRes.setRowCount(0)
            self.lblMsg.setText("нет результатов для этого метода")

    """ Обновление данных на экране данных """
    def updateAfterSelect(self):
        self.lblThisMethod.setText(self.workApi.getNameThisMethod())
        self.lblPrevMethod.setText(self.workApi.getNamePrevMethod())
        self.lblNextMethod.setText(self.workApi.getNameNextMethod())
        self.setResTable(res=self.workApi.dataForTable())

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWnd()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()