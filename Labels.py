from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class Label(QtGui.QLabel):
    def __init__(self,parent):
        super(Label,self).__init__(parent)
        self.initUI(parent)

    def initUI(self,parent):
        self.setFont(QtGui.QFont('Calagiri',10,-1,True))
        