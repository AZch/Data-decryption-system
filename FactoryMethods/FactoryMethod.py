from abc import ABCMeta, abstractmethod

class FactoryMethod(ABCMeta):
    @abstractmethod
    def createMethod(self, param):
        pass