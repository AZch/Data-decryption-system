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

class MReverse(Method):

    def __init__(self, name, timeSleep, posStart, posEnd, countProc, timeWait):
        super().__init__(name=name, countProc=countProc, timeWait=timeWait)
        self.__timeSleep = timeSleep
        self.__posStart = posStart
        self.__posEnd = posEnd

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

        posByteSave = 0 # содержат позицию байтов, которые поток проверяет (для последнего шага проверки)
        pos = self.__posStart
        while pos <= self.__posEnd and pos < len(testData.getLstTestData()):
            posByteSave = pos
            self.thisCalcByte = pos - self.__posStart
            testData.reverseDot(pos) # изменяем данные в одной позиции
            self._resStrData = "" # обнуляем строку с даннымии в которую будет записан результат
            # получаем новый поток
            Add.addProc(flagExec=-1, inputTest=testData.getStrTestData(), resFile="", taskDDS=task, pos=str(pos),
                        bytes=str(testData.getLstTestData()[pos]), timewait=self.__timeWait__)
            # proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
            #                         testData=testData, byte=testData.getLstTestData()[pos],
            #                         bytePos=pos, isBase=False)
            # proc.start() # запускаем поток (запускается бат файл и формируется список результатов)
            testData.reverseDot(pos)
            pos += 1

        self.updateRes(task)
        # while len(Select.selectProcByFlagIdOnly(-1, task)) > 0 or len(Select.selectProcByFlagIdOnly(0, task)) > 0:
        #     self.thisCalcByte = len(Select.selectProcByFlagIdOnly(1, task)) - 1
        #     pass
        # allRes = Select.selectProcByFlagIdOnly(1, task)
        # # дожидаемся последний поток
        # for oneRes in allRes:
        #     self.addRes(notes=self.compareData(position=oneRes.pos,
        #                                                      byte=oneRes.bytes,
        #                                                      resData=oneRes.resFile))  # добавлем различия
        self.thisCalcByte = self.getMaxCountByte()
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

    def getPosStart(self):
        return self.__posStart

    def getPosEnd(self):
        return self.__posEnd

    def setPosStart(self, startPos):
        self.__posStart = startPos


    def setPosEnd(self, endPos):
        self.__posEnd = endPos