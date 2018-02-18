#this function receives an graph list and return when changes happens
def outPutSequenceMaker(lista):
    transintionsSpot=[(lista[0],0)]
    actualValue=1
    nextValue=0
    if lista[0]==0:
        actualValue=0
        nextValue=1
    counter=1
    for i in lista[1:]:
        if i==nextValue:
            #nextValue,actualValue=nextValue,actualValue
            transintionsSpot+=[(nextValue,counter)]
            temp=actualValue
            actualValue=nextValue
            nextValue=temp
        counter+=1
    return transintionsSpot

def createOutPutFunction(pinNumber, lista):
    transintionsSpot=outPutSequenceMaker(lista)
    strings=["unsigned short pin"+str(pinNumber)+"Output(unsigned long long timemark)\n","{\n","\tunsigned long long timemarkTemp=timemark%"+str(len(lista))+";\n"]
    for i in range(len(transintionsSpot)-1):
        #if i!=0:
            #elseMarke=('\t'*(i+1))+"else "
        #else:
            #elseMarke='\t'
        strings+=["\tif(timemarkTemp<"+str(transintionsSpot[i+1][1])+")return "+str(transintionsSpot[i][0])+";\n"]
    strings+=["\treturn "+str(transintionsSpot[-1][0])+";\n}\n\n"]
    return strings

#this function receives an graph list and return the list compacted
#TODO try to make this more eficient using index function
def listCampacter(lista):
    transintionsSpot=[]
    actualValue=1
    nextValue=0
    if lista[0]==0:
        actualValue=0
        nextValue=1
    counter=1
    for i in lista[1:]:
        if i==actualValue:
            counter+=1
        else:
            transintionsSpot+=[(actualValue,counter)]
            temp=actualValue
            actualValue=nextValue
            nextValue=temp
            counter=1
    return transintionsSpot+[(actualValue,counter)]
    
        
