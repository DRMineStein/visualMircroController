from Tkinter import *
import tkFileDialog
import pickle
import datetime
import ViewsMenuFunction

def newProject(self, view_list, dataPin, dataStates, dataFlow):
    print(dataPin, dataStates, dataFlow)
    self.dataPin.clear()
    self.dataStates.clear()
    self.dataFlow.clear()
    while len(view_list) != 0:
        view_list.pop().destroy()

    ViewsMenuFunction.updateCurrentView(self, view_list, dataPin, dataStates, dataFlow)


def saveProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster):
    if hasattr(self, 'filename'):
        data2store = (dataPin, dataStates, dataFlow)
        storefile = open(self.filename, 'wb')
        pickle.dump(data2store, storefile)
        storefile.close()
    else:
        saveAsProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster)

def saveAsProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster):
    data2store = (dataPin, dataStates, dataFlow)
    filename = tkFileDialog.asksaveasfilename(parent=frameMaster, filetypes=(("Project file", "*.proj"),))
    storefile = open(filename + '.proj', 'wb')
    pickle.dump(data2store, storefile)
    storefile.close()

def openProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster):



    self.filename = tkFileDialog.askopenfilename(parent=frameMaster, filetypes=(("Project file", "*.proj"),))

    loadfile = open(self.filename, 'rb')
    data2load = pickle.load(loadfile)
    loadfile.close()
   
    dataPin.clear()
    dataStates.clear()
    dataFlow.clear()

    dataPin.update(data2load[0])
    dataStates.update(data2load[1])
    dataFlow.update(data2load[2])

    ViewsMenuFunction.updateCurrentView(self, view_list, dataPin, dataStates, dataFlow)

