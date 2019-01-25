import threading

from Methods.Method import Method
from FactoryMethods.FactoryMethodCheck import FactoryMethodCheck
from FactoryMethods.FactoryMBruteForce import FactoryMBruteForce
from FactoryMethods.FactoryMCompBase import FactoryMCompBase
from FactoryMethods.FactoryMRandom import FactoryMRandom
from FactoryMethods.FactoryMethod import FactoryMethod
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
        self.testDataWay=""
        self.execFileName = ""
        self.currThread = None

    """ 1. работа с данными """
    ''' 1.1. загрузка '''
    def loadData(self, data, fileWay):
        self.testDataWay=fileWay
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

    def setFactoryBruteForce(self):
        try:
            self.factoryMethods = FactoryMBruteForce()
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    def setFactoryRandom(self):
        try:
            self.factoryMethods = FactoryMRandom()
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    def setFactoryCompBase(self):
        try:
            self.factoryMethods = FactoryMCompBase()
            return StrRetConts.retGood
        except:
            return StrRetConts.retBat

    def clearFactory(self):
        self.factoryMethods = None

    """ 4. работа с методами """
    ''' 4.1. создание методов '''
    def createMethod(self, nameMethod):
        if (not isinstance(self.factoryMethods, FactoryMethod)):
            print("Не правильный формат фабрики метода")
            return StrRetConts.retBat
        self.__addMethod(method=self.factoryMethods.createMethod(param=nameMethod))

    def getMaxCountByte(self):
        return self.currMethod.getMaxCountByte()

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
            self.currThread = threading.Thread(target=self.currMethod.calc, args=[self.currTestData, self.resDataWay, self.execFileName])
            self.currThread.start()
            #self.currMethod.calc(self.currTestData, self.resDataWay, self.execFileName)
            return StrRetConts.retGood
        else:
            print("Неверный формат метода")
            return StrRetConts.retBat

    def checkEndCalc(self):
        return self.currThread.isAlive()

    def getThisCalcByte(self):
        return self.currMethod.getThisCalcByte()

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
    def loadJSONMethods(self, dataStr):
        try:
            if dataStr[jsonWord.method] != None:
                self.__parseOneMethod(dataStr=dataStr[jsonWord.method])
        except:
            countMethod = 1
            try:
                while dataStr[jsonWord.method + str(countMethod)] != None:
                    self.__parseOneMethod(dataStr=dataStr[jsonWord.method + str(countMethod)][jsonWord.method])
                    countMethod += 1
                    try:
                        dataStr[jsonWord.method + str(countMethod)]
                    except:
                        return StrRetConts.retGood
            except:
                return StrRetConts.retGood

    ''' 4.4. загрузка метода(ов) из json файла '''
    def loadJSONFiles(self, dataStr):
        try:
            loadFile = open(dataStr[jsonWord.testFile], 'r')
            with loadFile:
                data = loadFile.read()
                self.loadData(data=data, fileWay=dataStr[jsonWord.testFile])
        except:
            pass
        try:
            self.execFileName = dataStr[jsonWord.execFile]
        except:
            pass
        try:
            self.resDataWay = dataStr[jsonWord.endResFile]
        except:
            pass

    ''' загрузка одного метода '''
    def __parseOneMethod(self, dataStr):
        if dataStr[jsonWord.type] == jsonWord.mCheck:
            self.factoryMethods = FactoryMethodCheck()
            self.__addMethod(self.factoryMethods.createMethod([dataStr[jsonWord.name], dataStr[jsonWord.mCountProc],
                                                             dataStr[jsonWord.mPosStart], dataStr[jsonWord.mPosEnd],
                                                             dataStr[jsonWord.mTimeSleep], dataStr[jsonWord.mTimeWait]]))
        elif dataStr[jsonWord.type] == jsonWord.mBruteForce:
            self.factoryMethods = FactoryMBruteForce()
            lst = list()
            lst.extend(
                int(strPos) for strPos in dataStr[jsonWord.mLstPosition].split())
            self.__addMethod(self.factoryMethods.createMethod([dataStr[jsonWord.name], dataStr[jsonWord.mCountProc],
                                                               dataStr[jsonWord.mTimeWait], lst, dataStr[jsonWord.mCountForce]]))
        elif dataStr[jsonWord.type] == jsonWord.mRand:
            self.factoryMethods = FactoryMRandom()
            lst = list()
            lst.extend(
                int(strPos) for strPos in dataStr[jsonWord.mLstPosition].split())
            self.__addMethod(self.factoryMethods.createMethod([dataStr[jsonWord.name], dataStr[jsonWord.mCountProc],
                                                               dataStr[jsonWord.mTimeWait], lst,
                                                               dataStr[jsonWord.mCountRandom]]))
        elif dataStr[jsonWord.type] == jsonWord.mCompBase:
            self.factoryMethods = FactoryMCompBase()
            self.__addMethod(self.factoryMethods.createMethod([dataStr[jsonWord.name], dataStr[jsonWord.mTimeWait]]))
        else:
            print("Данного метода еще нету")

    ''' 4.4. получить имя текущего метода '''
    def getNameThisMethod(self):
        try:
            return self.currMethod.getName()
        except:
            return "NO"

    def getTimeWaitThisMethod(self):
        try:
            return self.currMethod.getTimeWait()
        except:
            return 0

    def getPosStartThisMethod(self):
        try:
            return self.currMethod.getPosStart()
        except:
            return -1

    def getPosEndThisMethod(self):
        try:
            return self.currMethod.getPosEnd()
        except:
            return -1

    def getRandomPosThisMethod(self):
        try:
            return self.currMethod.getLstPosRand()
        except:
            return -1

    def getCountRandThisMethod(self):
        try:
            return self.currMethod.getCountRand()
        except:
            return -1

    def getBFPosThisMethod(self):
        try:
            return self.currMethod.getLstPosBruteForce()
        except:
            return -1

    def getCountBFThisMethod(self):
        try:
            return self.currMethod.getCountForce()
        except:
            return -1

    def setNameThisMethod(self, name):
        try:
            return self.currMethod.setName(name)
        except:
            return "NO"

    def setTimeWaitThisMethod(self, timeWait):
        try:
            return self.currMethod.setTimeWait(timeWait)
        except:
            return -1

    def setPosStartThisMethod(self, posStart):
        try:
            return self.currMethod.setPosStart(posStart)
        except:
            return -1

    def setPosEndThisMethod(self, posEnd):
        try:
            return self.currMethod.setPosEnd(posEnd)
        except:
            return -1

    def setRandomPosThisMethod(self, lstRandPos):
        try:
            return self.currMethod.setLstPosRand(lstRandPos)
        except:
            return -1

    def setCountRandThisMethod(self, countRand):
        try:
            return self.currMethod.setCountRand(countRand)
        except:
            return -1

    def setBFPosThisMethod(self, BFPos):
        try:
            return self.currMethod.setLstPosBruteForce(BFPos)
        except:
            return -1

    def setCountBFThisMethod(self, CountBF):
        try:
            return self.currMethod.setCountForce(CountBF)
        except:
            return -1

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

    def exportAllMethods(self):
        if self.currMethod == None:
            return {}
        currMethod = self.currMethod
        self.goStartMethod()
        countMethods = 1
        data = {}
        data[jsonWord.method + str(countMethods)] = self.exportMethod()
        while self.goNextMethod() != StrRetConts.retBat:
            countMethods += 1
            data[jsonWord.method + str(countMethods)] = self.exportMethod()
        self.currMethod = currMethod
        return data

    ''' 5.3. сохрание входных данных в файл '''
    def saveResData(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getResData(), Data)):
                return self.currMethod.makeReport()
            else:
                print("Неверный формат результирующих данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat

    ''' 5.3. сохрание входных данных в файл '''
    def dataForTable(self):
        if (isinstance(self.currMethod, Method)):
            if (isinstance(self.currMethod.getResData(), Data)):
                return self.currMethod.getResData().makeStrData()
            else:
                print("Неверный формат результирующих данных")
        else:
            print("Неверный формат метода")
        return StrRetConts.retBat

    def saveResDataByte(self):
        return self.currTestData.getStrTestData()


