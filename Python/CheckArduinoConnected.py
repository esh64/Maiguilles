import os

#this function check the /dev/ directory to find if  there is any arduino connected(ttyACM or ttyUSB)
#return the port if found, return nothing if there is no arduino connected
#TODO figure out someway to let the user choice if there is more than one arduino connected
def checkArduinoConected(platform):
    if platform=="Linux":
        files=os.listdir("/dev")
        usbList=(os.popen("lsusb")).read()
        if "Arduino" not in usbList:
            return ''
        pos1=usbList.index("Arduino")
        pos2=usbList[pos1:].index("\n")
        if "ACM" in usbList[pos1:pos2+pos1]:
            ttyType="ACM"
        else:
            if "USB" in usbList[pos1:pos2+pos1]:
                ttyType="USB"
            else:
                return ''
        for i in files:
            #TODO find a way to know if this is really Arduino
            if (("tty"+ttyType) in i):
                return i
        return ''
    if platform=="Windows":
        serialPorts=os.popen("mode").read()
        if "COM" in serialPorts:
            comFirstPosition=serialPorts.index("COM")
            return serialPorts[comFirstPosition:comFirstPosition+4]#len of COM plus the number of the COM port
        return ''
    else:
        print("Not working with mac yet")
    



