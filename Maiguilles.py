#!/usr/bin/env python

import sys
import os
import pickle
import MainFrame
import MakeInofile
import ConfigGraph
import VerifyCorruptedFile
import ConfigProgram
import platform
import webbrowser
import AboutProgram

openErrorValue=0
try:
    from PyQt4 import QtGui
except:
    try:
        import pip
        pip.main(['install', "python-qt4"])
        from PyQt4 import QtGui
    except:
        openErrorValue=1


if openErrorValue==0:
    try:
        import serial
    except:
        try:
            import pip
            pip.main(['install', 'pyserial'])
            import serial
        except:
            openErrorValue=2   
        

class mainProgram(QtGui.QMainWindow):
    
    def __init__(self, app):
        super(mainProgram, self).__init__()
        self.app=app
        self.filename="untitled.uiui"
        self.platform=platform.system()
        self.initUI()
       
        
    def initUI(self):
        self.frame = MainFrame.mainFrame(self, self.platform)
        self.frame.checkUsedPins()
        self.savedFrame=self.frame.usedPins[:]
        self.setCentralWidget(self.frame)
        self.statusLabel=QtGui.QLabel('Status')
        self.statusBar().addWidget(self.statusLabel)
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        #filemenu itens
        newProjectAction = QtGui.QAction("New", self)
        newProjectAction.setShortcut('Ctrl+N')
        newProjectAction.setStatusTip('New project')
        newProjectAction.triggered.connect(self.newProject)
        fileMenu.addAction(newProjectAction)
        
        openProjectAction = QtGui.QAction("Open", self)
        openProjectAction.setShortcut('Ctrl+O')
        openProjectAction.setStatusTip('Open project')
        openProjectAction.triggered.connect(self.openProject)
        fileMenu.addAction(openProjectAction)
        
        saveProjectAction = QtGui.QAction("Save", self)
        saveProjectAction.setShortcut('Ctrl+S')
        saveProjectAction.setStatusTip('Save project')
        saveProjectAction.triggered.connect(self.saveProject)
        fileMenu.addAction(saveProjectAction)
        
        saveAsProjectAction = QtGui.QAction("Save as", self)
        saveAsProjectAction.setShortcut('Ctrl+Shift+S')
        saveAsProjectAction.setStatusTip('Save project as')
        saveAsProjectAction.triggered.connect(self.saveAsProject)
        fileMenu.addAction(saveAsProjectAction)
        
        exportInoAction = QtGui.QAction("Export", self)
        exportInoAction.setShortcut('Ctrl+E')
        exportInoAction.setStatusTip('Export the project as the ino file')
        exportInoAction.triggered.connect(self.exportFileIno)
        fileMenu.addAction(exportInoAction)
        
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        #file menu itens end
        
        settingsMenu = menubar.addMenu('&Config')
        #config menu itens
        
        graphConfigAction = QtGui.QAction('Configure Graphics', self)
        graphConfigAction.setStatusTip('Configure graphics colors, fonts and size')
        self.graphConfigWindows=ConfigGraph.configGraph(self.frame)
        graphConfigAction.triggered.connect(lambda: self.graphConfigWindows.exec_())
        settingsMenu.addAction(graphConfigAction)
        
        ProgramConfigAction = QtGui.QAction('Configure Program', self)
        ProgramConfigAction.setStatusTip('Configure arduino info, serial connection and etc')
        self.programConfigWindows=ConfigProgram.configProgram(self)
        ProgramConfigAction.triggered.connect(lambda: self.programConfigWindows.exec_())
        settingsMenu.addAction(ProgramConfigAction)
        
        #config menu itens end
        helpMenu = menubar.addMenu('&Help')
        #help menu itens
        
        aboutAction = QtGui.QAction('About Maiguilles', self)
        aboutAction.setStatusTip('Program information')
        about=AboutProgram.aboutProgram()
        aboutAction.triggered.connect(lambda: about.exec_())
        helpMenu.addAction(aboutAction)
        
        aboutAction = QtGui.QAction('Maiguilles Handbook', self)
        aboutAction.setShortcut('F1')
        aboutAction.setStatusTip('Program manual')
        aboutAction.triggered.connect(lambda: webbrowser.open('https://github.com/esh64/Maiguilles/wiki'))
        helpMenu.addAction(aboutAction)
        
        reportBugAction = QtGui.QAction('Report Bug', self)
        reportBugAction.setStatusTip('Report Bug')
        reportBugAction.triggered.connect(lambda: webbrowser.open('https://github.com/esh64/Maiguilles/issues'))
        helpMenu.addAction(reportBugAction)
        
        contributeAction = QtGui.QAction('Contribute', self)
        contributeAction.setStatusTip('Improve, share, donate')
        contributeAction.triggered.connect(lambda: webbrowser.open('https://github.com/esh64/Maiguilles/pulls'))
        helpMenu.addAction(contributeAction)
        #help menu itens end

        self.setGeometry(300, 150, 900, 600)
        self.setWindowTitle('Maiguilles')
        self.setWindowIcon(QtGui.QIcon("Maiguilles.png"))
        self.show()
        if not (os.path.isfile('./configProgramFile')):
            self.statusLabel.setText("Config Program file not found")
            self.programConfigWindows.exec_()
    
    def closeEvent(self, event):
        self.frame.checkUsedPins()
        if self.savedFrame!=self.frame.usedPins:
            quitMensage= "Are you sure you want to exit the program withouth saving the "+self.filename+"?"
            reply = QtGui.QMessageBox.question(self, 'Message', quitMensage, QtGui.QMessageBox.Save, QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Save:
                self.saveProject()
                event.accept()
            if reply == QtGui.QMessageBox.Discard:
                event.accept()
            if reply == QtGui.QMessageBox.Cancel:
                event.ignore()
        else:
            event.accept()
    
    def newProject(self):
        self.frame.checkUsedPins()
        if self.savedFrame!=self.frame.usedPins:
            newProjectMensage= "The "+self.filename+" file have been modified. Do you want to save?"
            reply = QtGui.QMessageBox.question(self, 'Message', newProjectMensage, QtGui.QMessageBox.Save, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Save:
                self.saveProject()
            if reply == QtGui.QMessageBox.Cancel:
                return
        for i in self.frame.graphList:
            i.removeWidgetAction()
        self.frame.deleteLater()
        self.frame=None
        self.frame = MainFrame.mainFrame(self, self.platform)
        self.setCentralWidget(self.frame)
        self.filename="untitled.uiui"
    
    def openProject(self):
        self.frame.checkUsedPins()
        if self.savedFrame!=self.frame.usedPins:
            newProjectMensage= "The "+self.filename+" file have been modified. Do you want to save?"
            reply = QtGui.QMessageBox.question(self, 'Message', newProjectMensage, QtGui.QMessageBox.Save, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Save:
                self.saveProject()
            if reply == QtGui.QMessageBox.Cancel:
                return
        openFileDialog=QtGui.QFileDialog()
        filename = openFileDialog.getOpenFileNameAndFilter(self, 'Open Project', '','*.uiui')[0]
        if filename=='':
            return
        file1=open(filename, "r")
        try:
            usedPins=pickle.load(file1)
        except:
            QtGui.QMessageBox.question(self, 'Alert', "Invalid file", QtGui.QMessageBox.Ok)
            return
        if VerifyCorruptedFile.fileCorrupted(filename, usedPins):
            QtGui.QMessageBox.question(self, 'Alert', "Corrupted File", QtGui.QMessageBox.Ok)
            return
        self.filename=filename
        for i in self.frame.graphList:
            i.removeWidgetAction()
        self.frame.deleteLater()
        self.frame=None
        self.frame = MainFrame.mainFrame(self, self.platform)
        self.setCentralWidget(self.frame)
        self.frame.graphList[0].removeWidgetAction()
        for i in range(len(usedPins[0])):
            self.frame.addWidgetAction()
            pos=self.frame.graphList[-1].pinNumberList.index(usedPins[0][i])
            self.frame.graphList[-1].pinNumber.setCurrentIndex(pos)
            for j in usedPins[0]:
                if j==usedPins[0][i] or j not in self.frame.graphList[-1].pinNumberList:
                    continue
                pos2=self.frame.graphList[-1].pinNumberList.index(j)
                self.frame.graphList[-1].pinNumber.removeItem(pos2)
                self.frame.graphList[-1].pinNumberList.remove(j)
            self.frame.graphList[-1].pinMode.setCurrentIndex(["INPUT","OUTPUT"].index(usedPins[1][i]))
            if usedPins[1][i]=="OUTPUT":
                self.frame.graphList[-1].expandGraphButton.show()
                self.frame.graphList[-1].reduceGraphButton.show()
                self.frame.graphList[-1].graph.setGraphStatus(usedPins[1][i])
            self.frame.graphList[-1].graph.setLista(usedPins[2][i])
            self.frame.graphList[-1].graph.repaint()
        self.frame.checkUsedPins()
        self.savedFrame=self.frame.usedPins[:]
            
        
    def exportFileIno(self):
        saveFileDialog=QtGui.QFileDialog()
        filename = saveFileDialog.getSaveFileNameAndFilter(self, 'Save File', '', '*.ino')[0]
        if filename[-4:]!=".ino":
            filename+=".ino"
        self.frame.checkUsedPins()
        MakeInofile.makeInoFile(self.frame.usedPins, 9600, filename, True)
        
    def saveProject(self):
        if self.filename=="untitled.uiui":
            saveFileDialog=QtGui.QFileDialog()
            self.filename = saveFileDialog.getSaveFileNameAndFilter(self, 'Save Project', '', '*.uiui')[0]
            if self.filename=="":
                self.filename="untitled.uiui"
                return
            if self.filename[-5:]!=".uiui":
                self.filename+=".uiui"
        self.frame.checkUsedPins()
        pickle.dump(self.frame.usedPins, open(self.filename, "wb"))
        self.savedFrame=self.frame.usedPins[:]
    
    def saveAsProject(self):
        saveFileDialog=QtGui.QFileDialog()
        filename = saveFileDialog.getSaveFileName(self, 'Save Project')
        if filename=="":
            return
        if filename[-5:]!=".uiui":
            filename+=".uiui"
        self.frame.checkUsedPins()
        pickle.dump(self.frame.usedPins, open(filename, "wb"))
        if filename==self.filename:
            self.savedFrame=self.frame.usedPins[:]
            
        
def main():
    if openErrorValue==0:
            app = QtGui.QApplication(sys.argv)
            mainProgram(app)
            sys.exit(app.exec_())
    else:
        platformUsing=platform.system()
        import commands
        if openErrorValue==1:
            if platformUsing=="Linux":
                status=commands.getstatusoutput("notify-send \"PyQt4 is not installed\"")[0]
                if status!=0:
                    commands.getstatusoutput("zenity --error --text=\"PyQt4 is not installed\!\" --title=\"Dependencie not installed\"")
            else:
                os.popen("cscript FailedImportModuleWindowsDialog.vbs \"PyQt4 is not installed\"")
        else:
            if platformUsing=="Linux":
                status=commands.getstatusoutput("notify-send \"pySerial is not installed\"")[0]
                if status!=0:
                    commands.getstatusoutput("zenity --error --text=\"pySerial is not installed\!\" --title=\"Dependencie not installed\"")
            else:
                os.popen("cscript FailedImportModuleWindowsDialog.vbs \"pySerial is not installed\"")
                
                
if __name__ == '__main__':
    main()    
