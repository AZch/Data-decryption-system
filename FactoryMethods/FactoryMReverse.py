from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MReverse import MReverse

class FactoryMReverse(FactoryMethod):
    def createMethod(self, param):
        return MReverse(name=param[0], posStart=param[1], posEnd=param[2],
                        countProc=param[3], timeWait=param[4])