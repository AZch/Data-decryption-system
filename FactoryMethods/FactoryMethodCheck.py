from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MethodCheck import MethodCheck

class FactoryMethodCheck(FactoryMethod):
    def createMethod(self, name):
        return MethodCheck(name=name)