import json
import smtplib

from Constants import *
from DataDB import Models


class WorkWithCFG():
    def __init__(self):
        self.__isEmpty = False

    def initDataFromCfg(self, workClass):
        try:
            file = open(jsonWord.configName, 'r')
        except:
            self.__isEmpty = True
            self.setStartData(workClass)
        if not self.__isEmpty:
            with file:
                data = file.read()
                workClass.jsonData = json.loads(data)

                workClass.mailSmtp = workClass.jsonData[jsonWord.mail][jsonWord.mailSmtp]
                workClass.mailLgn = workClass.jsonData[jsonWord.mail][jsonWord.mailLgn]
                workClass.mailPsw = workClass.jsonData[jsonWord.mail][jsonWord.mailPsw]
                workClass.userMail = workClass.jsonData[jsonWord.mail][jsonWord.userMail]
                workClass.testConnMail(mailSmtp=workClass.mailSmtp, mailLgn=workClass.mailLgn,
                                       mailPsw=workClass.mailPsw, userMail=workClass.userMail)

                workClass.DB = workClass.jsonData[jsonWord.db][jsonWord.dbName]
                workClass.HOST = workClass.jsonData[jsonWord.db][jsonWord.dbHost]
                workClass.PORT = workClass.jsonData[jsonWord.db][jsonWord.dbPosrt]
                workClass.USER = workClass.jsonData[jsonWord.db][jsonWord.dbUser]
                workClass.PASSWORD = workClass.jsonData[jsonWord.db][jsonWord.dbPsw]

                workClass.currCfg = workClass.jsonData[jsonWord.readCfg]
                workClass.currCfgMethods = workClass.jsonData[workClass.currCfg][jsonWord.readCfgMethods]
                workClass.currCfgFiles = workClass.jsonData[workClass.currCfg][jsonWord.readCfgFiles]
                workClass.currCfgChgVal = workClass.jsonData[workClass.currCfg][jsonWord.readCfgChgVal]

                workClass.workApi.loadJSONMethods(dataStr=workClass.jsonData[workClass.currCfgMethods])
                workClass.updateAfterSelect()
                workClass.workApi.loadJSONFiles(dataStr=workClass.jsonData[workClass.currCfgFiles])
                workClass.updTblInputTest()
                workClass.updNameFiles()
                workClass.dataChgVal = workClass.jsonData[workClass.currCfgChgVal]
                #workClass.updChgTbl(workClass.jsonData[workClass.currCfgChgVal])

    def setStartData(self, workClass):
        workClass.mailSmtp = ""
        workClass.mailLgn = ""
        workClass.mailPsw = ""
        workClass.userMail = ""

        workClass.DB = ""
        workClass.HOST = ""
        workClass.PORT = 0
        workClass.USER = ""
        workClass.PASSWORD = ""

        workClass.currCfg = "default"
        workClass.currCfgMethods = "loadMehtods"
        workClass.currCfgFiles = "ReadFiles"
        workClass.currCfgChgVal = "chgValue"
        workClass.dataChgVal = {}

    def makeCfg(self, classCall):
        dataToCfg = {}
        dataToCfg[jsonWord.db] = {}
        dataToCfg[jsonWord.db][jsonWord.dbName] = classCall.DB
        dataToCfg[jsonWord.db][jsonWord.dbHost] = classCall.HOST
        dataToCfg[jsonWord.db][jsonWord.dbPosrt] = classCall.PORT
        dataToCfg[jsonWord.db][jsonWord.dbUser] = classCall.USER
        dataToCfg[jsonWord.db][jsonWord.dbPsw] = classCall.PASSWORD

        dataToCfg[jsonWord.mail] = {}
        dataToCfg[jsonWord.mail][jsonWord.mailSmtp] = classCall.mailSmtp
        dataToCfg[jsonWord.mail][jsonWord.mailLgn] = classCall.mailLgn
        dataToCfg[jsonWord.mail][jsonWord.mailPsw] = classCall.mailPsw
        dataToCfg[jsonWord.mail][jsonWord.userMail] = classCall.userMail
        #database = MySQLDatabase(self.dbName, user=self.dbUser, password=self.dbPsw, host=self.dbHost, port=self.dbPort)

        dataToCfg[jsonWord.readCfg] = classCall.currCfg
        dataToCfg[classCall.currCfg] = {}
        dataToCfg[classCall.currCfg][jsonWord.readCfgMethods] = classCall.currCfgMethods
        dataToCfg[classCall.currCfg][jsonWord.readCfgFiles] = classCall.currCfgFiles
        dataToCfg[classCall.currCfg][jsonWord.readCfgChgVal] = classCall.currCfgChgVal

        dataToCfg[classCall.currCfgMethods] = classCall.workApi.exportAllMethods()

        dataToCfg[classCall.currCfgFiles] = {}
        dataToCfg[classCall.currCfgFiles][jsonWord.testFile] = classCall.workApi.testDataWay
        dataToCfg[classCall.currCfgFiles][jsonWord.execFile] = classCall.workApi.execFileName
        dataToCfg[classCall.currCfgFiles][jsonWord.endResFile] = classCall.workApi.resDataWay

#        rowChgTblCount = classCall.tblChgTest.rowCount()
        dataToCfg[classCall.currCfgChgVal] = classCall.dataChgVal
        # for i in range(rowChgTblCount):
        #     dataToCfg[classCall.currCfgChgVal][str(i)] = classCall.tblChgTest.cellWidget(i, 0).toPlainText() + \
        #                                             "->" + classCall.tblChgTest.cellWidget(i, 1).toPlainText()
        return dataToCfg

    def __compareDataInCfg(self, firstData, secondData):
        firstDataStr = str(firstData)
        secondDataStr = str(secondData)
        if len(firstDataStr) != len(secondDataStr):
            return False
        for i in range(len(firstDataStr)):
            if firstDataStr[i] != secondDataStr[i]:
                return False
        return True

    def compareCfg(self, workClass, firstCfg):
        if self.__isEmpty:
            return False

        secondCfg = workClass.jsonData
        if not self.__compareDataInCfg(firstCfg[workClass.currCfgMethods], secondCfg[workClass.currCfgMethods]):
            return False
        if not self.__compareDataInCfg(firstCfg[workClass.currCfgFiles], secondCfg[workClass.currCfgFiles]):
            return False
        if not self.__compareDataInCfg(firstCfg[workClass.currCfgChgVal], secondCfg[workClass.currCfgChgVal]):
            return False
        if not self.__compareDataInCfg(firstCfg[jsonWord.db], secondCfg[jsonWord.db]):
            return False
        if not self.__compareDataInCfg(firstCfg[jsonWord.mail], secondCfg[jsonWord.mail]):
            return False
        return True