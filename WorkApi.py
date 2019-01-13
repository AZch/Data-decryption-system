from Methods.Method import Method
from FactoryMethods.FactoryMethodCheck import FactoryMethodCheck
from Data.Data import Data
from Data.TestData import TestData
from Constants import StrRetConts
from Constants import jsonWord

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
    def __init__(self):
        self.startMethod = None    # 1. начальный метод
        self.currMethod = None     # 2. текущий метод
        #self.baseData = baseData   # 3. стандартные тестовые данные
        self.currTestData = None       # 4. текущие введенные данные
        self.factoryMethods = None # 5. фабрика для создания методов
        self.resDataWay = ""
        self.execFileName = ""

    """ 1. работа с данными """
    ''' 1.1. загрузка '''
    def loadData(self, data, fileWay):
        self.currTestData = TestData(testFileWay=fileWay)
        self.currTestData.loadData(strData=data)
        return StrRetConts.retGood

    ''' 1.2. сохранение '''
    def saveData(self):
        return self.currTestData.getStrTestData()

    ''' 1.3. очистка '''
    def clearCurrTestData(self):
        self.currTestData.loadData("")
        return StrRetConts.retGood

    def setWayResData(self, wayFile):
        self.resDataWay = wayFile

    def setExecFileName(self, wayFile):
        self.execFileName = wayFile

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

    def clearFactory(self):
        self.factoryMethods = None

    """ 4. работа с методами """
    ''' 4.1. создание методов '''
    def createMethod(self, nameMethod):
        if (not isinstance(self.factoryMethods, FactoryMethodCheck)):
            print("Не правильный формат фабрики метода")
            return StrRetConts.retBat
        self.__addMethod(method=self.factoryMethods.createMethod(param=nameMethod))
        # try:
        #     if (self.currMethod == None):
        #         self.startMethod = self.factoryMethods.createMethod(name=nameMethod)
        #         self.currMethod = self.startMethod
        #     else:
        #         newMethod = self.factoryMethods.createMethod(name=nameMethod)
        #         self.currMethod.setNext(newMethod)
        #         self.currMethod = newMethod
        #     return StrRetConts.retGood
        # except:
        #     return StrRetConts.retBat

    def __addMethod(self, method):
        try:
            if (self.currMethod == None):
                self.startMethod = method
                self.currMethod = method
            else:
                newMethod = method
                self.currMethod.setNext(newMethod)
                self.currMethod = newMethod
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    ''' 4.2. вычисление по методу '''
    def calcMethod(self):
        if (isinstance(self.currMethod, Method)):
            self.currMethod.calc(self.currTestData, self.resDataWay, self.execFileName)
            return self.currMethod.getResData().makeStrData()
        else:
            print("Неверный формат метода")
            return StrRetConts.retBat

    ''' 4.3. удаление метода '''
    def delMethod(self):
        if (self.currMethod == None):
            print("Нету методов")
            return StrRetConts.retBat
        try:
            if (self.currMethod.isNext() and self.currMethod.isPrev()):
                self.currMethod.next().setSimplePrev(self.currMethod.prev())
                self.currMethod.prev().setSimpleNext(self.currMethod.next())
                self.currMethod = self.currMethod.prev()
            elif (self.currMethod.isPrev()):
                self.currMethod.prev().setSimpleNext(None)
                self.currMethod = self.currMethod.prev()
            elif (self.currMethod.isNext()):
                self.currMethod.next().setSimplePrev(None)
                self.currMethod = self.currMethod.next()
            else:
                self.currMethod = None
            print("Удаление прошло успешно")
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    ''' 4.4. загрузка метода(ов) из json файла '''
    def loadJSONFile(self, dataStr):
        try:
            if dataStr[jsonWord.method] != None:
                self.__parseOneMethod(dataStr=dataStr[jsonWord.method])
        except:
            countMethod = 1
            while dataStr[jsonWord.method + str(countMethod)] != None:
                self.__parseOneMethod(dataStr=dataStr[jsonWord.method + str(countMethod)][jsonWord.method])
                countMethod += 1
                try:
                    dataStr[jsonWord.method + str(countMethod)]
                except:
                    return StrRetConts.retGood

    ''' загрузка одного метода '''
    def __parseOneMethod(self, dataStr):
        if dataStr[jsonWord.type] == jsonWord.mCheck:
            factoryMethodCheck = FactoryMethodCheck()
            self.__addMethod(factoryMethodCheck.createMethod(dataStr[jsonWord.name]))
        else:
            print("Данного метода еще нету")

    ''' 4.4. получить имя текущего метода '''
    def getNameThisMethod(self):
        try:
            return self.currMethod.getName()
        except:
            return "NO"

    ''' 4.4. получить имя следующего метода '''
    def getNameNextMethod(self):
        try:
            return self.currMethod.next().getName()
        except:
            return "NO"

    ''' 4.4. получить имя предыдущего метода '''
    def getNamePrevMethod(self):
        try:
            return self.currMethod.prev().getName()
        except:
            return "NO"

    """ 5. экспорт метода и сохранение входных и выходных данных """
    ''' 5.1. экспорт метода '''
    def exportMethod(self):
        if (isinstance(self.currMethod, Method)):
            return self.currMethod.exportJSON()
        else:
            print("Неверный формат метода")
            return StrRetConts.retBat

    ''' 5.3. сохрание входных данных в файл '''
    def saveResData(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getResData(), Data)):
                print(self.currMethod.getResData().makeStrData())
                return self.currMethod.getResData().makeStrData()
            else:
                print("Неверный формат результирующих данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat

    def saveResDataByte(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getResData(), Data)):
                print(self.currMethod.getResData().makeStrTestData())
                return self.currMethod.getResData().makeStrTestData()
            else:
                print("Неверный формат результирующих данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat
