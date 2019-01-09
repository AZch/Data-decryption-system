from abc import ABC, abstractmethod

class IMethod(ABC):
    # должен заполнять resData
    @abstractmethod
    def calc(self, data):
        pass

    # должен возвращать формализованную строку
    @abstractmethod
    def exportJSON(self):
        pass