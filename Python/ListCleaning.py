#this function receive a list with \x00 \x01 wich represents the waveform of a long serial transmission
#this funcion discarts the useless part of the given waveform list and return the period  and the startBit
#this function does not check if the given list has only \x00 or \x01
def clearList(orignalWaveList):
    nonSignal=orignalWaveList[0]
    if nonSignal=='\x00':
        startBit='\x01'
    else:
        startBit='\x00'
    if startBit not in orignalWaveList:#put some kind of error here
        return [], 0, nonSignal
    startAt=orignalWaveList.index(startBit)#get the first position of the useful data
    if nonSignal not in orignalWaveList[startAt:]:#put some kind of error here too
        return orignalWaveList,0, nonSignal
    temporaryPosition=orignalWaveList[startAt:].index(nonSignal)#get the first risedge
    period=temporaryPosition
    useFullList=orignalWaveList[startAt+temporaryPosition:]
    invertedList=useFullList[::-1]
    if startBit not in invertedList:
        return orignalWaveList[startAt-1:temporaryPosition+startAt]+[nonSignal]*period,period, startBit
    lastUsefullPosition=invertedList.index(startBit)#get the last position where startBit appears
    if lastUsefullPosition!=0:
        useFullList=useFullList[:-1*(lastUsefullPosition)]#make the useful list
    temporaryList=useFullList[:]
    while(startBit in temporaryList):
        position1=temporaryList.index(startBit)
        if nonSignal not in temporaryList[position1:]:
            break
        temporaryPeriod=temporaryList[position1:].index(nonSignal)
        if temporaryPeriod<period:
            period=temporaryPeriod
        temporaryList=temporaryList[temporaryPeriod:]
    return orignalWaveList[startAt-1:temporaryPosition+startAt]+useFullList+[nonSignal]*period, period, startBit

#this function receives a list with \x00 and \x01 and convert to a list with 0 and 1
#does not check if the list contais only \x00 or \x01
def convertList(lista):
    if ('\x00' not in lista):
        return []
    if ('\x01' not in lista):
        return []
    lista2=[]
    for i in lista:
        if (i=='\x00'):
            lista2+=[0]
        else:
            lista2+=[1]
    return lista2
    
    
