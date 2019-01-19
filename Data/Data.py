from Data.IData import IData
from Data.Note import Note
from Constants import NumConst
from Data.TestData import TestData

class Data(IData):
    def __init__(self):
        self.lstNotes = []

    '''
        Формат строки данных
        Название метода|результат|биты под результат|позиции битов
    '''
    def loadData(self, strData):
        lstAllNotes = strData.split('\n')
        for note in lstAllNotes:
            dataNote = note.split('|')
            if (len(dataNote) == NumConst.countDataStr):
                self.lstNotes.append(Note(nameFunction=dataNote[0], resFunction=dataNote[1],
                                          lstBit=dataNote[2].split(), lstPosition=dataNote[3].split()))
            else:
                print("загружаемые данные имеют неверный формат")
                pass
        pass

    '''
            Формат строки данных
            Название метода|результат|биты под результат
    '''
    def makeStrData(self):
        resStr = ""
        for note in self.lstNotes:
            resStr += note.nameFunction + "|" + note.resFunction + "|" + ' '.join(note.lstBit) + "|" + ' '.join(str(pos) for pos in note.lstPosition) + "\n"
        resStr = resStr[:-1]
        return resStr

    def makeLstTestData(self):
        testData = TestData()
        return testData.parseNotes(self.lstNotes)

    def makeStrTestData(self):
        testData = TestData()
        testData.parseNotes(self.lstNotes)
        return testData.getStrTestData()

    def searchForNameFunc(self, nameSearch):
        for note in self.lstNotes:
            if note.nameFunction == nameSearch:
                return note
        return "not found"

    def getData(self):
        copyLstNote = []
        for note in self.lstNotes:
            copyLstNote.append(Note(nameFunction=note.nameFunction, resFunction=note.resFunction,
                                    lstBit=note.lstBit, lstPosition=note.lstPosition))
        return copyLstNote

    def addOneNote(self, note):
        searchNote = self.searchForNameFunc(note.nameFunction)
        if searchNote != 'not found':
            newByte = list(set(note.lstPosition) - set(searchNote.lstPosition))
            if newByte != []:
                for oneBytePos in newByte:
                    searchNote.lstBit.append(note.lstBit[note.lstPosition.index(oneBytePos)])
                    searchNote.lstPosition.append(oneBytePos)
        else:
            self.lstNotes.append(note)

    def addSimpleOneNote(self, note):
        self.lstNotes.append(note)