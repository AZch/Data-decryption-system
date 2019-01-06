from FactoryMethods.FactoryMethod import FactoryMethod
from Methods.MethodCheck import MethodCheck

class FactoryMethodCheck(FactoryMethod):
    def createMethod(self, data):
        return MethodCheck(data=data, startTime=1, endTime=90)