from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MMoreOneRand import MMoreOneRand

class FactoryMMoreOneRand(FactoryMethod):
    def createMethod(self, param):
        return MMoreOneRand(name=param[0], timeSleep=param[1], posStart=param[2], posEnd=param[3],
                            countProc=param[4], timeWait=param[5], countOneRand=param[6])