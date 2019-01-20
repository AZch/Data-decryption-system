from Methods.Method import Method
from Data.TestData import TestData
from Data.Data import Data
from ObjectPool.ExecProcPool import ExecProcPool
from Constants import jsonWord

class MCompBase(Method):
    def __init__(self, name, timeWait):
        super().__init__(name, 1, timeWait)

    def calc(self, data, resFileWay, execFileWay):
        if (not isinstance(data, TestData)):
            print("Неверный формат входных данных")
            return 0

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__) # инициализируем заданное количество процессов
        isBaseData = self.__getBaseData__(execProcPool=execProcPool, execFileWay=execFileWay,
                                          resFileWay=resFileWay, testData=data, isBase=True)
        if isBaseData == 0:
            return isBaseData
        execProcPool = ExecProcPool(self.__countProc__, maxWait=self.__timeWait__)  # инициализируем заданное количество процессов
        proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
                                    testData=data, byte=0,
                                    bytePos=0, isBase=False)
        proc.start()  # запускаем поток (запускается бат файл и формируется список результатов)
        while self.addRes(execProcPool.wait()) == 'wait':  # ожидаем пока не будет доступен поток
            pass
        self.addRes(notes=self.compareData(position=[], byte=[]))  # добавлем различия

        data.saveBaseToFile()
        return self.resData

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name: self.name,
            jsonWord.type: jsonWord.mCompBase,
            jsonWord.mTimeWait: self.__timeWait__
        }
        return data

    def makeReport(self):
        resStr = "Отчет: \n"
        for note in self.resData.getData():
            resStr += note.nameFunction + "|" + note.resFunction + "\n"
        return resStr