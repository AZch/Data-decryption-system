from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MRandom import MRandom

class FactoryMRandom(FactoryMethod):
    def createMethod(self, param):
        return MRandom(name=param[0], countProc=param[1], timeWait=param[2], lstPosRand=param[3], countRand=param[4])