from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MCompBase import MCompBase

class FactoryMCompBase(FactoryMethod):
    def createMethod(self, param):
        return MCompBase(name=param[0], timeWait=param[1])