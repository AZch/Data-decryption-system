import json
import smtplib

from Constants import *
from DataDB import Models


class WorkWithCFG():
    def initDataFromCfg(self, workClass):
        file = open(jsonWord.configName, 'r')
        with file:
            data = file.read()
            workClass.jsonData = json.loads(data)

            workClass.mailSmtp = workClass.jsonData[jsonWord.mail][jsonWord.mailSmtp]
            workClass.mailLgn = workClass.jsonData[jsonWord.mail][jsonWord.mailLgn]
            workClass.mailPsw = workClass.jsonData[jsonWord.mail][jsonWord.mailPsw]
            workClass.userMail = workClass.jsonData[jsonWord.mail][jsonWord.userMail]
            while True:
                if workClass.mailSmtp == "":
                    print('smtp server(example: smtp.mail.ru): ')
                    workClass.mailSmtp = input()
                if workClass.mailLgn == "":
                    print('mail login: ')
                    workClass.mailLgn = input()
                if workClass.mailPsw == "":
                    print('mail password: ')
                    workClass.mailPsw = input()
                if workClass.userMail == "":
                    print('mail to send result status: ')
                    workClass.userMail = input()
                try:
                    workClass.smtpObj = smtplib.SMTP(workClass.mailSmtp, 587)
                    workClass.smtpObj.starttls()
                    resLgn = workClass.smtpObj.login(workClass.mailLgn, workClass.mailPsw)
                    break
                except:
                    pass
                print("data incorrect, please input correct data")
                workClass.mailSmtp = ''
                workClass.mailLgn = ''
                workClass.mailPsw = ''
                workClass.userMail = ''
                print('Reconnect y/n (y):')
                workClass.isReconnect = input()
                if workClass.isReconnect == 'n' or workClass.isReconnect == 'not':
                    break

            workClass.dbName = workClass.jsonData[jsonWord.db][jsonWord.dbName]
            workClass.dbHost = workClass.jsonData[jsonWord.db][jsonWord.dbHost]
            workClass.dbPort = workClass.jsonData[jsonWord.db][jsonWord.dbPosrt]
            workClass.dbUser = workClass.jsonData[jsonWord.db][jsonWord.dbUser]
            workClass.dbPsw = workClass.jsonData[jsonWord.db][jsonWord.dbPsw]

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

    def makeCfg(self, classCall):
        dataToCfg = {}
        dataToCfg[jsonWord.db] = {}
        dataToCfg[jsonWord.db][jsonWord.dbName] = Models.DB
        dataToCfg[jsonWord.db][jsonWord.dbHost] = Models.HOST
        dataToCfg[jsonWord.db][jsonWord.dbPosrt] = Models.PORT
        dataToCfg[jsonWord.db][jsonWord.dbUser] = Models.USER
        dataToCfg[jsonWord.db][jsonWord.dbPsw] = Models.PASSWORD

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

    def compareCfg(self, workClass, firstCfg, secondCfg):
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