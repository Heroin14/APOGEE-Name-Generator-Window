from PyQt4 import QtGui
import sys
class Mess(QtGui.QMessageBox):
    def __init__(self):
        super(Mess,self).__init__()
        self.initUI()
    def initUI(self):
        
        
