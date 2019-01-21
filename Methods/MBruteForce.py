from Methods.Method import Method
from Data.TestData import TestData
from Data.Data import Data
from ObjectPool.ExecProcPool import ExecProcPool
from Constants import jsonWord

class MBruteForce(Method):
    def __init__(self, name, countProc, timeWait, lstPosBruteForce, countForce):
        super().__init__(name, countProc, timeWait)
        self.__lstPosBruteForce = lstPosBruteForce
        self.__countForce = countForce

    def calc(self, data, resFileWay, execFileWay):
        if (not isinstance(data, TestData)):
            print("Неверный формат входных данных")
            return 0

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__) # инициализируем заданное количество процессов
        isBaseData = self.__getBaseData__(execProcPool=execProcPool, execFileWay=execFileWay,
                                          resFileWay=resFileWay, testData=data, isBase=False)
        if isBaseData == 0:
            return isBaseData

        # запоминаем все начальные значения
        lstStartValue = list()
        for onePos in self.__lstPosBruteForce:
            lstStartValue.append(data.getLstTestData()[onePos])

        # пока на последнем элементе не сделаем цикла, что вернят нас к началу и будет означать перебор всех элементов
        isLastCycle = False
        countForce = 0
        while not isLastCycle:
            if self.__countForce > 0 and countForce > self.__countForce:
                break
            else:
                countForce += 1
            print(data.getByteByPos(self.__lstPosBruteForce))
            i = 0
            while i < len(self.__lstPosBruteForce):
               data.incDot(self.__lstPosBruteForce[i])
               # если новое инкрементированное значение совпадает с начальным на этой позиции
               if data.getLstTestData()[self.__lstPosBruteForce[i]].upper() != lstStartValue[i].upper():
                   break
               elif i == len(self.__lstPosBruteForce) - 1:
                   isLastCycle = True
               i += 1
            if isLastCycle: # сразу выходим, чтобы еще раз не прогонять программу
                break
            self._resStrData = ""  # обнуляем строку с даннымии в которую будет записан результат
            proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
                                    testData=data, byte=0,
                                    bytePos=0, isBase=False)
            proc.start()  # запускаем поток (запускается бат файл и формируется список результатов)
            while self.addByPosRes(execProcPool.wait()) == 'wait':  # ожидаем пока не будет доступен поток
                pass
            self.addByPosRes(notes=self.compareData(position=self.__lstPosBruteForce, byte=data.getByteByPos(self.__lstPosBruteForce)))  # добавлем различия

        i = 0
        for onePos in self.__lstPosBruteForce:
            data.chgValue(hex(onePos)[2:], lstStartValue[i])
            i += 1
        data.saveBaseToFile()
        self.thisCalcByte = self.getMaxCountByte()
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name: self.name,
            jsonWord.type: jsonWord.mBruteForce,
            jsonWord.mTimeWait: self.__timeWait__,
            jsonWord.mCountProc: self.__countProc__,
            jsonWord.mLstPosition: ' '.join(str(pos) for pos in self.__lstPosBruteForce),
            jsonWord.mCountForce:self.__countForce
        }
        return data

    def makeReport(self):
        resStr = "Отчет: \n"
        for note in self.resData.getData():
            resStr += "Позиции=байты: \n"
            for i in range(len(note.lstBit)):
                resStr += str(note.lstPosition[i]) + " = " + str(note.lstBit[i]) + ","
            resStr = resStr[:-1] + "\n" + "Функции:\n"
            splitFun = note.nameFunction.split('/')
            splitRes = note.resFunction.split('/')
            countFun = len(splitFun)
            for i in range(countFun):
                resStr += splitFun[i] + "|" + splitRes[i] + "\n"
        return resStr

    def getMaxCountByte(self):
        return (self.__countForce)