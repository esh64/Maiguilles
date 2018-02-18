import GraphWidget
from PyQt4 import QtGui, QtCore

#figure out to make this a widget
class menuGraphItens(QtGui.QWidget):
    def __init__(self, mainFrame):
        super(menuGraphItens, self).__init__()
        self.mainFrame=mainFrame
        self.mainFrame.graphCount+=1
        self.pinMode=QtGui.QComboBox()
        self.pinMode.addItem("INPUT")
        self.pinMode.addItem("OUTPUT")
        self.pinMode.activated.connect(self.changePinMode)
        self.pinNumber=QtGui.QComboBox()
        self.setPinNumberOptions()
        self.removeNewPinNumberItemFromOthers(self.pinNumberList[0])
        self.value=self.pinNumberList[0]
        self.pinNumber.activated.connect(self.changePinNumber)
        self.graphWidget=GraphWidget.graphWidget()
        self.graph=self.graphWidget.graph
        self.zoomSlider=self.graphWidget.slider
        self.mainFrame.usedPins[0]+=[str(self.pinNumber.currentText())]
        self.mainFrame.usedPins[1]+=[str(self.pinMode.currentText())]
        self.setupLayout()
    
    #if i need to make any change, i can just change this as an square
    #this will make the things fancier
    def setupLayout(self):
        self.mainFrame.vboxWidget.resize(700,480*self.mainFrame.graphCount)
        self.grid=QtGui.QGridLayout()
        self.grid.setAlignment(QtCore.Qt.AlignCenter)
        self.grid.setHorizontalSpacing (10)
        self.grid.setVerticalSpacing(0)
        self.grid.setRowStretch(0,0)
        self.emptySpace=QtGui.QLabel(' ')
        self.emptySpace.setFixedWidth(5)
        
        self.removeButton = QtGui.QPushButton("Remove")
        self.removeButton.clicked.connect(self.removeWidgetAction)
        self.grid.addWidget(self.removeButton,0,9)
        
        self.grid.addWidget(self.pinMode,0,4)
        self.pinModeLabel=QtGui.QLabel('Pin Mode')
        self.pinMode.setFixedWidth(80)
        self.pinModeLabel.setFixedWidth(80)
        self.grid.addWidget(self.pinModeLabel,0,3)
        
        self.grid.addWidget(self.pinNumber,0,2)
        self.pinNumberLabel=QtGui.QLabel('Pin Number')
        self.pinNumberLabel.setFixedWidth(80)
        self.pinNumber.setFixedWidth(80)
        self.grid.addWidget(self.pinNumberLabel,0,1)
        
        self.grid.addWidget(self.emptySpace,0,0)
        
        self.expandGraphButton=QtGui.QPushButton("Expand")
        self.expandGraphButton.setFixedWidth(70)
        self.expandGraphButton.clicked.connect(self.expandGraphAction)
        self.expandGraphButton.hide()
        self.grid.addWidget(self.expandGraphButton,1,1)
        
        self.reduceGraphButton=QtGui.QPushButton("Reduce")
        self.reduceGraphButton.setFixedWidth(70)
        self.reduceGraphButton.clicked.connect(self.reduceGraphAction)
        self.reduceGraphButton.hide()
        self.grid.addWidget(self.reduceGraphButton,1,2)
        
        self.textFromLabel=QtGui.QLabel('From')
        self.textFromLabel.setFixedWidth(40)
        self.grid.addWidget(self.textFromLabel,1,3)
        self.textLineFrom=QtGui.QLineEdit("0")
        self.textLineFrom.setFixedWidth(70)
        self.grid.addWidget(self.textLineFrom,1,4)
        self.textToLabel=QtGui.QLabel('To')
        self.textToLabel.setFixedWidth(20)
        self.grid.addWidget(self.textToLabel,1,5)
        self.textLineTo=QtGui.QLineEdit("0")
        self.textLineTo.setFixedWidth(70)
        self.grid.addWidget(self.textLineTo,1,6)
        
        self.editGraphComboBox=QtGui.QComboBox()
        self.editGraphComboBox.addItem("Copy")
        self.editGraphComboBox.setFixedWidth(100)
        self.editGraphComboBox.activated.connect(self.changeEditComboboxOption)
        self.grid.addWidget(self.editGraphComboBox,1,7)
        
        self.editGraphButton=QtGui.QPushButton("Copy graph section")
        self.editGraphButton.clicked.connect(self.editGraphAction)
        self.editGraphButton.setFixedWidth(170)
        self.grid.addWidget(self.editGraphButton,1,9)
        
        self.grid.addWidget(self.graphWidget,2,0,2,10)
        self.mainFrame.vbox.addLayout(self.grid)
    
    def setPinNumberOptions(self):
        self.pinNumberList=[]
        for i in range(2, 14):
            if str(i) not in self.mainFrame.usedPins[0]:
                self.pinNumber.addItem(str(i))
                self.pinNumberList+=[str(i)]
                
    #remove New PinNumber Item From Others PinNumer Combobox
    def removeNewPinNumberItemFromOthers(self, value):
        for i in self.mainFrame.graphList:
            if value not in i.pinNumberList:
                continue
            pos=i.pinNumberList.index(value)
            i.pinNumber.removeItem(pos)
            i.pinNumberList.remove(value)
            
    def changePinNumber(self):
        newValue=str(self.pinNumber.currentText())
        if newValue==self.value:
            return
        for i in self.mainFrame.graphList:
            if i==self:
                continue
            pos=i.pinNumberList.index(newValue)
            i.pinNumber.removeItem(pos)
            i.pinNumberList.remove(newValue)
            i.pinNumber.addItem(self.value)
            i.pinNumberList+=[self.value]
        self.mainFrame.usedPins[0].remove(self.value)
        self.mainFrame.usedPins[0]+=[newValue]
        self.value=newValue
    
    def changePinMode(self):
        self.graphWidget.graph.graphStatus=self.pinMode.currentText()
        if self.graphWidget.graph.graphStatus=="INPUT":
            self.expandGraphButton.hide()
            self.reduceGraphButton.hide()
            for i in range(7, 0, -1):
                self.editGraphComboBox.removeItem(i)
            self.editGraphButton.setText("Copy graph section")
            self.textLineTo.setDisabled(False)
        else:
            self.expandGraphButton.show()
            self.reduceGraphButton.show()
            self.editGraphComboBox.addItems(["Delete", "Negate", "All 1", "All 0", "Reverse", "Paste in", "Substitute"])
        if self.graphWidget.graph.graphStatus=="OUTPUT" and self.graphWidget.graph.lista==[]:
            self.graphWidget.graph.lista=[0]*500
            self.graphWidget.graph.repaint()
    
    def removeWidgetAction(self):
        for i in self.mainFrame.graphList:
            if i==self:
                continue
            i.pinNumber.addItem(self.value)
            i.pinNumberList+=[self.value]
        self.mainFrame.graphCount-=1
        self.mainFrame.graphList.remove(self)
        self.mainFrame.usedPins[0].remove(self.value)
        self.mainFrame.vboxWidget.resize(700,480*self.mainFrame.graphCount)
        self.mainFrame.vbox.removeItem(self.grid)
        self.emptySpace.deleteLater()
        self.emptySpace=None
        self.removeButton.deleteLater()
        self.removeButton=None
        self.graphWidget.deleteLater()
        self.graphWidget=None
        self.pinNumber.deleteLater()
        self.pinNumber=None
        self.pinMode.deleteLater()
        self.pinMode=None
        self.pinNumberLabel.deleteLater()
        self.pinNumberLabel=None
        self.pinModeLabel.deleteLater()
        self.pinModeLabel=None
        self.expandGraphButton.deleteLater()
        self.expandGraphButton=None
        self.reduceGraphButton.deleteLater()
        self.reduceGraphButton=None
        self.textFromLabel.deleteLater()
        self.textFromLabel=None
        self.textLineFrom.deleteLater()
        self.textLineFrom=None
        self.textToLabel.deleteLater()
        self.textToLabel=None
        self.textLineTo.deleteLater()
        self.textLineTo=None
        self.editGraphComboBox.deleteLater()
        self.editGraphComboBox=None
        self.editGraphButton.deleteLater()
        self.editGraphButton=None
        self.deleteLater()
        self=None
    
    def expandGraphAction(self):
        self.graph.lista+=[0]*self.graph.zoom
        self.graph.setSize(50+(len(50*self.graph.lista)/float(self.graph.zoom)))
        self.graph.repaint()
    
    def reduceGraphAction(self):
        if self.graph.size>500/float(self.graph.zoom):
            self.graph.lista=self.graph.lista[:-self.graph.zoom]
            self.graph.setSize(50+(50*len(self.graph.lista)/float(self.graph.zoom)))
            self.graph.repaint()
            
    def changeEditComboboxOption(self):
        self.editGraphButton.setText(self.editGraphComboBox.currentText()+" graph section")
        if self.editGraphButton.text()=="Paste in graph section":
            self.textLineTo.setDisabled(True)
        else:
            self.textLineTo.setDisabled(False)
        
    def editGraphAction(self):
        try:
            initialValue=int(self.textLineFrom.text())
            if self.editGraphButton.text()=="Paste in graph section":
                finalValue=initialValue+1
            else:
                finalValue=int(self.textLineTo.text())
        except:
            print("valor invalido")
            return
        if initialValue<0 or initialValue>finalValue or finalValue>len(self.graph.lista):
            print("valor invalido")
            return
        if self.editGraphButton.text()=="Copy graph section":
            self.mainFrame.clipboard=self.graph.lista[initialValue:finalValue+1]
            return
        if self.editGraphButton.text()=="Delete graph section":
            temporaryLista1=self.graph.lista[:initialValue]
            temporaryLista2=self.graph.lista[finalValue:]
            self.graph.setLista(temporaryLista1+temporaryLista2)
            self.graph.setSize(50+(len(50*self.graph.lista)/float(self.graph.zoom)))
            self.graph.repaint()
            return
        if self.editGraphButton.text()=="Negate graph section":
            for i in range(initialValue, finalValue):
                if self.graph.lista[i]==1:
                    self.graph.lista[i]=0
                else:
                    self.graph.lista[i]=1
            self.graph.repaint()
            return
        if self.editGraphButton.text()=="All 1 graph section":
            for i in range(initialValue, finalValue):
                self.graph.lista[i]=1
            self.graph.repaint()
            return
        if self.editGraphButton.text()=="All 0 graph section":
            for i in range(initialValue, finalValue):
                self.graph.lista[i]=0
            self.graph.repaint()    
            return
        if self.editGraphButton.text()=="Reverse graph section":
            temporaryLista1=self.graph.lista[:initialValue]
            temporaryLista2=self.graph.lista[finalValue+1:]
            toBeReversed=self.graph.lista[initialValue:finalValue+1]
            self.graph.setLista(temporaryLista1+toBeReversed[::-1]+temporaryLista2)
            self.graph.repaint()
            return
        if self.editGraphButton.text()=="Substitute graph section":
            temporaryLista1=self.graph.lista[:initialValue]
            temporaryLista2=self.graph.lista[finalValue+1:]
            self.graph.setLista(temporaryLista1+self.mainFrame.clipboard+temporaryLista2)
            self.graph.setSize(50+(len(50*self.graph.lista)/float(self.graph.zoom)))
            self.graph.repaint()
            return
        if self.editGraphButton.text()=="Paste in graph section":
            temporaryLista1=self.graph.lista[:initialValue]
            temporaryLista2=self.graph.lista[initialValue:]
            self.graph.setLista(temporaryLista1+self.mainFrame.clipboard+temporaryLista2)
            self.graph.setSize(50+(len(50*self.graph.lista)/float(self.graph.zoom)))
            self.graph.repaint()
            return
