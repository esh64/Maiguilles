from PyQt4 import QtCore
import CheckArduinoConnected
import os

class checkReady (QtCore.QThread):
    def __init__(self, mainFrame):
        QtCore.QThread.__init__(self)
        self.mainFrame=mainFrame
    
    def run(self):
        while (True):
            if  not(os.path.isfile('./configProgramFile')):
                if (self.mainFrame.mainWindow.statusLabel.text()!="config program file not found"):
                    self.mainFrame.mainWindow.statusLabel.setText("config program file not found")
                    self.mainFrame.mainWindow.app.processEvents()
                    continue
            else:
                self.mainFrame.arduinoPort=CheckArduinoConnected.checkArduinoConected(self.mainFrame.platform)
                if (self.mainFrame.arduinoPort==''):
                    if (self.mainFrame.mainWindow.statusLabel.text()!="No arduino connected"):
                        self.mainFrame.mainWindow.statusLabel.setText("No arduino connected")
                        self.mainFrame.mainWindow.app.processEvents()
                        continue
                else:
                    if (self.mainFrame.mainWindow.statusLabel.text()!="Ready"):
                        self.mainFrame.mainWindow.statusLabel.setText("Ready")
                        self.mainFrame.mainWindow.app.processEvents()
                        continue
