class TestData():
    def __init__(self):
        self.__lstTestData = []

    def parseNotes(self, lstNote):
        maxXSize = 0
        maxYSize = 0
        for note in lstNote:
            for position in note.lstPosition:
                x = int(position.split('x')[0])
                y = int(position.split('x')[1])
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

    '''
        Данные представляют собой матрицу битов
    '''
    def loadData(self, strData):
        linesData = strData.split('\n')
        xSize = 0
        ySize = 0
        for i in range(len(linesData)):
            elems = linesData[i].split(' ')
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
                strTestData += str(self.__lstTestData[i][j]) + ' '
            strTestData = strTestData[:-1]
            strTestData += '\n'
        strTestData = strTestData[:-1]
        return strTestData