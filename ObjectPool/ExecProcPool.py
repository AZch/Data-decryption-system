from ObjectPool.ExecProc import ExecProc
from Methods.Method import Method
import time

class ExecProcPool():

    def __init__(self, maxCountProc):
        self.__maxCountProc = maxCountProc
        self.__lstExecProc = list()
        self.__workProc = list()
        self.__thisCount = 0

    def getProc(self, execFile, resFile, bytePos, byte, method):
        for proc in self.__workProc:
            if proc.whatSecWork() > 6:
                self.returnProc(proc)
        if len(self.__lstExecProc) > 0:
            newProc = self.__lstExecProc.pop(0)
            newProc.setNewData(execFile, resFile, bytePos, byte)
            self.__workProc.append(newProc)
            return newProc
        else:
            if self.__thisCount < self.__maxCountProc:
                self.__thisCount += 1
                proc = ExecProc(execFile, resFile, bytePos, byte, method, self)
                self.__workProc.append(proc)
                return proc
            else:
                return 'wait'

    def returnProc(self, proc):
        #connection.commit()
        isDel = False
        for procWork in self.__workProc:
            if procWork.startTime == proc.startTime:
                self.__workProc.remove(procWork)
                isDel = True
        if isDel:
            self.__lstExecProc.append(proc.clone())

        #print(len(self.__workProc) + len(self.__lstExecProc))


    # def __del__(self):
    #     for conn in self.__lstExecProc:
    #         conn.commit()
    #         conn.close()