from abc import ABC, abstractmethod

class IMethod(ABC):
    # должен заполнять resData
    @abstractmethod
    def calc(self, data, resFileWay, execFileWay):
        pass

    # должен возвращать формализованную строку
    @abstractmethod
    def exportJSON(self):
        pass

    @abstractmethod
    def makeReport(self):
        pass

    @abstractmethod
    def getMaxCountByte(self):
        pass