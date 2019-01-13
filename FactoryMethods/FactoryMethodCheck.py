from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MethodCheck import MethodCheck

class FactoryMethodCheck(FactoryMethod):
    def createMethod(self, param):
        return MethodCheck(name=param[0], countProc=param[1], countRow=param[2], timeSleep=param[3])