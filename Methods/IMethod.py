from abc import ABC, abstractmethod

class IMethod(ABC):
    # должен заполнять resData
    @abstractmethod
    def calc(self):
        pass

    # должен возвращать формализованную строку
    @abstractmethod
    def exportXMLStr(self):
        pass