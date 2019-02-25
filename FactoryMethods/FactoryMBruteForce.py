from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MBruteForce import MBruteForce

class FactoryMBruteForce(FactoryMethod):
    def createMethod(self, param):
        return MBruteForce(name=param[0], countProc=param[1], timeWait=param[2], lstPosBruteForce=param[3], countForce=param[4])