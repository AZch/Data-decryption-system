from peewee import *
from DataDB.Models import *
import time

class Add:
    @staticmethod
    def addTask(method, userName = ""):
        row = Tasks(method=method.strip(), userName=userName)

        row.save()
        return Tasks.get(Tasks.idTasks == row.idTasks)

    @staticmethod
    def addProc(flagExec, inputTest, resFile, taskDDS, timeStart = time.time(), pos="", bytes="", userNameProc="", timewait=""):
        task = taskDDS
        isExist = True
        try:
            task = Tasks.select().where(Tasks.idTasks == taskDDS.idTasks).get()
        except DoesNotExist:
            isExist = False

        if isExist:
            row = Proc(flagExec=flagExec, inputTest=inputTest, resFile=resFile, pos=pos, bytes=bytes,
                       userNameProc=userNameProc, timewait=timewait, tasks=task, timeStart=timeStart)
            row.save()


class Select():
    @staticmethod
    def selectAllTasks():
        return Tasks.select()

    @staticmethod
    def selectAllProc():
        return Proc.select()

    @staticmethod
    def selectProcByTask(id):
        return Proc.get(Proc.idTaskProc == id)

    @staticmethod
    def selectProcByFlag(flag):
        return Proc.get(Proc.flagExec == flag)

    @staticmethod
    def selectProcByFlagId(flag, tasks, bytes, pos):
        return Proc.select().where(Proc.flagExec == flag, Proc.tasks == tasks, Proc.pos == pos, Proc.bytes == bytes)

    @staticmethod
    def selectProcByFlagIdOnly(flag, tasks):
        return Proc.select().where(Proc.flagExec == flag, Proc.tasks == tasks)

class Update():
    @staticmethod
    def updTask(id, method, userName = ""):
        task = Tasks.get(Tasks.idTasks == id)
        task.method = method
        task.userName = userName

    @staticmethod
    def updProc(id, flagExec, inputTest, resFile, pos, bytes, startTime=time.time(), userNameProc="", timewait=20):
        proc = Proc.select().where(Proc.idProc == id).get()
        proc.flagExec = flagExec
        proc.inputTest = inputTest
        proc.resFile = resFile
        proc.pos = pos
        proc.bytes = bytes
        proc.userNameProc = userNameProc
        proc.timewait = timewait
        proc.startTime = startTime
        proc.save()

def checkNull(elem, task):
    if elem == "":
        return True
    else:
        return elem == task
class Delete():
    @staticmethod
    def delTask(id = -1, method = "", userName = ""):
        if id == -1:
            if userName == "":
                task = Tasks.get(Tasks.method == method)
            elif method == "":
                task = Tasks.get(Tasks.userName == userName)
            else:
                task = Tasks.get(Tasks.method == method and Tasks.userName == userName)
            task.delete_instance()
        else:
            task = Tasks.get(Tasks.idTasks == id)
            task.delete_instance()

    @staticmethod
    def delProc(id = -1, flagExec = "", inputTest = "", resFile = "", pos="", bytes="", userNameProc="", timewait=""):
        if id == -1:
            proc = Proc.get(checkNull(flagExec, Proc.flagExec) and
                            checkNull(inputTest, Proc.inputTest) and
                            checkNull(resFile, Proc.resFile) and
                            checkNull(pos, Proc.pos) and
                            checkNull(bytes, Proc.bytes) and
                            checkNull(userNameProc, Proc.userNameProc) and
                            checkNull(timewait, Proc.timewait))
            proc.delete_instance()
        else:
            proc = Proc.get(Proc.idProc == id)
            proc.delete_instance()

