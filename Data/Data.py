from Data.IData import IData
from Data.Note import Note
from Constants import NumConst

class Data(IData):
    def __init__(self):
        self.lstNotes = []

    '''
        Формат строки данных
        Название метода|результат|биты под результат
    '''
    def loadData(self, strData):
        lstAllNotes = strData.split('\n')
        for note in lstAllNotes:
            dataNote = note.split('|')
            if (len(dataNote) == NumConst.countDataStr):
                self.lstNotes.append(Note(nameFunction=dataNote[0], resFunction=dataNote[1],
                                          lstBit=dataNote[2].split()))
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
            resStr += note.nameFunction + "|" + note.resFunction + "|" + ' '.join(note.lstBit) + "\n"
        return resStr

    def getData(self):
        copyLstNote = []
        for note in self.lstNotes:
            copyLstNote.append(Note(nameFunction=note.nameFunction, resFunction=note.resFunction,
                                    lstBit=note.lstBit))
        return copyLstNote
