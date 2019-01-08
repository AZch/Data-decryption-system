import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import time

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from WorkApi import WorkApi

import design  # Это наш конвертированный файл дизайна

class MainWnd(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.workApi = WorkApi()
        self.workApi.setFactoryCheck()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.cmbMethods.addItems(["Проверка", "Метод проверки"])

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

    def saveTestRes(self):
        wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
        file = open(wayFile, 'w')
        file.write(self.workApi.saveResData())
        file.close()

    def saveTestResByte(self):
        wayFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл для сохранения')[0]
        file = open(wayFile, 'w')
        file.write(self.workApi.saveResDataByte())
        file.close()

    def setFactory(self, text):
        if (text == "Проверка"):
            self.workApi.setFactoryCheck()
        elif (text == "Метод проверки"):
            self.lblMsg.setText("Данный метод еще не реализован")
        else:
            self.lblMsg.setText("Данный метод еще не реализован")

    def addMethod(self):
        self.workApi.createMethod(self.nameMethod.toPlainText())
        self.updateAfterSelect()

    def nextMethod(self):
        self.workApi.goNextMethod()
        self.updateAfterSelect()

    def prevMethod(self):
        self.workApi.goPrevMethod()
        self.updateAfterSelect()

    def calcThisMethod(self):
        startTime = time.time()
        self.txtRes.setText(self.workApi.calcMethod())
        self.lcdNumber.display(int(time.time() - startTime))

    def loadExecFile(self):
        self.lblExecFile.clear()
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите исполняемый файл')[0]
        waySplit = file.split('/')
        self.lblExecFile.setText(waySplit[len(waySplit) - 1])

    def loadInputTestFile(self):
        self.lblInputTest.clear()
        self.txtInputTest.clear()
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите тестовый пример')[0]
        waySplit = file.split('/')
        self.lblInputTest.setText(waySplit[len(waySplit) - 1])
        try :
            loadFile = open(file, 'r')
            with loadFile:
                data = loadFile.read()
                self.txtInputTest.setText(data)
                self.workApi.loadData(data=data)
        except:
            self.lblInputTest.clear()
            self.txtInputTest.clear()
            self.lblMsg.setText("Плохой файл для загрузки")

    def updateAfterSelect(self):
        check = self.workApi.getNameThisMethod()
        self.lblThisMethod.setText(self.workApi.getNameThisMethod())
        self.lblPrevMethod.setText(self.workApi.getNamePrevMethod())
        self.lblNextMethod.setText(self.workApi.getNameNextMethod())

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWnd()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()