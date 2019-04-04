from PyQt5 import QtWidgets

import designConn

from Constants import *
from DataDB.Models import *


class ConnWnd(QtWidgets.QDialog, designConn.Ui_Dialog):
    def __init__(self, idConn, parentCall):
        super(ConnWnd, self).__init__()
        self.setupUi(self)
        self.btnExit.clicked.connect(self.close)
        self.parentCall = parentCall
        if idConn == idConnWnd.idDB:
            self.lbl0.setText(connDB.lbl0)
            self.txt0.setPlainText(self.parentCall.DB)
            self.lbl1.setText(connDB.lbl1)
            self.txt1.setPlainText(self.parentCall.USER)
            self.lbl2.setText(connDB.lbl2)
            self.txt2.setPlainText(self.parentCall.PASSWORD)
            self.lbl3.setText(connDB.lbl3)
            self.txt3.setPlainText(self.parentCall.HOST)
            self.lbl4.setText(connDB.lbl4)
            self.spn4.setValue(self.parentCall.PORT)
            self.btnTestConn.clicked.connect(self.__testConnDB)
        elif idConn == idConnWnd.idMail:
            self.lbl0.setText(connMail.lbl0)
            self.txt0.setPlainText(self.parentCall.mailSmtp)
            self.lbl1.setText(connMail.lbl1)
            self.txt1.setPlainText(self.parentCall.mailLgn)
            self.lbl2.setText(connMail.lbl2)
            self.txt2.setPlainText(self.parentCall.mailPsw)
            self.lbl3.setText(connMail.lbl3)
            self.txt3.setPlainText(self.parentCall.userMail)
            self.lbl4.setText(StrConst.noUse)
            self.spn4.setEnabled(False)
            self.btnTestConn.clicked.connect(self.__testConnMail)

    def __testConnDB(self):
        if testConnect(DBcheck=self.txt0.toPlainText(), USERcheck=self.txt1.toPlainText(),
                    PASSWORDcheck=self.txt2.toPlainText(), HOSTcheck=self.txt3.toPlainText(),
                    PORTcheck=self.spn4.value()):
            self.parentCall.DB = self.txt0.toPlainText()
            self.parentCall.HOST = self.txt3.toPlainText()
            self.parentCall.PORT = self.spn4.value()
            self.parentCall.USER = self.txt1.toPlainText()
            self.parentCall.PASSWORD = self.txt2.toPlainText()
            self.lblState.setText(msgConfirm.conn)
            self.lblState.setStyleSheet(styles.lblStyleGood)
        else:
            self.lblState.setText(msgError.conn)
            self.lblState.setStyleSheet(styles.lblStyleBad)

    def __testConnMail(self):
        if self.parentCall.testConnMail(mailSmtp=self.txt0.toPlainText(), mailLgn=self.txt1.toPlainText(),
                                        mailPsw=self.txt2.toPlainText(), userMail=self.txt3.toPlainText()):
            self.lblState.setText(msgConfirm.conn)
            self.lblState.setStyleSheet(styles.lblStyleGood)
        else:
            self.lblState.setText(msgError.conn)
            self.lblState.setStyleSheet(styles.lblStyleBad)
        pass
