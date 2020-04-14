import OutputPinsHandling
from PyQt4 import QtGui, QtCore

class drawGraph(QtGui.QWidget):
    
    def __init__(self,PosX, PosY, lista,size, height, sizeDivision, timeUnity='ms', zoom=1,fontSize=10, fontColor=QtGui.QColor(255,0,0), fontStyle='Decorative',lineThick=2, lineColor=QtGui.QColor(41,225,140), divisionLineColor=QtGui.QColor(204,195,26), backgroundColor=QtGui.QColor(14,46,32)):
        super(drawGraph, self).__init__()
        self.PosX=PosX
        self.PosY=PosY
        self.lista=lista
        self.lastPosition=PosX+1
        self.time=0
        self.size=size
        self.height=height
        self.zoom=zoom
        self.sizeDivision=sizeDivision
        self.lineThick=lineThick
        self.lineColor=lineColor
        self.line=QtGui.QPen(lineColor, lineThick, QtCore.Qt.SolidLine)
        self.divisionLineColor=divisionLineColor
        self.divisionLine=QtGui.QPen(divisionLineColor, lineThick/2., QtCore.Qt.DotLine)
        self.fontSize=fontSize
        self.fontStyle=fontStyle
        self.fontColor=fontColor
        self.backgroundColor=backgroundColor
        self.timeUnity=timeUnity
        self.graphStatus="INPUT"
        self.mousePressEvent = self.clickOnTheGraph
        self.setMinimumSize(size+fontSize*2+PosX, PosY+height+fontSize*2)
    
#set methods
    def setPosX(self, PosX):
        self.lastPosition=PosX+1
        self.PosX=Posx

    def setPosY(self, PosY):
        self.PosY=PosY
        
    def setLista(self, Lista):
        self.lista=Lista
    
    def setSize(self, size):
        self.size=size
    
    def setSizeDivision(self, sizeDivision):
        self.sizeDivision=sizeDivision
            
    def setHeight(self, height):
        self.height=height
    
    def setZoom(self, zoom):
        self.zoom=zoom
    
    def setFontSize(self, fontSize):
        self.fontSize=fontSize
    
    def setFontStyle(self, fontStyle):
        self.fontStyle=fontStyle
        
    def setFontColor(self, fontColor):
        self.fontColor=fontColor
    
    def setLineThick(self, lineThick):
        self.lineThick=lineThick
        self.setLine(self.lineColor, lineThick)
        self.setDivisionLine(self.divisionLineColor, lineThick)
    
    def setLineColor(self, lineColor):
        self.lineColor=lineColor
        self.setLine(lineColor, self.lineThick)
    
    def setLine(self, lineColor, lineThick):
        self.line=QtGui.QPen(lineColor, lineThick, QtCore.Qt.SolidLine)
    
    def setDivisionLineColor(self, divisionLineColor):
        self.divisionLineColor=divisionLineColor
        self.setDivisionLine(divisionLineColor, self.lineThick)
    
    def setDivisionLine(self, divisionLineColor, lineThick):
        self.divisionLine=QtGui.QPen(divisionLineColor, lineThick/2., QtCore.Qt.DotLine)
    
    def setBackGroundColor(self, backgroundColor):
        self.backgroundColor=backgroundColor
    
    def setTimeUnity(self, timeUnity):
        self.timeUnity=timeUnity
    
    def setGraphStatus(self, graphStatus):
        self.graphStatus=graphStatus
#set methods end

#others methods

#Event method
    def paintEvent(self, event):
        painter=QtGui.QPainter()
        painter.begin(self)
        #self.eraser(painter)
        #self.setGeometry(0,0,self.size,self.height)
        self.resize(self.size, self.height)
        painter.eraseRect(0,0,1000000,1000000)
        self.drawRectangles(painter)
        #self.writeTimeUnity(painter)
        self.drawLines(painter)
        self.writeTimeMark(painter)
        painter.end()

#Draw the background
    def drawRectangles(self, painter):
        painter.setBrush(self.backgroundColor)
        painter.drawRect(self.PosX, self.PosY, self.size, self.height)

#Draw the lines and call for the timeMark method
    def drawLines2OLD(self, painter):
        lastPos=self.PosX+1
        if self.lista==[]:
            return
        for i in range(len(self.lista)):
            painter.setPen(self.line)
            if i!=0:
                if self.lista[i-1]!=self.lista[i]:
                    painter.drawLine(lastPos, self.PosY+self.height*0.1, lastPos, self.PosY+self.height*0.9)
            if self.lista[i]==1:
                height=self.PosY+self.height*0.1
            else:
                height=self.PosY+self.height*0.9
            if i==len(self.lista)-1:
                painter.drawLine(lastPos, height, lastPos, height)
            else:
                painter.drawLine(lastPos, height, lastPos+self.sizeDivision, height)
            lastPos+=self.sizeDivision
            self.lastPosition=lastPos
            self.time=i
            if (i%self.zoom==0):
                self.writeTimeMark(painter)

#Draw the lines and call for the timeMark method
    def drawLines(self, painter):
        lastPos=self.PosX+1
        if self.lista==[]:
            return
        compactLista=OutputPinsHandling.listCampacter(self.lista)
        for i in range(len(compactLista)):
            painter.setPen(self.line)
            if i!=0:
                if compactLista[i-1][0]!=compactLista[i][0]:
                    painter.drawLine(lastPos, self.PosY+self.height*0.1, lastPos, self.PosY+self.height*0.9)
            if compactLista[i][0]==1:
                height=self.PosY+self.height*0.1
            else:
                height=self.PosY+self.height*0.9
            #if i==len(compactLista)-1:
                #painter.drawLine(lastPos, height, lastPos, height)
            #else:
            painter.drawLine(lastPos, height, lastPos+compactLista[i][1]*self.sizeDivision, height)
            lastPos+=compactLista[i][1]*self.sizeDivision
            self.lastPosition=lastPos
                
#Draw the timeMark
    def writeTimeMarkOLD(self, painter):
       painter.setPen(self.fontColor)
       painter.setFont(QtGui.QFont(self.fontStyle, self.fontSize))
       painter.drawText(self.lastPosition-self.sizeDivision-self.fontSize/3, self.PosY+self.height+self.fontSize*1.2, str(self.time))
       painter.setPen(self.divisionLine)
       painter.drawLine(self.lastPosition-self.sizeDivision, self.PosY+self.height, self.lastPosition-self.sizeDivision, self.PosY)

#Draw the timeMark
    def writeTimeMark(self, painter):
       if self.lista==[]:
           return
       for i in range(0, len(self.lista)+self.zoom,self.zoom):
        painter.setPen(self.fontColor)
        painter.setFont(QtGui.QFont(self.fontStyle, self.fontSize))
        painter.drawText(self.PosX+(i-1)*self.sizeDivision-self.fontSize/3., self.PosY+self.height+self.fontSize*1.2, str(i))
        painter.setPen(self.divisionLine)
        painter.drawLine(self.PosX+(i-1)*self.sizeDivision, self.PosY+self.height, self.PosX+(i-1)*self.sizeDivision, self.PosY)
       
#draw the timeUnity
    def writeTimeUnity(self,painter):
        painter.setPen(self.fontColor)
        painter.setFont(QtGui.QFont(self.fontStyle, self.fontSize))
        painter.drawText(self.PosX+self.size, self.PosY+self.height+self.fontSize*1.2, self.timeUnity)
        
#graph clicked event
    def clickOnTheGraph(self, clickEvent):
        if self.graphStatus=="OUTPUT":
            xClicked=clickEvent.pos().x()
            xClickedRealPos=(xClicked/50)*self.zoom
            if xClickedRealPos<len(self.lista):
                newValue=0
                if self.lista[xClickedRealPos]==0:
                    newValue=1
                index=xClickedRealPos
                while (index<xClickedRealPos+self.zoom) and index<len(self.lista):
                    self.lista[index]=newValue
                    index+=1
                self.repaint()
            
            
