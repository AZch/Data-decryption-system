import pymysql

class DBConnPool():
    __lstConn = list()
    __db = ""
    __user = ""
    __psw = ""
    __host = ""

    def __init__(self, db, user, psw, host):
        self.__db = db
        self.__user = user
        self.__psw = psw
        self.__host = host

    def getConn(self):
        if len(self.__lstConn) > 0:
            return self.__lstConn.pop(0)
        else:
            return pymysql.connect(db=self.__db,
                                   user=self.__user,
                                   password=self.__psw,
                                   host=self.__host)

    def returnConn(self, connection):
        connection.commit()
        self.__lstConn.append(connection)

    def __del__(self):
        for conn in self.__lstConn:
            conn.commit()
            conn.close()