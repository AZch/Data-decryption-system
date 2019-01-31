from PyQt5 import QtWidgets

from Wnds.OpenTblWnd import designOpenTbl


class OpenTblWnd(QtWidgets.QDialog, designOpenTbl.Ui_openTbl):
    def __init__(self, tbl):
        super(OpenTblWnd, self).__init__()
        self.setupUi(self)
        self.btnExit.clicked.connect(self.close)

        self.tblData.setColumnCount(tbl.columnCount())
        self.tblData.setRowCount(tbl.rowCount())
        for i in range(tbl.rowCount()):
            for j in range(tbl.columnCount()):
                self.tblData.setItem(i, j,
                                         QtWidgets.QTableWidgetItem(tbl.item(i, j)))
        self.tblData.resizeColumnsToContents()
        self.btnUpdTbl.setVisible(False)
        pass