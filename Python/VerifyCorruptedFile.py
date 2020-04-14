
#this functions verifies if the openend file is not supported by the program
#return true if the file is corrupted/not suitable return false if the file is readable by the program
def fileCorrupted(filename, usedPins):
    if filename[-5:]!=".uiui":
        print("extension")
        return True
    if len(usedPins)!=3:
        print("usedPins format")
        return True
    for i in usedPins[1]:
        if i not in ["INPUT", "OUTPUT"]:
            print("Other than INPUT/OUTPUT")
            return True
    pins=range(2,15)
    for i in usedPins[0]:
        if int(i) not in pins:
            print("invalid pin numbers")
            return True
        pins.remove(int(i))
    for i in usedPins[2]:
        if i==[]:
            break
        lista=filter(lambda a: a!=0, i)
        lista=filter(lambda a: a!=1, lista)
        if lista!=[]:
            print("invalid graph value")
            return True
    return False
        
        
