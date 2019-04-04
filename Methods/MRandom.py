from Methods.Method import Method
from Data.TestData import TestData
from Data.Data import Data
from ObjectPool.ExecProcPool import ExecProcPool
from Constants import jsonWord
from DataDB.GRUD import *

class MRandom(Method):
    def __init__(self, name, countProc, timeWait, lstPosRand, countRand):
        super().__init__(name, countProc, timeWait)
        self.__lstPosRand = lstPosRand
        self.__countRand = countRand

    def calc(self, data, resFileWay, execFileWay):
        if (not isinstance(data, TestData)):
            print("Неверный формат входных данных")
            return 0
        task = Add.addTask(method=jsonWord.mRand, userName="")

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__) # инициализируем заданное количество процессов
        #isBaseData = self.__getBaseData__(execProcPool=execProcPool, execFileWay=execFileWay,
        #                                  resFileWay=resFileWay, testData=data, isBase=False)
        isBaseData = self.__getBaseData__(task, data, False)
        if isBaseData == 0:
            return isBaseData

        # запоминаем все начальные значения
        lstStartValue = list()
        for onePos in self.__lstPosRand:
            lstStartValue.append(data.getLstTestData()[onePos])

        self.thisCalcByte = 0
        while self.thisCalcByte < self.__countRand:
            print(data.getByteByPos(self.__lstPosRand))
            i = 0
            while i < len(self.__lstPosRand):
               data.randVal(hexPos=hex(self.__lstPosRand[i]))
               i += 1
            self._resStrData = ""  # обнуляем строку с даннымии в которую будет записан результат
            # proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
            #                         testData=data, byte=0,
            #                         bytePos=0, isBase=False)
            # proc.start()  # запускаем поток (запускается бат файл и формируется список результатов)
            # while self.addByPosRes(execProcPool.wait()) == 'wait':  # ожидаем пока не будет доступен поток
            #     pass
            # self.addByPosRes(notes=self.compareData(position=self.__lstPosRand, byte=data.getByteByPos(self.__lstPosRand)))  # добавлем различия
            Add.addProc(flagExec=-1, inputTest=data.getStrTestData(), resFile="", taskDDS=task,
                        pos=' '.join(str(pos) for pos in self.__lstPosRand),
                        bytes=' '.join(str(byte) for byte in data.getByteByPos(self.__lstPosRand)), timewait=self.__timeWait__)
            self.thisCalcByte += 1
        i = 0
        for onePos in self.__lstPosRand:
            data.chgValue(hex(onePos)[2:], lstStartValue[i])
            i += 1
        data.saveBaseToFile()

        self.updateRes(task)
        # while len(Select.selectProcByFlagIdOnly(-1, task)) > 0 or len(Select.selectProcByFlagIdOnly(0, task)) > 0:
        #     self.thisCalcByte = len(Select.selectProcByFlagIdOnly(1, task)) - 1
        #     pass
        # allRes = Select.selectProcByFlagIdOnly(1, task)
        # # дожидаемся последний поток
        # for oneRes in allRes:
        #     self.addByPosRes(notes=self.compareData(position=oneRes.pos,
        #                                                      byte=oneRes.bytes,
        #                                                      resData=oneRes.resFile))  # добавлем различия

        self.thisCalcByte = self.getMaxCountByte()
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name: self.name,
            jsonWord.type: jsonWord.mRand,
            jsonWord.mTimeWait: self.__timeWait__,
            jsonWord.mCountProc: self.__countProc__,
            jsonWord.mLstPosition: ' '.join(str(pos) for pos in self.__lstPosRand),
            jsonWord.mCountRandom:self.__countRand
        }
        return data

    def makeReport(self):
        resStr = "Отчет: \n"
        for note in self.resData.getData():
            resStr += "Позиции=байты: \n"
            for i in range(len(note.lstBit)):
                resStr += str(hex(int(note.lstPosition[i]))[2:]) + " = " + str(note.lstBit[i]) + ","
            resStr = resStr[:-1] + "\n" + "Функции:\n"
            splitFun = note.nameFunction.split('/')
            splitRes = note.resFunction.split('/')
            countFun = len(splitFun)
            for i in range(countFun):
                resStr += splitFun[i] + "|" + splitRes[i] + "\n"
        return resStr

    def getMaxCountByte(self):
        return (self.__countRand)

    def getLstPosRand(self):
        return self.__lstPosRand

    def getCountRand(self):
        return self.__countRand

    def setLstPosRand(self, lstPosRand):
        self.__lstPosRand = lstPosRand

    def setCountRand(self, countRand):
        self.__countRand = countRand