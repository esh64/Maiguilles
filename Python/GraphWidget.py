from PyQt4 import QtGui, QtCore
import CreateGraphFromInputs

class graphWidget(QtGui.QWidget):
    def __init__(self):
        super(graphWidget, self).__init__()
        self.graph=CreateGraphFromInputs.createGraph()
        self.graph.setPosY(10+240-self.graph.height-2*self.graph.fontSize)
        self.slider=QtGui.QSlider(QtCore.Qt.Vertical)
        self.setup()
    
    def setup(self):
        #slider setup#
        self.slider.setMinimum(1)
        self.slider.setMaximum(20)
        self.slider.setValue(1)
        self.slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.sliderValueChange)
        self.zoomLabel=QtGui.QLabel(str(self.slider.value())+"x")
        grid=QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel(""),0,0)
        grid.addWidget(QtGui.QLabel("Zoom"),1,1)
        grid.addWidget(self.slider,2,1)
        grid.addWidget(self.zoomLabel,3,1)
        grid.addWidget(QtGui.QLabel(""),4,0)
        grid.setRowMinimumHeight(0,55)
        grid.setRowMinimumHeight(4,55)
        grid.setSpacing(0)
        #slider setup#
        
        #scrollArea setup#
        self.scrollArea=QtGui.QScrollArea()
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setWidget(self.graph)
        self.scrollArea.setFixedHeight(270)
        #self.scrollArea.setFixedWidth(600)
        #scrollarea setup#
        
        #layout setup
        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(0)
        hbox.setSpacing(5)
        hbox.addLayout(grid)
        hbox.addWidget(self.scrollArea)
        self.setLayout(hbox)
        #layout setup#
    
    def sliderValueChange(self):
        if self.graph.lista!=[]:
            self.graph.setSize(50+(len(self.graph.lista)/float(self.slider.value())))
        self.graph.setSizeDivision(1/float(self.slider.value()))
        self.graph.setZoom(50*self.slider.value())
        self.zoomLabel.setText(str(self.slider.value())+"x")
        self.graph.repaint()

            
        

        
