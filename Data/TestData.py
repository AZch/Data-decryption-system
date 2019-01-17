class TestData():
    def __init__(self, testFileWay=""):
        self.__baseLstTestData = []
        self.__workLstTestData = []
        self.testFileWay = testFileWay
        self.__allUpData = ""
        self.__allDownData = ""

    def parseNotes(self, lstNote):
        maxXSize = 0
        maxYSize = 0
        for note in lstNote:
            for position in note.lstPosition:
                y = int(position.split('x')[0])
                x = int(position.split('x')[1])
                if x > maxXSize:
                    maxXSize = x
                if y > maxYSize:
                    maxYSize = y

        self.__workLstTestData = [[0] * (maxXSize + 1) for i in range(maxYSize + 1)]
        for note in lstNote:
            if (len(note.lstPosition) == len(note.lstBit)):
                for i in range(len(note.lstPosition)):
                    xyPosition = note.lstPosition[i].split('x')
                    self.__workLstTestData[int(xyPosition[1])][int(xyPosition[0])] = note.lstBit[i]
        self.__baseLstTestData = self.copyLstTestData()
        return self.__workLstTestData

    def saveToFile(self):
        fileSave = self.testFileWay
        file = open(fileSave, 'w')
        if file == '':
            return fileSave + " not open"

        file.write(self.getStrTestData())
        file.close()

    def incDot(self, x, y):
        res = hex(int('0x' + self.__workLstTestData[x][y], 16) + 1)[2:]
        if len(res) == 1:
            self.__workLstTestData[x][y] = "0" + res
        elif len(res) > 2:
            self.__workLstTestData[x][y] = "00"
        else:
            self.__workLstTestData[x][y] = res

    def decDot(self, x, y):
        if hex(int('0x' + self.__workLstTestData[x][y], 16))[2:] == '0':
            self.__workLstTestData[x][y] = 'ff'
            return True

        res = hex(int('0x' + self.__workLstTestData[x][y], 16) - 1)[2:]
        if len(res) == 1:
            self.__workLstTestData[x][y] = "0" + res
        elif len(res) > 2:
            self.__workLstTestData[x][y] = "00"
        else:
            self.__workLstTestData[x][y] = res

    def chgValue(self, hexPos, newVal):
        intVal = int(hexPos, 16)
        for i in range(len(self.__workLstTestData)):
            for j in range(len(self.__workLstTestData[i])):
                if i * len(self.__workLstTestData[i]) + j == intVal:
                    self.__workLstTestData[i][j] = newVal
                    break
        return self.__workLstTestData

    def backStartValue(self, hexPos):
        intVal = int(hexPos, 16)
        for i in range(len(self.__workLstTestData)):
            for j in range(len(self.__workLstTestData[i])):
                if i * len(self.__workLstTestData[i]) + j == intVal:
                    self.__workLstTestData[i][j] = self.__baseLstTestData[i][j]
                    break
        return self.__workLstTestData

    '''
        Данные представляют собой матрицу битов
    '''
    def loadData(self, strData):
        getData = strData.split('"Data"=hex:')
        self.__allUpData = getData[0] + '"Data"=hex:'
        # getData = getData[1].split('\n\n"ColumnMask"')
        # self.__allDownData = '\n\n"ColumnMask"' + getData[1]
        while getData[1][:len(getData) - 1] == '\n' or getData[1][:len(getData) - 1] == ' ' or getData[1][:len(getData) - 1] == '\\' : # здесь смотрим первый элемент, по этому и -1
            self.__allUpData += getData[1][:len(getData) - 1]
            getData[1] = getData[1][1:]
        linesData = getData[1].split(',\\\n')
        xSize = 0
        ySize = 0
        for i in range(len(linesData)):
            elems = linesData[i].split(',')
            if (xSize == 0 and ySize == 0):
                xSize = len(elems)
                ySize = len(linesData)
                self.__workLstTestData = [[0] * xSize for i in range(ySize)]
            for j in range(len(elems)):
                if len(elems[j].split('\n')) > 1: # последний символ
                    self.__workLstTestData[i][j] = elems[j].split('\n')[0]
                    self.__allDownData = elems[j][len(elems[j].split('\n')[0]):]
                    self.__baseLstTestData = self.copyLstTestData()
                    return self.__workLstTestData
                self.__workLstTestData[i][j] = elems[j]
        self.__baseLstTestData = self.copyLstTestData()
        return self.__workLstTestData

    def clearData(self):
        self.__workLstTestData.clear()
        return self.__workLstTestData

    def copyLstTestData(self):
        testData = []
        for strData in self.__workLstTestData:
            strTestData = []
            for oneElem in strData:
                strTestData.append(oneElem)
            testData.append(strTestData)
        return testData

    def getLstTestData(self):
        return self.__workLstTestData

    def getStrTestData(self):
        strTestData = ""
        for i in range(len(self.__workLstTestData)):
            for j in range(len(self.__workLstTestData[i])):
                strTestData += str(self.__workLstTestData[i][j]) + ','
            strTestData += '\\\n'
        strTestData = strTestData[:-3]

        return self.__allUpData + strTestData + self.__allDownData