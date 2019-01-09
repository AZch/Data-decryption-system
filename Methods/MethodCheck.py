from Methods.Method import Method
import time
import random
import string
from Data.Note import Note
from Data.Data import Data
from Data.TestData import TestData
from Constants import jsonWord

class MethodCheck(Method):

    def __init__(self, name):
        super().__init__(name=name)
        self.start = 1
        self.end = 90
        pass

    def calc(self, testData):
        print(self.name)
        if (not isinstance(testData, TestData)):
            print("Неверный формат входных данных")
            pass

        #time.sleep(random.randint(self.start, self.end))
        self.resData = Data()
        print(testData.getStrTestData())
        x = 0
        y = 0
        for i in range(random.randint(1, 10)):
            count = 5
            lstBit = []
            lstPos = []
            for j in range(count):
                y = random.randint(0, len(testData.getLstTestData()) - 1)
                x = random.randint(0, len(testData.getLstTestData()[0]) - 1)
                lstPos.append(str(x) + 'x' + str(y))
                lstBit.append(testData.getLstTestData()[y][x])
            self.resData.addOneNote(Note(nameFunction=self.__randomstr(3), resFunction=self.__randomstr(5),
                                         lstBit=lstBit, lstPosition=lstPos))
        return self.resData

    def __randomstr(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def exportJSON(self):
        data = {}
        data[jsonWord.method] = {
            jsonWord.name : self.name,
            jsonWord.type : jsonWord.mCheck,
            jsonWord.startTime : self.start,
            jsonWord.endTime : self.end
        }
        return data