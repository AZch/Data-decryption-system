from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MReverse import MReverse

class FactoryMReverse(FactoryMethod):
    def createMethod(self, param):
        return MReverse(name=param[0], timeSleep=param[1], posStart=param[2], posEnd=param[3],
                        countProc=param[4], timeWait=param[5])