from Methods.IMethod import IMethod

class Method(IMethod):
    def __init__(self, name):
        self.nextMethod = None
        self.prevMethod = None
        self.resData = None
        self.name = name
        pass



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
