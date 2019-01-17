from ObjectPool.ExecProc import ExecProc
from Data.Note import Note

class ExecProcPool():

    def __init__(self, maxCountProc, maxWait):
        self.__maxCountProc = maxCountProc
        self.__lstExecProc = list()
        self.__workProc = list()
        self.__thisCount = 0
        self.__maxWait = maxWait

    def wait(self):
        lstNoteToLong = list()
        for proc in self.__workProc:
            if proc.whatSecWork() > self.__maxWait:
                lstNoteToLong.append(Note(nameFunction='long wait', resFunction='long wait',
                                          lstBit=proc.getLstByte(), lstPosition=proc.getLstBytePos()))
                self.returnProc(proc)
        if len(self.__lstExecProc) <= 0 and len(self.__workProc) != 0:
            return 'wait'
        return lstNoteToLong

    def getProc(self, execFile, resFile, bytePos, byte, method, testData):
        ret = self.wait()
        if ret == 'wait':
            return ret
        if len(self.__lstExecProc) > 0:
            newProc = self.__lstExecProc.pop(0)
            newProc.setNewData(execFile, resFile, bytePos, byte)
            self.__workProc.append(newProc)
            return newProc
        else:
            if self.__thisCount < self.__maxCountProc:
                self.__thisCount += 1
                proc = ExecProc(execFile, resFile, bytePos, byte, method, self, testData=testData)
                self.__workProc.append(proc)
                return proc
            else:
                return 'wait'

    def returnProc(self, proc):
        isDel = False
        proc.dontAdd()
        for procWork in self.__workProc:
            if procWork.startTime == proc.startTime:
                self.__workProc.remove(procWork)
                isDel = True
        if isDel:
            self.__lstExecProc.append(proc.clone())
