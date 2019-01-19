from PyQt5 import QtWidgets
from PyQt5 import QtCore

import time

import designOpenTbl

class OpenTblWnd(QtWidgets.QDialog, designOpenTbl.Ui_openTbl):
    def __init__(self, tbl):
        super(OpenTblWnd, self).__init__()
        self.setupUi(self)
        self.tblData.setColumnCount(tbl.columnCount())
        self.tblData.setRowCount(tbl.rowCount())
        for i in range(tbl.rowCount()):
            for j in range(tbl.columnCount()):
                self.tblData.setItem(i, j,
                                         QtWidgets.QTableWidgetItem(tbl.item(i, j)))
        self.tblData.resizeColumnsToContents()
        pass