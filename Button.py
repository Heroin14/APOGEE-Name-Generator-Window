from PyQt4 import QtGui
import sys

class generateButton(QtGui.QPushButton):
    def __init__(self,parent):
        super(generateButton,self).__init__(parent)
        self.initUI(parent)

    def initUI(self,parent):
        self.setFont(QtGui.QFont('Calagiri',10,-1,True))
        



        
        