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

    def __init__(self, name, timeSleep, countRow, countProc):
        super().__init__(name=name)
        self.__timeSleep = timeSleep
        self.__countRow = countRow
        self.__countProc = countProc
        pass

    def getStrFromFile(self, fileWay):
        try:
            file = open(fileWay, 'r', encoding='cp866')
            if file == '':
                return fileWay + " not open"
            with file:
                data = file.read()
                return data
        except:
            return fileWay + " not open"

    def calc(self, testData, resFileWay, execFileWay):
        print(self.name)
        if (not isinstance(testData, TestData)):
            print("Неверный формат входных данных")
            return 0

        self.resData = Data() # инициализирем объект данных для результата
        execProcPool = ExecProcPool(self.__countProc) # инициализируем заданное количество процессов
        proc = None
        for x in range(self.__countRow):#range(len(testData.getLstTestData())):
            for y in range(len(testData.getLstTestData()[x])):
                testData.incDot(x, y) # изменяем данные в одной позиции
                testData.saveToFile() # сохраняем измененные данные во входной файл
                proc = 'wait'
                while proc == 'wait': # ждем пока не получим свободный поток
                    proc = execProcPool.getProc(execFile=execFileWay, resFile=resFileWay, # инициализуем поток
                                         bytePos=x * len(testData.getLstTestData()[x]) + y, byte=testData.getLstTestData()[x][y],
                                                method=self)
                proc.start() # запускаем поток (запускается бат файл и формируется список результатов)
                time.sleep(self.__timeSleep) # ждем запуска окна паузой
                testData.decDot(x, y)
        testData.saveToFile() # сохраняем последний раз файл с правильными данными
        proc.join() # дожидаемся последний поток

        dataStr = self.getStrFromFile(resFileWay)  # получаем результат (функции, которые изменились)
        countRes = 0
        for oneData in list(filter(None, dataStr.split('new\n'))):
            for strForNew in list(filter(None, oneData.split('\n'))):
                splitOneData = strForNew.split('│')
                i = 0
                nameFunction = ""
                resFunction = ""
                try:
                    while (i < len(splitOneData)):
                        nameFunction += splitOneData[i]
                        resFunction += splitOneData[i + 1]
                        resFunction += splitOneData[i + 2]
                        i += 3
                except:
                    nameFunction += 'error'
                    resFunction += 'error'
                nameFunction = nameFunction.translate({ord(char): None for char in '\n'})
                resFunction = resFunction.translate({ord(char): None for char in '\n'})
                self.resData.addOneNote(Note(nameFunction=nameFunction, resFunction=resFunction,  # добавляем новую запись
                                         lstBit=[self.bytePosForRes[countRes].split(' == ')[0]], lstPosition=[int(self.bytePosForRes[countRes].split(' == ')[1])]))
            countRes += 1

        if countRes + 1 != len(self.bytePosForRes):
            print('not good')
        #self.method.addRes(notes=self.lstNote)  # добавлем их к вызванному методу
        file = open(resFileWay, 'w', encoding='cp866')  # очищаем файл с результатом
        file.write("")
        file.close()

        return self.resData

    def __randomstr(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name : self.name,
            jsonWord.type : jsonWord.mCheck,
            #jsonWord.startTime : self.start,
            #jsonWord.endTime : self.end
        }
        return data