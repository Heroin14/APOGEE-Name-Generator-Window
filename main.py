#!/usr/bin/python
import sys
from PyQt4 import QtGui,QtCore
from mainWindow import *

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    mWindow=mainWindow()

    sys.exit(app.exec_())