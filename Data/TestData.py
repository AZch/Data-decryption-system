class TestData():
    def __init__(self, testFileWay=""):
        self.__baseLstTestData = []
        self.__workLstTestData = []
        self.testFileWay = testFileWay
        self.__allUpData = ""
        self.__allDownData = ""
        self.__yDiv = 16 # начальный размер массива по y, для отображения в матричной форме

    def parseNotes(self, lstNote):
        maxSize = 0
        for note in lstNote:
            for position in note.lstPosition:
                size = int(position, 16)
                if size > maxSize:
                    maxSize = size

        self.__workLstTestData = list(maxSize)
        for note in lstNote:
            if (len(note.lstPosition) == len(note.lstBit)):
                for i in range(len(note.lstPosition)):
                    self.__workLstTestData[int(note.lstPosition[i], 16)] = note.lstBit[i]
        self.__baseLstTestData = self.copyLstTestData()
        return self.__workLstTestData

    def saveToFile(self):
        fileSave = self.testFileWay
        file = open(fileSave, 'w')
        if file == '':
            return fileSave + " not open"

        file.write(self.getStrTestData())
        file.close()

    def getByteByPos(self, positions):
        bytes = list()
        for pos in positions:
            bytes.append(self.__workLstTestData[pos])
        return bytes

    def saveBaseToFile(self):
        fileSave = self.testFileWay
        file = open(fileSave, 'w')
        if file == '':
            return fileSave + " not open"

        file.write(self.getBaseStrTestData())
        file.close()

    def incDot(self, pos):
        res = hex(int('0x' + self.__workLstTestData[pos], 16) + 1)[2:]
        if len(res) == 1:
            self.__workLstTestData[pos] = "0" + res
        elif len(res) > 2:
            self.__workLstTestData[pos] = "00"
        else:
            self.__workLstTestData[pos] = res

    def decDot(self, pos):
        if hex(int('0x' + self.__workLstTestData[pos], 16))[2:] == '0':
            self.__workLstTestData[pos] = 'ff'
            return True

        res = hex(int('0x' + self.__workLstTestData[pos], 16) - 1)[2:]
        if len(res) == 1:
            self.__workLstTestData[pos] = "0" + res
        elif len(res) > 2:
            self.__workLstTestData[pos] = "00"
        else:
            self.__workLstTestData[pos] = res

    def chgValue(self, hexPos, newVal):
        intVal = int(hexPos, 16)
        self.__workLstTestData[intVal] = newVal
        return self.__workLstTestData

    def backStartValue(self, hexPos):
        intVal = int(hexPos, 16)
        self.__workLstTestData[intVal] = self.__baseLstTestData[intVal]
        return self.__workLstTestData

    def getValByPos(self, hexPos):
        intVal = int(hexPos, 16)
        return self.__workLstTestData[intVal]

    def makeMatrixData(self):
        matrixData = [[0] * self.__yDiv for i in range(int(len(self.__workLstTestData) / self.__yDiv))]
        for i in range(len(matrixData)):
            for j in range(len(matrixData[i])):
                matrixData[i][j] = self.__workLstTestData[i * len(matrixData[i]) + j]

        return matrixData

    '''
        Данные представляют собой матрицу битов
    '''
    def loadData(self, strData):
        getData = strData.split('"Data"=hex:')
        self.__allUpData = getData[0] + '"Data"=hex:'
        # getData = getData[1].split('\n\n"ColumnMask"')
        # self.__allDownData = '\n\n"ColumnMask"' + getData[1]
        while getData[1][:len(getData) - 1] == '\n' or \
                getData[1][:len(getData) - 1] == ' ' or \
                getData[1][:len(getData) - 1] == '\\' : # здесь смотрим первый элемент, по этому и -1
            self.__allUpData += getData[1][:len(getData) - 1]
            getData[1] = getData[1][1:]
        linesData = getData[1].split(',\\\n')
        # xSize = 0
        # ySize = 0
        for i in range(len(linesData)):
            elems = linesData[i].split(',')
            # if (xSize == 0 and ySize == 0):
            #     xSize = len(elems)
            #     ySize = len(linesData)
                #self.__workLstTestData = [[0] * xSize for i in range(ySize)]
            for j in range(len(elems)):
                if len(elems[j].split('\n')) > 1: # последний символ
                    self.__workLstTestData.append(elems[j].split('\n')[0])
                    self.__allDownData = elems[j][len(elems[j].split('\n')[0]):]
                    self.__baseLstTestData = self.copyLstTestData()
                    return self.__workLstTestData
                self.__workLstTestData.append(elems[j])
        self.__baseLstTestData = self.copyLstTestData()
        return self.__workLstTestData

    def clearData(self):
        self.__workLstTestData.clear()
        return self.__workLstTestData

    def copyLstTestData(self):
        testData = []
        for oneElem in self.__workLstTestData:
            testData.append(oneElem)
        return testData

    def getLstTestData(self):
        return self.__workLstTestData

    def getStrTestData(self):
        strTestData = ""
        i = 0
        while i < len(self.__workLstTestData):
            for j in range(self.__yDiv):
                strTestData += str(self.__workLstTestData[i]) + ','
                i += 1
            strTestData += '\\\n'
        strTestData = strTestData[:-3]

        return self.__allUpData + strTestData + self.__allDownData

    def getBaseStrTestData(self):
        strTestData = ""
        i = 0
        while i < len(self.__baseLstTestData):
            for j in range(self.__yDiv):
                strTestData += str(self.__baseLstTestData[i]) + ','
                i += 1
            strTestData += '\\\n'
        strTestData = strTestData[:-3]

        return self.__allUpData + strTestData + self.__allDownData