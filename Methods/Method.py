import time

from Methods.IMethod import IMethod
from Data.Note import Note
from DataDB.GRUD import *

class Method(IMethod):
    def __init__(self, name, countProc, timeWait):
        self.nextMethod = None
        self.prevMethod = None
        self.resData = None
        self._resStrData = ""
        self._baseResData = ""
        self.name = name
        self.__countProc__ = countProc
        self.__timeWait__ = timeWait
        self.thisCalcByte = 0
        pass

    def getThisCalcByte(self):
        return self.thisCalcByte

    def __getBaseData__(self, task, testData, isBaseData):
        if not isBaseData:
            Add.addProc(flagExec=-1, inputTest=testData.getBaseStrTestData(), resFile="", taskDDS=task, pos="", bytes="", timewait=self.__timeWait__)
        else:
            Add.addProc(flagExec=-1, inputTest=testData.getStrTestData(), resFile="", taskDDS=task, pos="-1", bytes="", timewait=self.__timeWait__)
        while True:
            retData = Select().selectProcByFlagId(1, task, bytes="", pos="")
            if len(retData) > 0:
                break
        print([data.idProc for data in retData])
        self._resStrData = retData[0].resFile
        Update.updProc(retData[0].idProc, flagExec=2, inputTest=retData[0].inputTest,
                       resFile=retData[0].resFile,
                       pos=retData[0].pos, bytes=retData[0].bytes, timewait=retData[0].timewait)

        if self._resStrData == "":
            print("Файл не отработал успешно на пустом результате")
            return 0
        self._baseResData = self._resStrData
        return self._baseResData

    def __getProc__(self, procPool, execFileWay, resFileWay, testData, bytePos, byte, isBase):
        proc = 'wait'
        while proc == 'wait':
            proc = procPool.getProc(execFile=execFileWay, resFile=resFileWay,  # инициализуем поток
                                        bytePos=bytePos,
                                        byte=byte,
                                        method=self, testData=testData,
                                        isBaseFile=isBase)
        return proc

    def updateRes(self, task):
        while len(Select.selectProcByFlagIdOnly(-1, task)) > 0 or len(Select.selectProcByFlagIdOnly(0, task)) > 0:
            allExec = Select.selectProcByFlagIdOnly(0, task)
            for oneExec in allExec:
                if time.time() - oneExec.startTime > self.__timeWait__ * 2:
                    Update.updProc(oneExec.idProc, flagExec=-1, inputTest=oneExec.inputTest,
                                   resFile=oneExec.resFile,
                                   pos=oneExec.pos, bytes=oneExec.bytes, timewait=oneExec.timewait)
            self.thisCalcByte = len(Select.selectProcByFlagIdOnly(2, task)) - 1
            allRes = Select.selectProcByFlagIdOnly(1, task)
            for oneRes in allRes:
                self.addByPosRes(notes=self.compareData(position=oneRes.pos,
                                                        byte=oneRes.bytes,
                                                        resData=oneRes.resFile))  # добавлем различия
                Update.updProc(oneRes.idProc, flagExec=2, inputTest=oneRes.inputTest,
                               resFile=oneRes.resFile,
                               pos=oneRes.pos, bytes=oneRes.bytes, timewait=oneRes.timewait)
            time.sleep(5)
            pass
        allRes = Select.selectProcByFlagIdOnly(1, task)
        for oneRes in allRes:
            self.addByPosRes(notes=self.compareData(position=oneRes.pos,
                                                    byte=oneRes.bytes,
                                                    resData=oneRes.resFile))  # добавлем различия
            Update.updProc(oneRes.idProc, flagExec=2, inputTest=oneRes.inputTest,
                           resFile=oneRes.resFile,
                           pos=oneRes.pos, bytes=oneRes.bytes, timewait=oneRes.timewait)
        # дожидаемся последний поток

    def compareData(self, position, byte, resData):
        resStrData = self._baseResData.split('\n')
        compStrData = resData.split('\n')
        noteCompare = list()
        i = 0
        while i < len(resStrData) and i < len(compStrData):
            if resData == 'nope':
                posInt = list()
                for onePos in position.split(' '):
                    posInt.append(onePos)
                noteCompare.append(Note(nameFunction="too long wait", resFunction="too long wait",  # добавляем новую запись
                                        lstBit=byte.split(' '), lstPosition=posInt))
                return noteCompare
            else:
                if (resStrData[i] != compStrData[i]):
                    splitOneStrData = compStrData[i].split('│')
                    nameFunction = ""
                    resFunction = ""
                    try:
                        nameFunction += splitOneStrData[0]
                        resFunction += splitOneStrData[1] + " Дата: "
                        resFunction += splitOneStrData[2]
                    except:
                        nameFunction += 'error'
                        resFunction += 'error'
                    nameFunction = nameFunction.translate({ord(char): None for char in '\n'})
                    resFunction = resFunction.translate({ord(char): None for char in '\n'})
                    posInt = list()
                    for onePos in position.split(' '):
                        posInt.append(onePos)
                    noteCompare.append(Note(nameFunction=nameFunction, resFunction=resFunction,  # добавляем новую запись
                                             lstBit=byte.split(' '), lstPosition=posInt))
                i += 1
        return noteCompare

    def setResData(self, data):
        self._resStrData = data

    def addRes(self, notes):
        if notes == 'wait':
            return notes

        for note in notes:
            self.resData.addOneNote(note)

    def addByPosRes(self, notes):
        if notes == 'wait':
            return notes
        try:
            resNote = Note("", "", notes[0].lstBit, notes[0].lstPosition)
            for note in notes:
                resNote.nameFunction += note.nameFunction + "/"
                resNote.resFunction += note.resFunction + "/"
            self.resData.addSimpleOneNote(resNote)
        except:
            pass

    # работа со следующими методами
    def next(self): # получить следующий метод
        return self.nextMethod

    def isNext(self): # проверить наличие следующего метода
        if (self.nextMethod != None):
            return True
        else:
            return False

    def setNext(self, method): # задать следующий метод
        if (not isinstance(method, Method)):
            print("Не правильный формат метода")
            pass

        if (self.nextMethod == None):
            self.nextMethod = method
            self.nextMethod.setSimplePrev(method=self)
        else:
            bufMethod = self.nextMethod
            while (bufMethod.isNext()):
                bufMethod = bufMethod.next()
            bufMethod.setNext(method=method)
            method.setSimplePrev(method=bufMethod)
        return method

    def setSimpleNext(self, method): # простое задание следующего метода
        if (not isinstance(method, Method)):
            print("Не правильный формат метода")
            pass
        self.nextMethod = method

    # работа с предыдущими методами
    def prev(self): # получить предыдущий метод
        return self.prevMethod

    def isPrev(self): # проверить наличие предыдущего метода
        if (self.prevMethod != None):
            return True
        else:
            return False

    def setSimplePrev(self, method): # простое задание предыдущего метода
        if (not isinstance(method, Method)):
            print("Не правильный формат метода")
            pass
        self.prevMethod = method

    def setPrev(self, method): # задать предыдущий метод
        if (not isinstance(method, Method)):
            print("Не правильный формат метода")
            pass

        if (self.prevMethod == None):
            self.prevMethod = method
            self.prevMethod.setSimpleNext(method=self)
        else:
            bufMethod = self.prevMethod
            while (bufMethod.isPrev()):
                bufMethod = bufMethod.prev()
            bufMethod.setPrev(method=method)
            method.setSimpleNext(method=bufMethod)
        return method

    def getResData(self):
        return self.resData

    def getName(self):
        return self.name

    def getTimeWait(self):
        return self.__timeWait__

    def setName(self, name):
        self.name = name

    def setTimeWait(self, timeWait):
        self.__timeWait__ = timeWait
