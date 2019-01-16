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

import design  # Это наш конвертированный файл дизайна

class MainWnd(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.countMethod = 0

        self.cmbMethods.addItems(["Проверка", "Метод проверки"])
        self.__initAPI()
        self.__initBtn()

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
        self.workApi.setFactoryCheck()

    ''' Инициализация кнопок '''
    def __initBtn(self):
        self.cmbMethods.activated[str].connect(self.setFactory)
        self.btnLoadExecFile.clicked.connect(self.loadExecFile)
        self.btnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
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


    """ Работа с файлами """
    def loadTestResFile(self):
        wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
        self.workApi.setWayResData(wayFile=wayFile)
        waySplit = wayFile.split('/')
        self.lblResFile.setText(waySplit[len(waySplit) - 1])

    ''' Сохранение '''
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

                    self.tblInutTest.setColumnCount(len(self.workApi.currTestData.getLstTestData()[0]))
                    self.tblInutTest.setRowCount(len(self.workApi.currTestData.getLstTestData()))
                    for i in range(len(self.workApi.currTestData.getLstTestData())):
                        for j in range(len(self.workApi.currTestData.getLstTestData()[0])):
                            self.tblInutTest.setItem(i, j, QtWidgets.QTableWidgetItem(self.workApi.currTestData.getLstTestData()[i][j]))
                    self.tblInutTest.resizeColumnsToContents()
            except:
                self.lblInputTest.clear()
                self.txtInputTest.clear()
                return self.lblMsg.setText(msgError.loadFile)
            self.lblMsg.setText(msgConfirm.loadFile)
        except:
            self.lblMsg.setText(msgError.loadFile)

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
                    self.workApi.loadJSONFile(dataStr=json.loads(data))
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
        if (text == "Проверка"):
            self.workApi.setFactoryCheck()
        elif (text == "Метод проверки"):
            self.workApi.clearFactory()
            return self.lblMsg.setText(msgWarning.noReleaseMethod)
        else:
            self.workApi.clearFactory()
            return self.lblMsg.setText(msgWarning.noReleaseMethod)
        self.lblMsg.setText(msgConfirm.setReleaseMethod)

    ''' Добавление метода '''
    def addMethod(self):
        try:
            if self.nameMethod.toPlainText() == '' or self.workApi.createMethod([self.nameMethod.toPlainText(), self.spnCountThread.value(),
                                                                                self.spnCountRowStart.value() - 1, self.spnCountRowEnd.value() - 1,
                                                                                 self.spnSleepWork.value(), self.spnTimeWait.value()]) == StrRetConts.retBat:
                return self.lblMsg.setText(msgError.addMethod)
            self.updateAfterSelect()
            self.lblMsg.setText(msgConfirm.addMethod)
            self.countMethod += 1
        except:
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
            newThread = threading.Thread(target=self.updateCalc, args=[self.workApi, self.lblMsg, self.getAllBtnArray(),
                                                                       self.updateAfterSelect, self.lcdNumber, time.time()])
            newThread.start()
            if res == StrRetConts.retBat:
                raise ValueError()
            #self.setResTable(res=res)
            #self.txtRes.setText(res)
        except:
            print('Ошибка:\n', traceback.format_exc())
            self.lblMsg.setText(msgError.successCalc)

    def getAllBtnArray(self):
        return [self.btnCalcThisMethod, self.btnCalcTo, self.btnNextMethod, self.btnPrevMethod,
                self.btnSaveResByte, self.btnSaveThisMethod, self.btnSaveAllMethod,
                self.btnDelThisMethod, self.btnDelAllMethod, self.btnLoadMethods, self.btnAddMethod,
                self.btnLoadResFile, self.btnLoadExecFile, self.btnLoadInputTest]

    def updateCalc(self, workApi, lblMsg, arrayBtnLock, functionUpdateRes, lcdNumber, startTime):
        try:
            for btn in arrayBtnLock:
                btn.setEnabled(False)
            maxByte = workApi.getMaxCountByte()
            oldThisCountByte = workApi.getThisCalcByte() - 1
            while (workApi.checkEndCalc()):
                lblMsg.setText(
                    "Вычисление! строка: " + str(workApi.getThisCalcStr() + 1) + " номер байта (со строки): " +
                    str(workApi.getThisCalcByte() + 1) + " / " + str(maxByte))
                if oldThisCountByte != workApi.getThisCalcByte():
                    functionUpdateRes()
                    oldThisCountByte = workApi.getThisCalcByte()
            for btn in arrayBtnLock:
                btn.setEnabled(True)
            lcdNumber.display(int(time.time() - startTime))
            if workApi.getThisCalcByte() + 1 == maxByte:
                lblMsg.setText(msgConfirm.successCalc)
            else:
                lblMsg.setText(msgError.successCalc)
            functionUpdateRes()
        except:
            for btn in arrayBtnLock:
                btn.setEnabled(True)
            lcdNumber.display(int(time.time() - startTime))
            lblMsg.setText(msgError.successCalc)

    def setResTable(self, res):
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

    """ Обновление данных на экране (label) """
    def updateAfterSelect(self):
        self.lblThisMethod.setText(self.workApi.getNameThisMethod())
        self.lblPrevMethod.setText(self.workApi.getNamePrevMethod())
        self.lblNextMethod.setText(self.workApi.getNameNextMethod())
        try:
            self.setResTable(res=self.workApi.dataForTable())
        except:
            self.tblRes.setRowCount(0)
            self.lblMsg.setText("нет результатов для этого метода")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWnd()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()