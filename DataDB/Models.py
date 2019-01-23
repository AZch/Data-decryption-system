from peewee import *
from Constants import jsonWord
import json
file = open(jsonWord.configName, 'r')
with file:
    data = file.read()
    jsonData = json.loads(data)
    DB = jsonData[jsonWord.db][jsonWord.dbName]
    USER = jsonData[jsonWord.db][jsonWord.dbUser]
    PASSWORD = jsonData[jsonWord.db][jsonWord.dbPsw]
    HOST = jsonData[jsonWord.db][jsonWord.dbHost]
    PORT = jsonData[jsonWord.db][jsonWord.dbPosrt]

if DB == "":
    print("Database name:")
    DB = input()
if USER == "":
    print("Database user name:")
    USER = input()
if PASSWORD == "":
    print("Database password:")
    PASSWORD = input()
if HOST == "":
    print("Database host name:")
    HOST = input()
if PORT == 0:
    print("Database port:")
    PORT = int(input())

databaseMain = MySQLDatabase(DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
databaseMain.connect()

class BaseModelDDS(Model):
    class Meta:
        database = databaseMain

class Tasks(BaseModelDDS):
    idTasks = PrimaryKeyField(null=False)
    method = CharField(max_length=1000)
    userName = CharField(max_length=100)

    class Meta:
        dbTable = 'tasks'
        orderBy = ('method',)

class Proc(BaseModelDDS):
    idProc = PrimaryKeyField(null=False)
    flagExec = IntegerField(default=None)
    inputTest = CharField(max_length=3000)
    resFile = TextField()
    pos = CharField(max_length=200)
    bytes = CharField(max_length=200)
    userNameProc = CharField(max_length=100)
    timewait = CharField(max_length=300)
    tasks = ForeignKeyField(Tasks, db_column='idTaskProc', related_name="proc")

    class Meta:
        dbTable = 'proc'
        orderBy = ('flagExec',)