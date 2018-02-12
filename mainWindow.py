import sys
from PyQt4 import QtGui, QtCore
from Button import *
from Labels import *
from LabelEdit import *
import os
import random
from Dialog import *

class mainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(mainWindow,self).__init__()
        self.initUI()
    def initUI(self):

            central=QtGui.QWidget(self)
            central.setGeometry(250,250,120,120)

            quitBtn=generateButton(central)
            quitBtn.setText('Quit')
            quitBtn.clicked.connect(self.quit)

            welcomeLabel1=Label(central)
            welcomeLabel1.setText('Welcome to the APOGEE Theme generator, 2018!')
            welcomeLabel2=Label(central)
            welcomeLabel2.setText('Enter your name and the funniest theme you can dare to dream of!')
            welcomeLabel1.setAlignment(QtCore.Qt.AlignCenter)
            welcomeLabel2.setAlignment(QtCore.Qt.AlignCenter)

            self.clickToGen=generateButton(central)
            self.clickToGen.setText('Click to generate')

            aboutBtn=QtGui.QPushButton(central)
            aboutBtn.setFont(QtGui.QFont('Calagiri',10,-1,True))
            aboutBtn.setText('About')
                        
            aboutBtn.clicked.connect(self.createMess)
       
            self.name= Label(central)
            self.name.setText('Enter your name:')
            self.name.setAlignment(QtCore.Qt.AlignLeft)
            self.nameEdit= LineEdit(central)
            
            self.theme=Label(central)
            self.theme.setText('Enter the most appropriate theme')
            self.theme.setAlignment(QtCore.Qt.AlignLeft)
            self.themeEdit= LineEdit(central)
              
            self.nameEdit.editingFinished.connect(self.nameEnter)
            self.themeEdit.returnPressed.connect(self.themeEnter)
               
            hbox=QtGui.QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(self.clickToGen)
            hbox.addWidget(quitBtn)
            
            vbox=QtGui.QVBoxLayout(self)
            vbox.addWidget(welcomeLabel1)
            vbox.addWidget(welcomeLabel2)
            
            vbox.addWidget(aboutBtn)
            vbox.addStretch(1)
            vbox.addWidget(self.name)
            vbox.addWidget(self.nameEdit)
            vbox.addWidget(self.theme)
            vbox.addWidget(self.themeEdit)
           
            #self.clickToGen.clicked.connect(self.ItBegins1)
            vbox.addLayout(hbox)
            
            central.setLayout(vbox)
            
            self.setCentralWidget(central)
            self.setWindowIcon(QtGui.QIcon('/home/swarup/Downloads/epclogo.png'))
            self.setWindowTitle('APOGEE Name Generator')
            self.setGeometry(500,400,250,250)
            self.show()
    
    def quit(self):
        msg=QtGui.QMessageBox(self)
        reply=msg.question(self,'Message','Are you sure you want to quit?',QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if reply== QtGui.QMessageBox.Yes:
            sys.exit(0)
        else:
            msg.close()
   
   
    def nameEnter(self):
        fileName= 'entriesList.txt'
       
        currDir= os.path.abspath(os.path.curdir)
        path= os.path.join(currDir,fileName)
        
        with open(path,'a') as infile:
            infile.write(self.nameEdit.text())
            infile.write('\n')


    def themeEnter(self):
        
        currdir=os.path.abspath(os.path.curdir)
        f1='firstWords.txt'
        f2='secondWords.txt'

        p1=os.path.join(currdir,f1)
        p2=os.path.join(currdir,f2)
        
        st=str(self.themeEdit.text())
        words= st.split(' ')
        l=len(words)
        if(l>3):
           self.wrongFormat()
        
        else:
            
            if l==1:
                if words[0]=='The' or words[0]=='the' or words[0]=='a'or words[0] =='A':

                    msgBox1= QtGui.QMessageBox(self)
                    reply=msgBox1.warning(self,'Warning','Enter more than one word', QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
                    if reply==QtGui.QMessageBox.Ok:
                        msgBox1.close()
                else:
                    with open(p1,'a') as i1:
                        i1.write(words[0])
                        i1.write('\n')

                    self.correctStored()
                    self.clickToGen.clicked.connect(self.ItBegins)
            elif l==2:
                if words[1]=='The' or words[1]=='the' or words[1]=='a' or words[1] =='A':
                    self.wrongFormat()
                else:
                    if(words[0]=='The' or words[0]=='the' or words[0]=='a' or words[0] =='A'):
                        with open(p1,'a') as i1:
                            i1.write(words[1])
                            i1.write('\n')
                        self.correctStored()
                        self.clickToGen.clicked.connect(self.ItBegins)

                    else:
                        with open(p1,'a') as i1:
                            i1.write(words[0])
                            i1.write('\n')
                        with open(p2,'a') as i2:
                            i2.write(words[1])
                            i2.write('\n')
                        self.correctStored()
                        self.clickToGen.clicked.connect(self.ItBegins)

            else:
                if words[1]=='The' or words[1]=='the' or words[1]=='a' or words[1] =='A' or words[2]=='The' or words[2]=='the' or words[2]=='a' or words[2] =='A':
                    self.wrongFormat()
                else:
                    with open(p1,'a') as i1:
                        i1.write(words[1])
                        i1.write('\n')
                    with open(p2,'a') as i2:
                        i2.write(words[2])
                        i2.write('\n')
                    self.correctStored()
                    self.clickToGen.clicked.connect(self.ItBegins)
                

    def wrongFormat(self):
        msgBox= QtGui.QMessageBox(self)
        reply=msgBox.warning(self,'Warning','Enter in the correct format otherwise you may not proceed', QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        if reply==QtGui.QMessageBox.Ok:
            msgBox.close()
        
    def correctStored(self):
        msgBox2=QtGui.QMessageBox(self)
        reply=msgBox2.information(self,'Success','Phrase succesfully stored',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
        if reply==QtGui.QMessageBox.Ok:
            msgBox2.close()

    def createMess(self):
        
        msgBox=QtGui.QMessageBox(self)
        reply=msgBox.information(self,'About','The window is an APOGEE name generator. \nEnter a phrase which you believe is the funniest and the most meaningless APOGEE theme and see what results you get.\nUse and have fun.\nCreator: SwitchBLADE \nCourtesy of the APOGEE English Press. \n \nDisclaimer: Noobs and Mamallan should stay away.',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
        if reply==QtGui.QMessageBox.Ok:
            msgBox.close()
        msgBox.setGeometry(500,500,250,250)

    def ItBegins(self):

        
        currdir=os.path.abspath(os.path.curdir)
        f1='firstWords.txt'
        f2='secondWords.txt'

        p1=os.path.join(currdir,f1)
        p2=os.path.join(currdir,f2)

        lst3=['','A','The']
        lst2=[]
        lst1=[]
        with open(p1,'r') as i1:
            lst1=i1.readlines()
        

        with open(p2,'r') as i2:
            lst2=i2.readlines()
            
        while True:
            n1=random.randint(0,len(lst1)-1)
            n2=random.randint(0,len(lst2)-1)
            n3=random.randint(0,len(lst3)-1)

            if lst1[n1]=='\n' or lst2[n2]=='\n':
                continue
            else:
                break
            
        pronoun=lst3[n3]
        first=lst1[n1]
        second=lst2[n2]
        finalText=pronoun+' '+first+' '+second
        
        finalDia= QtGui.QDialog(self)
        finalDia.setWindowTitle('Success!!')
        lb=QtGui.QLabel(finalDia)
        lb.setTextFormat(QtCore.Qt.RichText)
        lb.setFont(QtGui.QFont('TimesNewRoman',30,QtGui.QFont.Bold))
        year= random.randint(0,2500)
        year="APOGEE "+ str(year) 
        lb.setText(year)
        lb.setAlignment(QtCore.Qt.AlignCenter)
        
        lb1=QtGui.QLabel(finalDia)
        lb1.setTextFormat(QtCore.Qt.RichText)
        lb1.setFont(QtGui.QFont('Calagiri',25,-1,True))
        lb1.setText(finalText)
        lb1.setAlignment(QtCore.Qt.AlignCenter)

        hbt1=generateButton(finalDia)
        hbt1.setText('Play again?')
        hbt2=generateButton(finalDia)
        hbt2.setText('Quit')

        hbt1.clicked.connect(finalDia.close)
        hbt2.clicked.connect(self.close)

        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(hbt1)
        hbox.addWidget(hbt2)


        vbox=QtGui.QVBoxLayout(finalDia)
        vbox.addSpacing(1)
        vbox.addWidget(lb)
        vbox.addSpacing(1)
        vbox.addWidget(lb1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        finalDia.setGeometry(300,600,350,150)
        finalDia.setLayout(vbox)

        finalDia.show()
        
    def ItBegins1(self):
        msgBox=QtGui.QMessageBox(self)
        reply=msgBox.information(self,'Error','Enter the fields first!',QtGui.QMessageBox.Ok,QtGui.QMessageBox.Ok)
        if reply==QtGui.QMessageBox.Ok:
            msgBox.close()
        msgBox.setGeometry(500,500,250,250)   

        
           
                
                


            
        

    



        

