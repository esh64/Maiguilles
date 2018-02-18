from PyQt4 import QtGui
import ColoredSquares
import DrawGraph
import ConfigGraphFile

class configGraph(QtGui.QDialog):
    
        def __init__(self, frame):
            super(configGraph, self).__init__()
            self.frame=frame
            self.initUI()
        
        def initUI(self):
            self.getConfigFilesDates()
            
            #buttons
            okButton = QtGui.QPushButton("OK")
            okButton.clicked.connect(self.okButtonAction)
            cancelButton = QtGui.QPushButton("Cancel")
            cancelButton.clicked.connect(self.cancelButtonAction)
            ApplyButton = QtGui.QPushButton("Apply")
            ApplyButton.clicked.connect(self.ApplyButtonAction)
            DefaultButton = QtGui.QPushButton("Default")
            DefaultButton.clicked.connect(self.DefaultButtonAction)
            #buttons end
            
            labelsList=[]
            widGetsList=[]
            
            #font size
            fontSizeLabel = QtGui.QLabel('Font Size')
            labelsList+=[fontSizeLabel]
            self.fontSizeWid=QtGui.QSpinBox()
            self.fontSizeWid.setRange(1,20)
            self.fontSizeWid.setSingleStep(1)
            self.fontSizeWid.setValue(self.fontSize)
            widGetsList+=[[self.fontSizeWid,]]
            #font size end
            
            #font style
            fontStyleLabel = QtGui.QLabel('Font Style')
            labelsList+=[fontStyleLabel]
            self.fontStyleComboBox=QtGui.QComboBox()
            self.fontStyleComboBox.addItems(["AnyStyle","SansSerif","Helvetica","Serif","Times","TypeWriter","Courier","OldEnglish","Decorative","Monospace","Fantasy","Cursive","System"])
            self.fontStyleComboBox.setCurrentIndex (["AnyStyle","SansSerif","Helvetica","Serif","Times","TypeWriter","Courier","OldEnglish","Decorative","Monospace","Fantasy","Cursive","System"].index(self.fontStyle))
            widGetsList+=[[self.fontStyleComboBox,]]
            #font style end
            
            #font color
            fontColorLabel = QtGui.QLabel('Font Color')
            labelsList+=[fontColorLabel]
            self.fontColorPicker = QtGui.QPushButton('Pick', self)
            self.fontColorPicker.clicked.connect(self.fontColorPickerDialog)
            self.fontColorSquare=ColoredSquares.coloredSquare(self.fontColor)
            widGetsList+=[[self.fontColorPicker,self.fontColorSquare]]
            #font color end
            
            #background color
            backgroundColorLabel = QtGui.QLabel('Background Color')
            labelsList+=[backgroundColorLabel]
            self.backgroundColorPicker = QtGui.QPushButton('Pick', self)
            self.backgroundColorPicker.clicked.connect(self.backgroundColorPickerDialog)
            self.backgroundColorSquare=ColoredSquares.coloredSquare(self.backgroundColor)
            widGetsList+=[[self.backgroundColorPicker,self.backgroundColorSquare]]
            #background color end
            
            #line color
            lineColorLabel = QtGui.QLabel('Line Color')
            labelsList+=[lineColorLabel]
            self.lineColorPicker = QtGui.QPushButton('Pick', self)
            self.lineColorPicker.clicked.connect(self.lineColorPickerDialog)
            self.lineColorSquare=ColoredSquares.coloredSquare(self.lineColor)
            widGetsList+=[[self.lineColorPicker,self.lineColorSquare]]
            #line color end
            
            #divisionLine color
            divisionLineColorLabel = QtGui.QLabel('Division Line Color')
            labelsList+=[divisionLineColorLabel]
            self.divisionLineColorPicker = QtGui.QPushButton('Pick', self)
            self.divisionLineColorPicker.clicked.connect(self.divisionLineColorPickerDialog)
            self.divisionLineColorSquare=ColoredSquares.coloredSquare(self.divisionLineColor)
            widGetsList+=[[self.divisionLineColorPicker,self.divisionLineColorSquare]]
            #divisionLine color end
            
            #lineThick
            lineThickLabel = QtGui.QLabel('Line Thick')
            labelsList+=[lineThickLabel]
            self.lineThickWid=QtGui.QSpinBox()
            self.lineThickWid.setRange(1,5)
            self.lineThickWid.setSingleStep(1)
            self.lineThickWid.setValue(self.lineThick)
            widGetsList+=[[self.lineThickWid,]]
            #lineThick end
            
            #graph Height
            graphHeightLabel=QtGui.QLabel('Graph Height')
            labelsList+=[graphHeightLabel]
            self.graphHeightWid=QtGui.QSpinBox()
            self.graphHeightWid.setRange(10,200)
            self.graphHeightWid.setSingleStep(1)
            self.graphHeightWid.setValue(self.graphHeight)
            widGetsList+=[[self.graphHeightWid,]]
            #graph Height end
            
            #grid
            self.grid = QtGui.QGridLayout()
            self.grid.setSpacing(5)
            for i in range(len(widGetsList)):
                if (len(widGetsList[i])==2):
                    self.grid.addWidget(widGetsList[i][0],i, 2)
                    self.grid.addWidget(widGetsList[i][1],i, 1)
                else:
                    self.grid.addWidget(widGetsList[i][0],i,1)
                self.grid.addWidget(labelsList[i], i, 0)
            #grid end
            
            #hbox buttons
            hboxButtons = QtGui.QHBoxLayout()
            hboxButtons.addStretch(0)
            hboxButtons.addWidget(DefaultButton)
            hboxButtons.addWidget(ApplyButton)
            hboxButtons.addWidget(cancelButton)
            hboxButtons.addWidget(okButton)
            #hbox buttons end

            self.insertGraph()
            self.grid.addLayout(hboxButtons, 20, 20)
            self.setLayout(self.grid) 
            self.setGeometry(300, 300, 900, 400)
            #self.setFixedSize(900,300)
            self.setWindowTitle('Configure Graph')
            self.setWindowIcon(QtGui.QIcon("Maiguilles.png"))
    
        #Config file
        def getConfigFilesDates(self):
            dates=ConfigGraphFile.getFileConfigs()
            self.fontSize=dates[0]
            self.fontStyle=dates[1]
            self.fontColor=QtGui.QColor(dates[2][0],dates[2][1],dates[2][2])
            self.backgroundColor=QtGui.QColor(dates[3][0],dates[3][1],dates[3][2])
            self.lineColor=QtGui.QColor(dates[4][0],dates[4][1],dates[4][2])
            self.divisionLineColor=QtGui.QColor(dates[5][0],dates[5][1],dates[5][2])
            self.lineThick=dates[6]
            self.graphHeight=dates[7]
        #Config file end
         
    #widgets
        #color dialog
        def fontColorPickerDialog(self):
            self.fontColor = QtGui.QColorDialog.getColor()
            if self.fontColor.isValid():
                self.fontColorSquare.setColor(self.fontColor)
		self.fontColorSquare.repaint()
        
        def backgroundColorPickerDialog(self):
            self.backgroundColor = QtGui.QColorDialog.getColor()
            if self.backgroundColor.isValid():
                self.backgroundColorSquare.setColor(self.backgroundColor)
		self.backgroundColorSquare.repaint()
        
        def lineColorPickerDialog(self):
            self.lineColor = QtGui.QColorDialog.getColor()
            if self.lineColor.isValid():
                self.lineColorSquare.setColor(self.lineColor)
		self.lineColorSquare.repaint()
        
        def divisionLineColorPickerDialog(self):
            self.divisionLineColor = QtGui.QColorDialog.getColor()
            if self.divisionLineColor.isValid():
                self.divisionLineColorSquare.setColor(self.divisionLineColor)
		self.divisionLineColorSquare.repaint()
        #color dialog end
        
        #graph
        def insertGraph(self):
            lista=[1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,1]
            size=500
            PosX=10
            PosY=10
            self.graph = DrawGraph.drawGraph(PosX, PosY, lista,size, self.graphHeight,size/len(lista), 'ms', 1, self.fontSize, self.fontColor, self.fontStyle, self.lineThick, self.lineColor, self.divisionLineColor, self.backgroundColor)
            scrollArea=QtGui.QScrollArea()
            scrollArea.setWidgetResizable(True)
            scrollArea.setWidget(self.graph)
            self.grid.addWidget(scrollArea, 0,3,7,20)
        #graph end
        
        #buttons
        #save the values in the config file and close
        def okButtonAction(self):
            self.upddateValues(self.fontSizeWid.value(),self.fontStyleComboBox.currentText(),self.lineThickWid.value(),self.graphHeightWid.value())
            ConfigGraphFile.writeConfigFile(self.fontSize, self.fontStyle, self.fontColor, self.backgroundColor, self.lineColor, self.divisionLineColor, self.lineThick, self.graphHeight)
            for i in self.frame.graphList:
                i.graph.setHeight(self.graphHeight)
                i.graph.setFontSize(self.fontSize)
                i.graph.setFontStyle(self.fontStyle)
                i.graph.setFontColor(self.fontColor)
                i.graph.setLineThick(self.lineThick)
                i.graph.setLineColor(self.lineColor)
                i.graph.setDivisionLineColor(self.divisionLineColor)
                i.graph.setBackGroundColor(self.backgroundColor)
                i.graph.repaint()
            self.close()
        #close without save
        def cancelButtonAction(self):
            self.close()
        
        #apply the changes in the model graph, does not save
        def ApplyButtonAction(self):
            self.upddateValues(self.fontSizeWid.value(),self.fontStyleComboBox.currentText(),self.lineThickWid.value(),self.graphHeightWid.value())
            self.graph.repaint()
        #set the default values, does not save
        def DefaultButtonAction(self):
            self.fontColor=QtGui.QColor(255,0,0)
            self.backgroundColor=QtGui.QColor(14,46,32)
            self.lineColor=QtGui.QColor(41,225,140)
            self.divisionLineColor=QtGui.QColor(204,195,26)
            self.upddateValues()
            self.fontSizeWid.setValue(self.fontSize)
            self.fontStyleComboBox.setCurrentIndex (["AnyStyle","SansSerif","Helvetica","Serif","Times","TypeWriter","Courier","OldEnglish","Decorative","Monospace","Fantasy","Cursive","System"].index(self.fontStyle))
            self.lineThickWid.setValue(self.lineThick)
            self.graphHeightWid.setValue(self.graphHeight)
            self.fontColorSquare.setColor(self.fontColor)
            self.fontColorSquare.repaint()
            self.backgroundColorSquare.setColor(self.backgroundColor)
            self.backgroundColorSquare.repaint()
            self.lineColorSquare.setColor(self.lineColor)
            self.lineColorSquare.repaint()
            self.divisionLineColorSquare.setColor(self.divisionLineColor)
            self.divisionLineColorSquare.repaint()
            self.graph.repaint()
            
        def upddateValues(self, fontSize=10,fontStyle="Decorative",lineThick=2,graphHeight=150):
            self.fontSize=fontSize
            self.fontStyle=fontStyle
            self.lineThick=lineThick
            self.graphHeight=graphHeight
            self.graph.setHeight(self.graphHeight)
            self.graph.setFontSize(self.fontSize)
            self.graph.setFontStyle(self.fontStyle)
            self.graph.setFontColor(self.fontColor)
            self.graph.setLineThick(self.lineThick)
            self.graph.setLineColor(self.lineColor)
            self.graph.setDivisionLineColor(self.divisionLineColor)
            self.graph.setBackGroundColor(self.backgroundColor)
        #buttons end
    #widgets end
            
            
