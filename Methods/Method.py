from Methods.IMethod import IMethod
from Data.Note import Note

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
        pass

    def __getBaseData__(self, execProcPool, execFileWay, resFileWay, testData):
        proc = self.__getProc__(procPool=execProcPool, execFileWay=execFileWay, resFileWay=resFileWay,
                                testData=testData, byte=0, bytePos=0)
        proc.start()
        # ожидаем завершения потока и получаем новый
        while self.addRes(execProcPool.wait()) == 'wait':
            pass

        if self._resStrData == "":
            print("Файл не отработал успешно на пустом результате")
            return 0
        self._baseResData = self._resStrData
        return self._baseResData

    def __getProc__(self, procPool, execFileWay, resFileWay, testData, bytePos, byte):
        proc = 'wait'
        while proc == 'wait':
            proc = procPool.getProc(execFile=execFileWay, resFile=resFileWay,  # инициализуем поток
                                        bytePos=bytePos,
                                        byte=byte,
                                        method=self, testData=testData)
        return proc

    def compareData(self, position, byte):
        resStrData = self._baseResData.split('\n')
        compStrData = self._resStrData.split('\n')
        noteCompare = list()
        i = 0
        while i < len(resStrData) and i < len(compStrData):
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
                noteCompare.append(Note(nameFunction=nameFunction, resFunction=resFunction,  # добавляем новую запись
                                         lstBit=byte, lstPosition=position))
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
                resNote.nameFunction += note.nameFunction + "\n"
                resNote.resFunction += note.resFunction + "\n"
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
