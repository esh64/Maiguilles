import os
import platform

#this function create the configFile
def writeConfigFile(board="uno", location1="/"):
    configFile=open('configProgramFile', 'w')
    configFile.write('board='+board+'\n')
    configFile.write('location1='+location1+'\n')
    configFile.close()

#this function check if the configFile existis, if not, call writeConfigFile with default values
#if configFile existis return all the values in a list
def getFileConfigs():
    if (os.path.isfile('./configProgramFile')):
        configFile=open('configProgramFile', 'r')
        lines=configFile.readlines()
        values=[]
        platformUsing=platform.system()
        if lines[0][6:-1] not in ["uno", "due", "mega", "nano", "yun", "leonardo", "lillypad", "esplora", "micro", "ethernet", "fio"]:
            print("Invalid board or non support board")
            return corruptedFileTreatment(platformUsing, configFile)
        values+=[lines[0][6:-1]]
        if not os.path.isdir(lines[1][10:-1]):
            print("Invalid directory")
            return corruptedFileTreatment(platformUsing, configFile)
        values+=[lines[1][10:-1]]
        configFile.close()
        return values
    return ['uno', os.getcwd()]

def corruptedFileTreatment(platformUsing, configFile):
    if platformUsing=="Linux":
        os.popen("cp configProgramFile configProgramFileCorrupted")
    if platformUsing=="Windows":
        os.popen("move configProgramFile configProgramFileCorrupted")
    configFile.close()
    os.remove("configProgramFile")
    return ['uno', os.getcwd()]
            
            
        
    
