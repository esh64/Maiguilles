import OutputPinsHandling
#this function receives a list with the pins number and mode and the  baudrate
#return the arduino file for this
#ignore the output graphs with empty list
def makeInoFile(usedPins, baudrate, fileName="temporary.ino", outPutOnly=False):
    inoFile=open(fileName,"w")
    inputOnly=False
    if "OUTPUT" not in usedPins[1]:
        inputOnly=True
    if not inputOnly:
        inoFile.write("unsigned long long timemark=0;\n\n")#set this only if there is output
    inoFile.write("void setup()\n")
    inoFile.write("{\n")
    if not outPutOnly:
        inoFile.write("\tSerial.begin("+str(baudrate)+");\n")
    for i in range(len(usedPins[0])):
        if ((usedPins[1][i]=="OUTPUT" and usedPins[2][i]!=[]) or (usedPins[1][i]=="INPUT" and outPutOnly==False)):
            inoFile.write("\tpinMode("+str(usedPins[0][i])+", "+usedPins[1][i]+");\n")
    inoFile.write("}\n\n")
    for i in range(len(usedPins[0])):
        if usedPins[1][i]=="OUTPUT" and usedPins[2][i]!=[]:
            strings=OutputPinsHandling.createOutPutFunction(usedPins[0][i],usedPins[2][i])
            for i in strings:
                inoFile.write(i)
    inoFile.write("void loop()\n")
    inoFile.write("{\n")
    for i in range(len(usedPins[0])):
        if usedPins[1][i]=="OUTPUT" and usedPins[2][i]!=[]:
            inoFile.write("\tdigitalWrite("+str(usedPins[0][i])+",pin"+str(usedPins[0][i])+"Output(timemark));\n")
        else:
            if not outPutOnly:
                inoFile.write("\tSerial.write(digitalRead("+str(usedPins[0][i])+"));\n")
    if not inputOnly:
        inoFile.write("\ttimemark=millis();\n\n")#set this only if there is output
    inoFile.write("}\n")#set this only if there is output
                
    

    
