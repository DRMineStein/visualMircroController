from Tkinter import *
import pickle
import datetime

def newProject(self, view_list, dataPin, dataStates, dataFlow):
    print(dataPin, dataStates, dataFlow)
    dataPin = {}
    dataStates = {}
    dataFlow = {}
    while len(view_list) != 0:
        view_list.pop().destroy()

def saveProject(self, view_list, dataPin, dataStates, dataFlow):
	data2store = (dataPin, dataStates, dataFlow)
	storefile = open('test.pickle', 'wb')
	pickle.dump(data2store, storefile)
	storefile.close()

def saveAsProject():
	pass

def openProject(self, dataPin, dataStates, dataFlow):
   print(dataPin)
   loadfile = open('test.pickle', 'rb')
   data2load = pickle.load(loadfile)
   loadfile.close()
   
   dataPin = data2load[0]
   dataStates = data2load[1]
   dataFlow = data2load[2]

   return dataPin, dataStates, dataFlow 


