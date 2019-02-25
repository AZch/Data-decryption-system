from abc import ABC, abstractmethod

class IData(ABC):
    @abstractmethod
    def loadData(self, strData):
        pass

    @abstractmethod
    def makeStrData(self):
        pass

    @abstractmethod
    def getData(self):
        pass

    @abstractmethod
    def makeLstTestData(self):
        pass

    @abstractmethod
    def makeStrTestData(self):
        pass

    @abstractmethod
    def searchForNameFunc(self, nameSearch):
        pass

    @abstractmethod
    def addOneNote(self, note):
        pass

    @abstractmethod
    def addSimpleOneNote(self, note):
        pass