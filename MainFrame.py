import os
import MakeInofile
import CreateMakefile
import GettingGraphInputs
import serial
import CreateGraphFromInputs
import CheckReady
import CheckArduinoConnected
import GraphWidget
import ConfigProgramFile
import MenuGraphItens
from PyQt4 import QtGui, QtCore

class mainFrame(QtGui.QFrame):
    
        def __init__(self, mainWindow, platform):
            super(mainFrame, self).__init__()
            self.mainWindow=mainWindow
            self.graphList=[]
            self.usedPins=[[],[],[]]
            self.graphCount=0
            self.graphInputs=[]
            self.platform=platform
            self.clipboard=[]
            self.arduinoPort=CheckArduinoConnected.checkArduinoConected(self.platform)
            self.initMainFrame()
            
        
        def initMainFrame(self):
            self.vbox = QtGui.QVBoxLayout()
            self.vboxWidget=QtGui.QWidget()
            self.vboxWidget.setLayout(self.vbox)
            self.vboxWidget.setGeometry(0,0,700,480)
            self.vbox.setSpacing(0)
            scrollArea=QtGui.QScrollArea()
            scrollArea.setAlignment(QtCore.Qt.AlignCenter)
            scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            scrollArea.setWidgetResizable(True)
            scrollArea.setWidget(self.vboxWidget)
            
            self.graphList+=[MenuGraphItens.menuGraphItens(self)]
            
            #buttons
            self.addButton = QtGui.QPushButton("Add")
            self.addButton.clicked.connect(self.addWidgetAction)
            self.startButton = QtGui.QPushButton("Start")
            self.startButton.clicked.connect(self.startAction)
            self.baudRateComboBox = QtGui.QComboBox()
            self.baudRateComboBox.addItems(["300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "38400", "57600", "115200"])
            self.baudRateComboBox.setCurrentIndex(5)
            vbox=QtGui.QVBoxLayout()
            hboxButtons = QtGui.QHBoxLayout()
            hboxButtons.addStretch(0)
            hboxButtons.addWidget(QtGui.QLabel("Baud Rate"))
            hboxButtons.addWidget(self.baudRateComboBox)
            hboxButtons.addWidget(self.addButton)
            hboxButtons.addWidget(self.startButton)
            vbox.addWidget(scrollArea)
            vbox.addLayout(hboxButtons)
            self.setLayout(vbox)
            self.checkReadyThread=CheckReady.checkReady(self)
            self.checkReadyThread.start()
            #buttons end
            
        def addWidgetAction(self):
            if self.graphCount<12:
                self.checkUsedPins()
                self.graphList+=[MenuGraphItens.menuGraphItens(self)]
                
        def checkUsedPins(self):
            self.usedPins=[[],[],[]]
            for i in self.graphList:
                self.usedPins[0]+=[str(i.pinNumber.currentText())]
                self.usedPins[1]+=[str(i.pinMode.currentText())]
                self.usedPins[2]+=[i.graph.lista]
        
        def disableOrEnableAllWidgets(self, status):
            #self.mainWindow.setDisabled(status)
            self.addButton.setDisabled(status)
            self.baudRateComboBox.setDisabled(status)
            for i in self.graphList:
                i.pinMode.setDisabled(status)
                i.pinNumber.setDisabled(status)
                i.removeButton.setDisabled(status)
                i.expandGraphButton.setDisabled(status)
                i.reduceGraphButton.setDisabled(status)
                i.textLineFrom.setDisabled(status)
                i.textLineTo.setDisabled(status)
                i.editGraphComboBox.setDisabled(status)
                i.editGraphButton.setDisabled(status)
                
                
        
        def startAction(self):
            if (self.startButton.text()=="Start"):
                if (os.path.isfile('./configProgramFile')):
                    if (self.arduinoPort!=''):
                        self.checkReadyThread.terminate()
                        self.disableOrEnableAllWidgets(True)
                        if self.compileAndUpload()==0:
                            self.mainWindow.statusLabel.setText("Running")
                            self.startButton.setText("Stop")
                            self.thread=GettingGraphInputs.arduinoProgramInterface(self)
                            self.thread.start()
                            #else show dialog with error
                else:
                    self.mainWindow.programConfigWindows.exec_()
            else:
                self.startButton.setText("Start")
                while self.graphInputs==[]:
                    continue
                os.chdir("..")
                self.mainWindow.statusLabel.setText("Drawing Graphics")
                self.mainWindow.app.processEvents()
                if self.graphInputs!=None:
                    CreateGraphFromInputs.drawFromInputs(self)
                self.disableOrEnableAllWidgets(False)
                #self.operationStatus=True
                self.checkReadyThread.start()
        
        def compileAndUpload(self):
            if not (os.path.isdir('./temporary')):
                os.popen("mkdir temporary")
            os.chdir("temporary")
            self.checkUsedPins()
            MakeInofile.makeInoFile(self.usedPins,self.baudRateComboBox.currentText())#TODO set the name randomly based on the time and also set flags as input only and output only
            os.chdir("..")
            if self.platform=="Linux":
                #TODO try to make use of arduino cli instead of sudar's makefile
                makefileResult=CreateMakefile.createMakefileFile()
                if makefileResult==1:
                    QtGui.QMessageBox.question(self, 'Alert', "Invalid Path to Arduino Makefile Folder. Make sure you have Arduino Makefile installed in your computer", QtGui.QMessageBox.Ok)
                    return 1
                if makefileResult==2:
                    QtGui.QMessageBox.question(self, 'Alert', "Create makefile failed", QtGui.QMessageBox.Ok)
                    return 2
                self.mainWindow.statusLabel.setText("Compiling")
                self.mainWindow.app.processEvents()
                os.system("make")
                self.mainWindow.statusLabel.setText("Uploading")
                self.mainWindow.app.processEvents()
                os.system("make upload")
                #TODO check for erros when compling and uploading
                self.arduinoSerial=serial.Serial("/dev/"+self.arduinoPort, int(self.baudRateComboBox.currentText()))
                return 0
            if self.platform=="Windows":
                board,arduinoLocation=ConfigProgramFile.getFileConfigs()
                if not os.path.isfile(arduinoLocation+"/arduino_debug.exe"):
                    QtGui.QMessageBox.question(self, 'Alert', "Invalid Path to Arduino Folder. Make sure you have Arduino IDE installed in your computer", QtGui.QMessageBox.Ok)
                    return 1
                os.chdir("temporary")
                print(os.getcwd())
                self.mainWindow.statusLabel.setText("Compiling")
                self.mainWindow.app.processEvents()
                print("\""+arduinoLocation+"\\arduino_debug.exe\" --verify --board arduino:avr:"+board+" --verbose temporary.ino")
                if os.system("\""+arduinoLocation+"\\arduino_debug.exe\" --verify --board arduino:avr:"+board+" --verbose temporary.ino")!=0:#TODO add CPU e architecture options
                    QtGui.QMessageBox.question(self, 'Alert', "Error at compiling", QtGui.QMessageBox.Ok)
                    return 3
                self.mainWindow.statusLabel.setText("Uploading")
                self.mainWindow.app.processEvents()
                print("\""+arduinoLocation+"\\arduino_debug.exe\" --upload --board arduino:avr:"+board+" --port"+self.arduinoPort+" --verbose temporary.ino")
                if os.system("\""+arduinoLocation+"\\arduino_debug.exe\" --upload --board arduino:avr:"+board+" --port "+self.arduinoPort+" --verbose temporary.ino")!=0:
                    QtGui.QMessageBox.question(self, 'Alert', "Error at uploading", QtGui.QMessageBox.Ok)
                    return 4
                self.arduinoSerial=serial.Serial(self.arduinoPort, int(self.baudRateComboBox.currentText()))
                return 0
            QtGui.QMessageBox.question(self, 'Alert', "Not working with mac yet", QtGui.QMessageBox.Ok)
            return 5
                
        
        
                
