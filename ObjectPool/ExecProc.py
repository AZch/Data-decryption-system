import random
import re
import subprocess
from Data.Note import Note
from threading import Thread
import time
from Methods.Method import Method

class ExecProc(Thread):
    def __init__(self, execFile, resFile, bytePos, byte, method, pool):
        Thread.__init__(self)
        self.execFile = execFile
        self.resFile = resFile
        self.__bytePos = bytePos
        self.__byte = byte
        self.method = method
        self.pool = pool
        self.startTime = time.time()
        self.__isAdd = True

    def dontAdd(self):
        self.__isAdd = False

    def whatSecWork(self):
        return int(time.time() - self.startTime)

    def setNewData(self, execFile, resFile, bytePos, byte):
        self.execFile = execFile
        self.resFile = resFile
        self.__bytePos = bytePos
        self.__byte = byte
        self.startTime = time.time()

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

    # def getLstNote(self):
    #     return self.lstNote

    def run(self):
        self.startTime = time.time() # запоминем время старта потока
        proc = subprocess.Popen( # запускаем переданный файл
            self.execFile,
            cwd=self.execFile.split(
                "/" + self.execFile.split('/')[len(self.execFile.split('/')) - 1]
            )[0],
            creationflags=subprocess.CREATE_NEW_CONSOLE)
        proc.wait() # ждем пока программа отработает и выдаст результат
        if (self.__isAdd):
            self.method.addBytePos(self.__byte, self.__bytePos)
        #timeSleep = random.randint(1, 11)
        #print(timeSleep)
        #time.sleep(timeSleep)

        # dataStr = self.getStrFromFile(self.resFile) # получаем результат (функции, которые изменились)
        # self.lstNote = []
        # for oneData in list(filter(None, dataStr.split('\n'))):
        #     splitOneData = oneData.split('│')
        #     i = 0
        #     nameFunction = ""
        #     resFunction = ""
        #     try:
        #         while (i < len(splitOneData)):
        #             nameFunction += splitOneData[i]
        #             resFunction += splitOneData[i + 1]
        #             resFunction += splitOneData[i + 2]
        #             i += 3
        #     except:
        #         nameFunction += 'error'
        #         resFunction += 'error'
        #     nameFunction = nameFunction.translate({ord(char): None for char in '\n'})
        #     resFunction = resFunction.translate({ord(char): None for char in '\n'})
        #     self.lstNote.append(Note(nameFunction=nameFunction, resFunction=resFunction, # добавляем новую запись
        #                              lstBit=[self.__byte], lstPosition=[self.__bytePos]))
        # self.method.addRes(notes=self.lstNote) # добавлем их к вызванному методу
        # file = open(self.resFile, 'w') # очищаем файл с результатом
        # file.write("")
        # file.close()
        self.pool.returnProc(proc=self) # завершаем процесс
        #return lstNote

    def clone(self):
        return ExecProc(execFile=self.execFile, resFile=self.resFile, bytePos=self.__bytePos,
        byte=self.__byte, method=self.method, pool=self.pool)
