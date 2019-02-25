from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MethodCheck import MethodCheck

class FactoryMethodCheck(FactoryMethod):
    def createMethod(self, param):
        return MethodCheck(name=param[0], countProc=param[1], posStart=param[2], posEnd=param[3], timeSleep=param[4], timeWait=param[5])