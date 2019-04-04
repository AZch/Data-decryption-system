from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MMoreOneRand import MMoreOneRand

class FactoryMMoreOneRand(FactoryMethod):
    def createMethod(self, param):
        return MMoreOneRand(name=param[0], posStart=param[1], posEnd=param[2],
                            countProc=param[3], timeWait=param[4], countOneRand=param[5])