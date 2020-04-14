import os
from PyQt4 import QtGui

class aboutProgram(QtGui.QDialog):
    
    def __init__(self):
        super(aboutProgram, self).__init__()
        self.initUI()
        
    def initUI(self):
        vbox=QtGui.QVBoxLayout()
        picture=QtGui.QLabel()
        picture.setPixmap(QtGui.QPixmap(os.getcwd() + "/Maiguilles.png"))
        vbox.addWidget(picture)
        tabs= QtGui.QTabWidget()
        vbox.addWidget(tabs)
        self.aboutProgram= QtGui.QWidget()
        self.aboutProgramUI()
        self.librariesAndDependencies= QtGui.QWidget()
        self.librariesAndDependenciesUI()
        self.aboutAutors= QtGui.QWidget()
        self.aboutAutorsUI()
        tabs.addTab(self.aboutProgram,"About Program")
        tabs.addTab(self.librariesAndDependencies,"Libraries and Dependencies")
        tabs.addTab(self.aboutAutors,"Authors")
        self.setLayout(vbox)
        self.setWindowTitle('About Maiguilles')
        self.setWindowIcon(QtGui.QIcon("Maiguilles.png"))
        
    def aboutProgramUI(self):
        vbox=QtGui.QVBoxLayout()
        name=QtGui.QLabel("Maiguilles")
        version=QtGui.QLabel("Version: 1.0")
        descripition=QtGui.QLabel("Program to create graphs from arduino inputs and generate output functions to arduino")
        reason=QtGui.QLabel("I made this as a tool for another project")
        license=QtGui.QLabel("GNU bla bla")
        link1=QtGui.QLabel("<a href='https://github.com/esh64/Maiguilles'>Github page</a>")
        link1.setOpenExternalLinks(True)
        vbox.addWidget(name)
        vbox.addWidget(version)
        vbox.addWidget(descripition)
        vbox.addWidget(reason)
        vbox.addWidget(link1)
        self.aboutProgram.setLayout(vbox)
    
    def librariesAndDependenciesUI(self):
        vbox=QtGui.QVBoxLayout()
        lista=[]
        lista+=[QtGui.QLabel("<a href='https://www.python.org/'>Written in Python 2.7</a>")]
        lista+=[QtGui.QLabel("<a href='https://wiki.python.org/moin/PyQt4'>With PyQt4 GUI toolkit</a>")]
        lista+=[QtGui.QLabel("<a href='https://pythonhosted.org/pyserial/'>With pySerial module</a>")]
        lista+=[QtGui.QLabel("<a href='https://www.arduino.cc/en/main/software'>Needs Arduino IDE</a>")]
        lista+=[QtGui.QLabel("<a href='https://github.com/sudar/Arduino-Makefile'>Needs Arduino Makefile(Linux only)</a>")]
        lista+=[QtGui.QLabel("<a href='http://www.pyinstaller.org/'>Executables made with PyInstaller</a>")]
        for i in lista:
            i.setOpenExternalLinks(True)
            vbox.addWidget(i)
        self.librariesAndDependencies.setLayout(vbox)
    
    def aboutAutorsUI(self):
        vbox=QtGui.QVBoxLayout()
        lista=[]
        lista+=[QtGui.QLabel("esh")]
        lista+=[QtGui.QLabel("<a href='https://github.com/esh64/'>My github</a>")]
        lista[-1].setOpenExternalLinks(True)
        for i in lista:
            vbox.addWidget(i)
        self.aboutAutors.setLayout(vbox)
        
        
        
        
