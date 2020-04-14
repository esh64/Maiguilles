from PyQt4 import QtGui

class coloredSquare(QtGui.QWidget):
    def __init__(self, color, width=100, height=20):
        super(coloredSquare, self).__init__()
        self.color=color
        self.width=width
        self.height=height
    
    def setColor(self, color):
        self.color=color
    
    def setWidth(self, width): 
        self.width=width
    
    def setHeight(self, height):
        self.height=height
    
    def paintEvent(self, event):
        painter=QtGui.QPainter()
        painter.begin(self)
        painter.setBrush(self.color)
        painter.drawRect(0, 0, self.width, self.height)
        painter.end()
        
