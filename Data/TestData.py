class TestData():
    def __init__(self, testFileWay=""):
        self.__lstTestData = []
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

        self.__lstTestData = [[0] * (maxXSize + 1) for i in range(maxYSize + 1)]
        for note in lstNote:
            if (len(note.lstPosition) == len(note.lstBit)):
                for i in range(len(note.lstPosition)):
                    xyPosition = note.lstPosition[i].split('x')
                    self.__lstTestData[int(xyPosition[1])][int(xyPosition[0])] = note.lstBit[i]
        return self.__lstTestData

    def saveToFile(self):
        fileSave = self.testFileWay
        file = open(fileSave, 'w')
        if file == '':
            return fileSave + " not open"

        file.write(self.getStrTestData())
        file.close()

    def incDot(self, x, y):
        res = hex(int('0x' + self.__lstTestData[x][y], 16) + 1)[2:]
        if len(res) == 1:
            self.__lstTestData[x][y] = "0" + res
        elif len(res) > 2:
            self.__lstTestData[x][y] = "00"
        else:
            self.__lstTestData[x][y] = res

    def decDot(self, x, y):
        if hex(int('0x' + self.__lstTestData[x][y], 16))[2:] == '0':
            self.__lstTestData[x][y] = 'ff'
            return True

        res = hex(int('0x' + self.__lstTestData[x][y], 16) - 1)[2:]
        if len(res) == 1:
            self.__lstTestData[x][y] = "0" + res
        elif len(res) > 2:
            self.__lstTestData[x][y] = "00"
        else:
            self.__lstTestData[x][y] = res

    '''
        Данные представляют собой матрицу битов
    '''
    def loadData(self, strData):
        getData = strData.split('"Data"=hex:\\\n')
        self.__allUpData = getData[0] + '"Data"=hex:\\\n'
        getData = getData[1].split('\n\n"ColumnMask"')
        self.__allDownData = '\n\n"ColumnMask"' + getData[1]
        linesData = getData[0].split(',\\\n')
        xSize = 0
        ySize = 0
        for i in range(len(linesData)):
            elems = linesData[i].split(',')
            if (xSize == 0 and ySize == 0):
                xSize = len(elems)
                ySize = len(linesData)
                self.__lstTestData = [[0] * xSize for i in range(ySize)]
            for j in range(len(elems)):
                self.__lstTestData[i][j] = elems[j]
        return self.__lstTestData

    def clearData(self):
        self.__lstTestData.clear()
        return self.__lstTestData


    def getLstTestData(self):
        return self.__lstTestData

    def getStrTestData(self):
        strTestData = ""
        for i in range(len(self.__lstTestData)):
            for j in range(len(self.__lstTestData[i])):
                strTestData += str(self.__lstTestData[i][j]) + ','
            strTestData = strTestData[:-1]
            strTestData += ',\\\n'
        strTestData = strTestData[:-3]

        return self.__allUpData + strTestData + self.__allDownData