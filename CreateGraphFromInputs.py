import ListCleaning
import ConfigGraphFile
import DrawGraph
from PyQt4 import QtGui

#not used anymore
def createGraphFromInputs(mainFrame):
    graphSettings=ConfigGraphFile.getFileConfigs()
    for i in range(len(mainFrame.graphInputs)):
        lista,period, startBit=ListCleaning.clearList(mainFrame.graphInputs[i])
        lista=ListCleaning.convertList(lista)
        print(period)
        graph=DrawGraph.drawGraph(5, 10, lista, len(lista), height=graphSettings[7],sizeDivision=0.05,zoom=1000,fontSize=graphSettings[0],fontColor=QtGui.QColor(graphSettings[2][0],graphSettings[2][1],graphSettings[2][2]),fontStyle=graphSettings[1],lineThick=graphSettings[6],lineColor=QtGui.QColor(graphSettings[4][0],graphSettings[4][1],graphSettings[4][2]),divisionLineColor=QtGui.QColor(graphSettings[5][0],graphSettings[5][1],graphSettings[5][2]),backgroundColor=QtGui.QColor(graphSettings[3][0],graphSettings[3][1],graphSettings[3][2]))
        scrollArea=QtGui.QScrollArea()
        scrollArea.setWidget(graph)
        mainFrame.grid.setRowMinimumHeight(i+1,10+graphSettings[7]+graphSettings[0]*2+20)
        #mainFrame.grid.addWidget(scrollArea, i+1, 2,i+6,10)
        mainFrame.grid.addWidget(scrollArea, i+1, 2, i+1, 10)
        
#this function create an empty graph, return an objet graph
def createGraph():
    graphSettings=ConfigGraphFile.getFileConfigs()
    graph=DrawGraph.drawGraph(5, 10+240-graphSettings[7]-2*graphSettings[0], [], 550, height=graphSettings[7],sizeDivision=1,zoom=50,fontSize=graphSettings[0],fontColor=QtGui.QColor(graphSettings[2][0],graphSettings[2][1],graphSettings[2][2]),fontStyle=graphSettings[1],lineThick=graphSettings[6],lineColor=QtGui.QColor(graphSettings[4][0],graphSettings[4][1],graphSettings[4][2]),divisionLineColor=QtGui.QColor(graphSettings[5][0],graphSettings[5][1],graphSettings[5][2]),backgroundColor=QtGui.QColor(graphSettings[3][0],graphSettings[3][1],graphSettings[3][2]))
    return graph

#this function update the previous graph created by the createGraph function
def drawFromInputs(mainFrame):
        graphSettings=ConfigGraphFile.getFileConfigs()
        for i in range(len(mainFrame.graphInputs)):
            lista,period, startBit=ListCleaning.clearList(mainFrame.graphInputs[i])
            lista=ListCleaning.convertList(lista)
            mainFrame.graphList[i].graph.setLista(lista)
            mainFrame.graphList[i].graph.setSize(50+len(lista))
            upddateValues(mainFrame.graphList[i].graph, graphSettings)
            mainFrame.graphList[i].graph.repaint()

def upddateValues(graph, graphSettings):
    graph.setHeight(graphSettings[7])
    graph.setFontSize(graphSettings[0])
    graph.setFontStyle(graphSettings[1])
    graph.setPosY(10+240-graphSettings[7]-2*graphSettings[0])
    graph.setFontColor(QtGui.QColor(graphSettings[2][0],graphSettings[2][1],graphSettings[2][2]))
    graph.setLineThick(graphSettings[6])
    graph.setLineColor(QtGui.QColor(graphSettings[4][0],graphSettings[4][1],graphSettings[4][2]))
    graph.setDivisionLineColor(QtGui.QColor(graphSettings[5][0],graphSettings[5][1],graphSettings[5][2]))
    graph.setBackGroundColor(QtGui.QColor(graphSettings[3][0],graphSettings[3][1],graphSettings[3][2]))
        
    
