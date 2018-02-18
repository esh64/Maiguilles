import os
import ConfigProgramFile

def createMakefileFile():
    values=ConfigProgramFile.getFileConfigs()
    if values!=[]:
        makefileFile=open('makefile', 'w')
        makefileFile.write('BOARD_TAG = '+values[0]+'\n')
	if not os.path.isfile(values[1]+'/Arduino.mk'):
		return 1
        makefileFile.write('include '+values[1]+'/Arduino.mk\n')
        makefileFile.close()
        os.popen("mv makefile temporary")
        os.chdir("temporary")
	return 0
    return 2
