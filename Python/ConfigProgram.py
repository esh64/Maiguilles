from PyQt4 import QtGui
import ConfigProgramFile

class configProgram(QtGui.QDialog):
    
    def __init__(self, mainWindow):
        super(configProgram, self).__init__()
        self.mainWindow=mainWindow
        self.initUI()

    def initUI(self):
        self.getConfigFilesDates()
    
    #buttons
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.okButtonAction)
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancelButtonAction)
        #buttons end

    #grid creation
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(5)
    #grid creation end

    #Arduino board		
        arduinoBoardLabel = QtGui.QLabel('Arduino Board')
        self.grid.addWidget(arduinoBoardLabel,0,0)
        self.arduinoBoardComboBox=QtGui.QComboBox()
        self.arduinoBoardComboBox.addItems(["uno", "due", "mega", "nano", "yun", "leonardo", "lillypad", "esplora", "micro", "ethernet", "fio"])
        self.arduinoBoardComboBox.setCurrentIndex (["uno", "due", "mega", "nano", "yun", "leonardo", "lillypad", "esplora", "micro", "ethernet", "fio"].index(self.board))
        self.grid.addWidget(self.arduinoBoardComboBox,0,1)
    #Arduino board end
        
    #TODO add the microcontroller variation for the same board
    #TODO add microcontroller frequency(maybe)

    #Arduino mk location
        if self.mainWindow.platform=="Linux":
            arduinoMakefileLocationLabel = QtGui.QLabel('Arduino Makefile location')
            self.grid.addWidget(arduinoMakefileLocationLabel,1,0)
            self.arduinoMakefileLocationLineedit=QtGui.QLineEdit(self)
            self.arduinoMakefileLocationLineedit.setText( self.location)
            self.grid.addWidget(self.arduinoMakefileLocationLineedit,1,1)
            arduinoMakefileLocationPicker = QtGui.QPushButton('Pick', self)
            arduinoMakefileLocationPicker.clicked.connect(self.arduinoMakefileLocationDialog)
            self.grid.addWidget(arduinoMakefileLocationPicker,1,2)
    #Arduino mk location end
    
    
        if self.mainWindow.platform=="Windows":
            #Arduino IDE Location
            arduinoIDELocationLabel = QtGui.QLabel('Arduino IDE location')
            self.grid.addWidget(arduinoIDELocationLabel,1,0)
            self.arduinoIDELocationLineedit=QtGui.QLineEdit(self)
            self.arduinoIDELocationLineedit.setText( self.location)
            self.grid.addWidget(self.arduinoIDELocationLineedit,1,1)
            arduinoIDELocationPicker = QtGui.QPushButton('Pick', self)
            arduinoIDELocationPicker.clicked.connect(self.arduinoIDELocationDialog)
            self.grid.addWidget(arduinoIDELocationPicker,1,2)
            #Arduino IDE location end
            
            ##Arduino libraries Location
            #arduinoIDELocationLabel = QtGui.QLabel('Arduino Libraries location')
            #self.grid.addWidget(arduinoIDELocationLabel,2,0)
            #self.arduinoLIBLocationLineedit=QtGui.QLineEdit(self)
            #self.arduinoLIBLocationLineedit.setText( self.location2)
            #self.grid.addWidget(self.arduinoLIBLocationLineedit,2,1)
            #arduinoLIBLocationPicker = QtGui.QPushButton('Pick', self)
            #arduinoLIBLocationPicker.clicked.connect(self.arduinoLIBLocationDialog)
            #self.grid.addWidget(arduinoLIBLocationPicker,2,2)
            ##Arduino libraries location end

        hboxButtons = QtGui.QHBoxLayout()
        hboxButtons.addStretch(0)
        hboxButtons.addWidget(cancelButton)
        hboxButtons.addWidget(okButton)

        self.grid.addLayout(hboxButtons, 3, 2)
        self.setLayout(self.grid) 
        self.setGeometry(300, 300, 600, 120)
        self.setFixedSize(600,120)
        self.setWindowTitle('Configure Program')
        self.setWindowIcon(QtGui.QIcon("Maiguilles.png"))

    #buttons
    #save the values in the config file and close
    def okButtonAction(self):
        if self.mainWindow.platform=="Linux":
            ConfigProgramFile.writeConfigFile(self.arduinoBoardComboBox.currentText(),  self.arduinoMakefileLocationLineedit.text())
            #if (self.mainWindow.statusLabel.text()=="Config Program file not found"):
                #self.mainWindow.statusLabel.setText("Ready")
            self.close()
        if self.mainWindow.platform=="Windows":
            ConfigProgramFile.writeConfigFile(self.arduinoBoardComboBox.currentText(),  self.arduinoIDELocationLineedit.text())
            self.close()
    #close without save
    def cancelButtonAction(self):
        self.close()
    #buttons end

    def arduinoMakefileLocationDialog(self):
        self.arduinoMakefileLocationLineedit.setText(QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', '/	'))
        
    def arduinoIDELocationDialog(self):
        self.arduinoIDELocationLineedit.setText(QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', '/	'))
        
    #def arduinoLIBLocationDialog(self):
        #self.arduinoLIBLocationLineedit.setText(QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', '/	'))
    
    #Config file
    def getConfigFilesDates(self):
        dates=ConfigProgramFile.getFileConfigs()
        self.board=dates[0]
        self.location=dates[1]
        #if self.mainWindow.platform=="Windows":
            #self.location2=dates[2]
    #Config file end
    
    
