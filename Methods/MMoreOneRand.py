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
from DataDB.GRUD import *

class MMoreOneRand(Method):

    def __init__(self, name, posStart, posEnd, countProc, timeWait, countOneRand):
        super().__init__(name=name, countProc=countProc, timeWait=timeWait)
        self.__posStart = posStart
        self.__posEnd = posEnd
        self.__countOneRand = countOneRand

    def makeReport(self):
        resStr = "Функции: \n"
        for note in self.resData.getData():
            resStr += note.nameFunction + " Позиции байтов: " + ' '.join(hex(int(posInt))[2:] + 'h' for posInt in note.lstPosition) + '\n'
        return resStr

    def calc(self, testData, resFileWay, execFileWay):
        if (not isinstance(testData, TestData)):
            print("Неверный формат входных данных")
            return 0
        task = Add.addTask(method=jsonWord.mCheck, userName="")

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__) # инициализируем заданное количество процессов
        isBaseData = self.__getBaseData__(task, testData, False)

        if isBaseData == 0:
            return isBaseData

        pos = self.__posStart
        while pos <= self.__posEnd and pos < len(testData.getLstTestData()):
            self.thisCalcByte = pos - self.__posStart
            oldVal = testData.getByteByPos(pos)
            countRand = 0
            while countRand < self.__countOneRand:
                testData.randVal(hexPos=pos) # изменяем данные в одной позиции
                self._resStrData = "" # обнуляем строку с даннымии в которую будет записан результат
                # получаем новый поток
                Add.addProc(flagExec=-1, inputTest=testData.getStrTestData(), resFile="", taskDDS=task, pos=str(pos),
                            bytes=str(testData.getLstTestData()[pos]), timewait=self.__timeWait__)
                countRand += 1
            testData.chgValue(pos, oldVal)
            pos += 1

        self.updateRes(task)

        self.thisCalcByte = self.getMaxCountByte()
        testData.saveBaseToFile()
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name : self.name,
            jsonWord.type : jsonWord.mMoreOneRand,
            jsonWord.mTimeWait : self.__timeWait__,
            jsonWord.mCountProc : self.__countProc__,
            jsonWord.mPosStart : self.__posStart,
            jsonWord.mPosEnd : self.__posEnd,
            jsonWord.mCountRandom: self.__countOneRand
        }
        return data

    def getMaxCountByte(self):
        return (self.__posEnd + 1 - self.__posStart)

    def getPosStart(self):
        return self.__posStart

    def getPosEnd(self):
        return self.__posEnd

    def setPosStart(self, startPos):
        self.__posStart = startPos


    def setPosEnd(self, endPos):
        self.__posEnd = endPos