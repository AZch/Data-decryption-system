from abc import ABCMeta, abstractmethod

class FactoryMethod():
    @abstractmethod
    def createMethod(self, name):
        pass