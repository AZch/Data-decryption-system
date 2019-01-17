from Methods.Method import Method
import time
import random
import string
from Data.Note import Note
from Data.Data import Data
from Data.TestData import TestData
from Constants import jsonWord
from ObjectPool.ExecProcPool import ExecProcPool
from ObjectPool.ExecProc import ExecProc
from threading import Thread

class MethodCheck(Method):

    def __init__(self, name, timeSleep, countRowStart, countRowEnd, countProc, timeWait):
        super().__init__(name=name)
        self.__timeSleep = timeSleep
        self.__countRowStart = countRowStart
        self.__countRowEnd = countRowEnd
        self.__countProc = countProc
        self.__timeWait = timeWait
        self.thisCalcStr = 0
        self.thisCalcByte = 0

    def makeReport(self):
        resStr = "Функции: \n"
        for note in self.resData.getData():
            resStr += note.nameFunction + " Позиции байтов: " + ' '.join(hex(posInt)[2:] + 'h' for posInt in note.lstPosition) + '\n'
        return resStr

    def calc(self, testData, resFileWay, execFileWay):
        if (not isinstance(testData, TestData)):
            print("Неверный формат входных данных")
            return 0

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc, maxWait=self.__timeWait) # инициализируем заданное количество процессов
        isBaseData = self.__getBaseData__(execProcPool=execProcPool, execFileWay=execFileWay,
                                          resFileWay=resFileWay, testData=testData)
        if isBaseData == 0:
            return isBaseData

        posByteX = 0 # содержат позицию байтов, которые поток проверяет (для последнего шага проверки)
        posByteY = 0
        x = self.__countRowStart
        while x <= self.__countRowEnd:
            self.thisCalcStr = x
            for y in range(len(testData.getLstTestData()[x])):
                posByteX = x
                posByteY = y
                self.thisCalcByte = (x - self.__countRowStart) * len(testData.getLstTestData()[x]) + y
                testData.incDot(x, y) # изменяем данные в одной позиции
                self._resStrData = "" # обнуляем строку с даннымии в которую будет записан результат
                # получаем новый поток
                proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
                                        testData=testData, byte=testData.getLstTestData()[x][y],
                                        bytePos=x * len(testData.getLstTestData()[x]) + y)
                proc.start() # запускаем поток (запускается бат файл и формируется список результатов)
                while self.addRes(execProcPool.wait()) == 'wait': # ожидаем пока не будет доступен поток
                    pass
                self.addRes(notes=self.compareData(position=x * len(testData.getLstTestData()[x]) + y,
                                                                 byte=testData.getLstTestData()[x][y]))  # добавлем различия
                testData.decDot(x, y)
            x += 1
        testData.saveToFile() # сохраняем последний раз файл с правильными данными
        # дожидаемся последний поток
        while self.addRes(execProcPool.wait()) == 'wait':  # ожидаем пока не будет доступен поток
            pass
        self.addRes(notes=self.compareData(position=posByteX * len(testData.getLstTestData()[posByteX]) + posByteY,
                                                         byte=testData.getLstTestData()[posByteX][posByteY]))  # добавлем различия
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name : self.name,
            jsonWord.type : jsonWord.mCheck,
        }
        return data

    def getMaxCountByte(self, testData):
        return (self.__countRowEnd + 1 - self.__countRowStart) * len(testData.getLstTestData()[self.__countRowEnd])

    def getThisCalcStr(self):
        return self.thisCalcStr

    def getThisCalcByte(self):
        return self.thisCalcByte