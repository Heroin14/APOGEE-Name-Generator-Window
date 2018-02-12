import sys
from PyQt4 import QtGui

class LineEdit(QtGui.QLineEdit):
    def __init__(self,parent):
        super(LineEdit,self).__init__(parent)
        self.initUI(parent)

    def initUI(self,parent):
        self.setFont(QtGui.QFont('SansSerif',10,-1,True))
        