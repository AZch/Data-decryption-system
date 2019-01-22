from peewee import *

class BaseModelDDS(Model):
    class Meta:
        database = MySQLDatabase('dds', user='root', password='Tezibo44', host='localhost', port=3307)
        database.connect()

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
    resFile = CharField(max_length=3000)
    pos = CharField(max_length=200)
    bytes = CharField(max_length=200)
    userNameProc = CharField(max_length=100)
    descr = CharField(max_length=300)
    tasks = ForeignKeyField(Tasks, db_column='idTaskProc', related_name="proc")

    class Meta:
        dbTable = 'proc'
        orderBy = ('flagExec',)