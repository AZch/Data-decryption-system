from Methods.IMethod import IMethod

class Method(IMethod):
    def __init__(self, data):
        self.nextMethod = None
        self.prevMethod = None
        self.data = data
        self.resData = None
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
            self.nextMethod.__setSimplePrev(method=self)
        else:
            bufMethod = self.nextMethod
            while (bufMethod.isNext()):
                bufMethod = bufMethod.next()
            bufMethod.setNext(method=method)
            method.__setSimplePrev(method=bufMethod)

    def __setSimpleNext(self, method): # простое задание следующего метода
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

    def __setSimplePrev(self, method): # простое задание предыдущего метода
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
            self.prevMethod.__setSimpleNext(method=self)
        else:
            bufMethod = self.prevMethod
            while (bufMethod.isPrev()):
                bufMethod = bufMethod.prev()
            bufMethod.setPrev(method=method)
            method.__setSimpleNext(method=bufMethod)

    def getData(self):
        return self.data

    def getResData(self):
        return self.resData


