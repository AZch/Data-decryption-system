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

    def __init__(self, name, timeSleep, posStart, posEnd, countProc, timeWait):
        super().__init__(name=name, countProc=countProc, timeWait=timeWait)
        self.__timeSleep = timeSleep
        self.__posStart = posStart
        self.__posEnd = posEnd

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
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__) # инициализируем заданное количество процессов
        isBaseData = self.__getBaseData__(execProcPool=execProcPool, execFileWay=execFileWay,
                                          resFileWay=resFileWay, testData=testData, isBase=False)
        if isBaseData == 0:
            return isBaseData

        posByteSave = 0 # содержат позицию байтов, которые поток проверяет (для последнего шага проверки)
        pos = self.__posStart
        while pos <= self.__posEnd:
            posByteSave = pos
            self.thisCalcByte = pos - self.__posStart
            testData.incDot(pos) # изменяем данные в одной позиции
            self._resStrData = "" # обнуляем строку с даннымии в которую будет записан результат
            # получаем новый поток
            proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
                                    testData=testData, byte=testData.getLstTestData()[pos],
                                    bytePos=pos, isBase=False)
            proc.start() # запускаем поток (запускается бат файл и формируется список результатов)
            while self.addRes(execProcPool.wait()) == 'wait': # ожидаем пока не будет доступен поток
                pass
            self.addRes(notes=self.compareData(position=[pos], byte=[testData.getLstTestData()[pos]]))  # добавлем различия
            testData.decDot(pos)
            pos += 1
        testData.saveToFile(isBaseFile=False) # сохраняем последний раз файл с правильными данными
        # дожидаемся последний поток
        while self.addRes(execProcPool.wait()) == 'wait':  # ожидаем пока не будет доступен поток
            pass
        self.addRes(notes=self.compareData(position=[posByteSave],
                                                         byte=[testData.getLstTestData()[posByteSave]]))  # добавлем различия
        testData.saveBaseToFile()
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name : self.name,
            jsonWord.type : jsonWord.mCheck,
            jsonWord.mTimeSleep : self.__timeSleep,
            jsonWord.mTimeWait : self.__timeWait__,
            jsonWord.mCountProc : self.__countProc__,
            jsonWord.mPosStart : self.__posStart,
            jsonWord.mPosEnd : self.__posEnd
        }
        return data

    def getMaxCountByte(self):
        return (self.__posEnd + 1 - self.__posStart)