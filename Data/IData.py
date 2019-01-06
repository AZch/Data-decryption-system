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