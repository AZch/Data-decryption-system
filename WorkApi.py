from Methods.Method import Method
from FactoryMethods.FactoryMethodCheck import FactoryMethodCheck
from Data.Data import Data
from Constants import StrRetConts

"""
    API предоставляющие взаимодейтсвие со всей системой
    пристуствуют объекты:
    1. начальный метод
    2. текущий метод
    3. стандартные тестовые данные
    4. текущие введенные данные
    5. фабрика для создания методов
    присутствуют методы: 
    1. Работа с данными
        1.1. загрузка
        1.2. сохранение
        1.3. очистка
    2. переход между методами
        2.1. переход к начальному методу
        2.2. переход на следующий метод
        2.3. переход на предыдущий метод
    3. задание фабрик по производству методов
        3.1. фабрика по производству методов проверки
    4. работа с методами
        4.1. создание методов
        4.2. вычисление по методу
        4.3. удаление метода
    5. экспорт метода и сохранение входных и выходных данных
        5.1. экспорт метода
        5.2. сохрание входных данных в файл
        5.3. сохрание входных данных в файл
"""
class WorkApi():
    def __init__(self, baseData):
        self.startMethod = None    # 1. начальный метод
        self.currMethod = None     # 2. текущий метод
        self.baseData = baseData   # 3. стандартные тестовые данные
        self.currData = None       # 4. текущие введенные данные
        self.factoryMethods = None # 5. фабрика для создания методов

    """ 1. работа с данными """
    ''' 1.1. загрузка '''
    def loadData(self, way):
        return StrRetConts.retGood

    ''' 1.2. сохранение '''
    def saveData(self, way, data):
        return StrRetConts.retGood

    ''' 1.3. очистка '''
    def  clearCurrData(self):
        return StrRetConts.retGood

    """ 2. переход между методами """
    ''' 2.1. переход к начальному методу '''
    def goStartMethod(self):
        try:
            self.currMethod = self.startMethod
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    ''' 2.2. переход на следующий метод '''
    def goNextMethod(self):
        if (self.currMethod != None):
            if (isinstance(self.currMethod, Method)):
                if (self.currMethod.isNext()):
                    self.currMethod = self.currMethod.next()
                    return StrRetConts.retGood
                else:
                    print("Нету следующего метода")
            else:
                print("Неправильный формат данных")
        else:
            print("Нет даже текущего метода")
        return StrRetConts.retBat

    ''' 2.3. переход на предыдущий метод '''
    def goPrevMethod(self):
        if (self.currMethod != None):
            if (isinstance(self.currMethod, Method)):
                if (self.currMethod.isPrev()):
                    self.currMethod = self.currMethod.prev()
                    return StrRetConts.retGood
                else:
                    print("Нету предыдущего метода")
            else:
                print("Неправильный формат данных")
        else:
            print("Нет даже текущего метода")
        return StrRetConts.retBat

    """ 3. задание фабрик по производству методов """
    ''' 3.1. фабрика по производству методов проверки '''
    def setFactoryCheck(self):
        try:
            self.factoryMethods = FactoryMethodCheck()
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    """ 4. работа с методами """
    ''' 4.1. создание методов '''
    def createMethod(self):
        if (not isinstance(self.factoryMethods, FactoryMethodCheck)):
            print("Не правильный формат фабрики метода")
            return StrRetConts.retBat

        try:
            if (self.currMethod == None):
                if (self.currData == None):
                    self.startMethod = self.factoryMethods.createMethod(data=self.baseData)
                else:
                    self.startMethod = self.factoryMethods.createMethod(data=self.currData)
                self.currMethod = self.startMethod
            else:
                if (self.currData == None):
                    self.currMethod.s = self.factoryMethods.createMethod(data=self.baseData)
                else:
                    self.startMethod = self.factoryMethods.createMethod(data=self.currData)
                self.currMethod = self.currMethod.next()
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    ''' 4.2. вычисление по методу '''
    def calcMethod(self):
        if (isinstance(self.currMethod, Method)):
            self.currMethod.calc()
            return self.currMethod.getResData()
        else:
            print("Неверный формат метода")
            return StrRetConts.retBat

    ''' 4.3. удаление метода '''
    def delMethod(self):
        if (self.currMethod == None):
            print("Нету методов")
            return StrRetConts.retBat
        try:
            if (self.currMethod.isNext and self.currMethod.isPrev):
                self.currMethod.next().setSimplePrev(self.currMethod.prev)
                self.currMethod.prev().setSimpleNext(self.currMethod.next)
                self.currMethod = self.currMethod.prev()
            elif (self.currMethod.prev()):
                self.currMethod.prev().setSimpleNext(None)
                self.currMethod = self.currMethod.prev
            elif (self.currMethod.next):
                self.currMethod.next.setSimplePrev(None)
                self.currMethod = self.currMethod.next()
            else:
                self.currMethod = None
            print("Удаление прошло успешно")
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    """ 5. экспорт метода и сохранение входных и выходных данных """
    ''' 5.1. экспорт метода '''
    def exportMethod(self):
        if (isinstance(self.currMethod, Method)):
            print(self.currMethod.exportXMLStr())
            return StrRetConts.retGood
        else:
            print("Неверный формат метода")
            return StrRetConts.retBat

    ''' 5.2. сохрание входных данных в файл '''
    def saveInputData(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getData(), Data)):
                print(self.currMethod.getData().toStr())
                return StrRetConts.retGood
            else:
                print("Неверный формат входных данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat

    ''' 5.3. сохрание входных данных в файл '''
    def saveResData(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getResData(), Data)):
                print(self.currMethod.getResData().toStr())
                return StrRetConts.retGood
            else:
                print("Неверный формат результирующих данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat
