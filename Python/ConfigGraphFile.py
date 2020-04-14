import os
import platform
from PyQt4 import QtGui

#this function create the configFile
def writeConfigFile(fontSize=10,fontStyle="Decorative",fontColor=QtGui.QColor(255,0,0),backgroundColor=QtGui.QColor(14,46,32),lineColor=QtGui.QColor(41,225,140),DivisionLineColor=QtGui.QColor(204,195,26),LineThick=2,GraphHeight=150):
    configFile=open('configGraphFile', 'w')
    configFile.write('fontSize='+str(fontSize)+'\n')
    configFile.write('fontStyle='+str(fontStyle)+'\n')
    configFile.write('fontColor='+str(fontColor.getRgb())+'\n')
    configFile.write('backgroundColor='+str(backgroundColor.getRgb())+'\n')
    configFile.write('lineColor='+str(lineColor.getRgb())+'\n')
    configFile.write('DivisionLineColor='+str(DivisionLineColor.getRgb())+'\n')
    configFile.write('LineThick='+str(LineThick)+'\n')
    configFile.write('GraphHeight='+str(GraphHeight)+'\n')
    configFile.close()

#this function check if the configFile existis, if not, call writeConfigFile with default values
#if configFile existis return all the values in a list
def getFileConfigs():
    if not (os.path.isfile('./configGraphFile')):
        writeConfigFile()
    configFile=open('configGraphFile', 'r')
    lines=configFile.readlines()
    values=[]
    platformUsing=platform.system()
    try:
        fontSize=int(lines[0][9:])
        if fontSize<0 or fontSize>20:
            print("fontSize invalid range")
            return corruptedFileTreatment(platformUsing, configFile)  
    except:
        print("fontSize invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[fontSize]
    if lines[1][10:-1] not in ["AnyStyle","SansSerif","Helvetica","Serif","Times","TypeWriter","Courier","OldEnglish","Decorative","Monospace","Fantasy","Cursive","System"]:
            print("fontStyle invalid")
            return corruptedFileTreatment(platformUsing, configFile)
    values+=[lines[1][10:-1]]
    fontColor=convertStringToList(lines[2][10:])
    if fontColor==None:
        print("fontColor invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[fontColor]
    backgroundColor=convertStringToList(lines[3][16:])
    if backgroundColor==None:
        print("backgroundColor invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[backgroundColor]
    lineColor=convertStringToList(lines[4][10:])
    if lineColor==None:
        print("lineColor invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[lineColor]
    DivisionLineColor=convertStringToList(lines[5][18:])
    if DivisionLineColor==None:
        print("DivisionLineColor invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[DivisionLineColor]
    try:
        LineThick=int(lines[6][10:])
        if LineThick<0 or LineThick>5:
            print("LineThick invalid rage")
            return corruptedFileTreatment(platformUsing, configFile)
    except:
        print("LineThick invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[LineThick]
    try:
        GraphHeight=int(lines[7][12:])
        if GraphHeight<10 or GraphHeight>200:
            print("GraphHeight invalid range")
            return corruptedFileTreatment(platformUsing, configFile)
    except:
        print("GraphHeight invalid")
        return corruptedFileTreatment(platformUsing, configFile)
    values+=[GraphHeight]
    configFile.close()
    return values
        

#receives a string with the format "(255, 0, 0, 255)\n" and return [255,0,0,255]
#return None if the file is corrupted
def convertStringToList(string):
    outputList=[]
    string=string[1:-2]
    try:
        while ',' in string:
            coma=string.index(',')
            outputList+=[int(string[:coma])]
            string=string[coma+1:]
        outputList+=[int(string)]
    except:
        return
    for i in outputList:
        if i<0 or i>255:
            return
    return outputList

def corruptedFileTreatment(platformUsing, configFile):
    if platformUsing=="Linux":
        os.popen("cp configGraphFile configGraphFileCorrupted")
    if platformUsing=="Windows":
        os.popen("move configGraphFile configGraphFileCorrupted")
    configFile.close()
    os.remove("configGraphFile")
    return getFileConfigs()
            
        
    
