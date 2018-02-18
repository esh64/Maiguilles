#TODO check difference in performance using thread and Qthread

from PyQt4 import QtCore
import serial

class arduinoProgramInterface(QtCore.QThread):
    def __init__(self,mainFrame):
        QtCore.QThread.__init__(self)
        #self.graphInputNumber=graphInputNumber
        self.mainFrame=mainFrame
        
    def run(self):
        self.mainFrame.graphInputs=[]
        graphInputs=[]
        #for i in range(self.graphInputNumber):
            #graphInputs+=[[]]
        for i in self.mainFrame.usedPins[1]:
            if i=="INPUT":
                graphInputs+=[[]]
        while self.mainFrame.startButton.text()=="Stop":
            for i in range(len(graphInputs)):
                graphInputs[i]+=[str(self.mainFrame.arduinoSerial.read())]
        if graphInputs==[]:
            graphInputs=None
        self.mainFrame.arduinoSerial.close()
        self.mainFrame.graphInputs=graphInputs
        
        
#import threading
#import serial

#class arduinoProgramInterface(threading.Thread):
    #def __init__(self, graphInputNumber,mainFrame):
        #threading.Thread.__init__(self)
        #self.graphInputNumber=graphInputNumber
        #self.mainFrame=mainFrame
        
    #def run(self):
        #graphInputs=[]
        #for i in range(self.graphInputNumber):
            #graphInputs+=[[]]
        #while self.mainFrame.startButton.text()=="Stop":
            #for i in range(len(graphInputs)):
                #graphInputs[i]+=[str(self.mainFrame.arduinoSerial.read())]
        #self.mainFrame.arduinoSerial.close()
        #self.mainFrame.graphInputs=graphInputs
        

