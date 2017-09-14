from Tkinter import *
import tkFileDialog
import pickle
import datetime
import ViewsMenuFunction

def newProject(self, view_list, dataPin, dataStates, dataFlow):
    print(dataPin, dataStates, dataFlow)
    dataPin = {}
    dataStates = {}
    dataFlow = {}
    while len(view_list) != 0:
        view_list.pop().destroy()

def saveProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster):

    data2store = (dataPin, dataStates, dataFlow)
    filename = tkFileDialog.asksaveasfilename(parent=frameMaster, filetypes=(("Pickle", "*.pickle"),))
    storefile = open(filename + '.pickle', 'wb')
    pickle.dump(data2store, storefile)
    storefile.close()

def saveAsProject(self, view_list, dataPin, dataStates, dataFlow):
	pass

def openProject(self, view_list, dataPin, dataStates, dataFlow, frameMaster):

    filename = tkFileDialog.askopenfilename(parent=frameMaster, filetypes=(("Pickle", "*.pickle"),))

    loadfile = open(filename, 'rb')
    data2load = pickle.load(loadfile)
    loadfile.close()
   
    dataPin.clear()
    dataStates.clear()
    dataFlow.clear()

    dataPin.update(data2load[0])
    dataStates.update(data2load[1])
    dataFlow.update(data2load[2])

    ViewsMenuFunction.gotoBoardView(self, view_list, dataPin, dataStates, dataFlow)

