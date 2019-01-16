from Methods.IMethod import IMethod
from Data.Note import Note

class Method(IMethod):
    def __init__(self, name):
        self.nextMethod = None
        self.prevMethod = None
        self.resData = None
        self.__resStrData = ""
        self.__baseResData = ""
        self.name = name
        pass

    def compareData(self, position, byte):
        resStrData = self.__baseResData.split('\n')
        compStrData = self.__resStrData.split('\n')
        noteCompare = list()
        i = 0
        while i < len(resStrData) and i < len(compStrData):
            if (resStrData[i] != compStrData[i]):
                splitOneStrData = compStrData[i].split('│')
                nameFunction = ""
                resFunction = ""
                try:
                    nameFunction += splitOneStrData[0]
                    resFunction += splitOneStrData[i + 1] + " Дата: "
                    resFunction += splitOneStrData[i + 2]
                except:
                    nameFunction += 'error'
                    resFunction += 'error'
                nameFunction = nameFunction.translate({ord(char): None for char in '\n'})
                resFunction = resFunction.translate({ord(char): None for char in '\n'})
                noteCompare.append(Note(nameFunction=nameFunction, resFunction=resFunction,  # добавляем новую запись
                                         lstBit=[byte], lstPosition=[position]))
        return noteCompare

    def setResData(self, data):
        self.__resStrData = data

    def addRes(self, notes):
        for note in notes:
            self.resData.addOneNote(note)

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
