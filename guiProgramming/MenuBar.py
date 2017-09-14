from Tkinter import *
import fileMenuFunction
import ViewsMenuFunction
import codeGenerator


def setupMenu(self, view_list, dataPin, dataStates, dataFlow):
    # File cascade menu option
    menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label="File", menu=menu)
    menu.add_command(label="New", command=lambda:fileMenuFunction.newProject(self,view_list, dataPin, dataFlow, dataStates))
    menu.add_command(label="Open", command=lambda:fileMenuFunction.openProject(self, view_list, dataPin, dataFlow, dataStates, self.master))
    menu.add_command(label="Save", command=lambda:fileMenuFunction.saveProject(self,view_list, dataPin, dataFlow, dataStates, self.master))
    menu.add_command(label="Save as..", command=lambda:fileMenuFunction.saveAsProject(self,view_list, dataPin, dataFlow, dataStates))
    menu.add_command(label="Generate code", command=lambda:codeGenerator.generateCode(dataPin,dataStates, dataFlow))

    # # Edit cascade menu option
    # menu = Menu(self.menubar, tearoff=0)
    # self.menubar.add_cascade(label="Edit", menu=menu)
    # menu.add_command(label="Cut",)
    # menu.add_command(label="Copy")
    # menu.add_command(label="Paste")

    # View cascade menu option
    menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label="Views", menu=menu)
    menu.add_command(label="Board", command=lambda:ViewsMenuFunction.gotoBoardView(self, view_list, dataPin, dataStates, dataFlow))
    menu.add_command(label="State transition builder", command=lambda:ViewsMenuFunction.gotoStateView(self, view_list, dataPin, dataStates, dataFlow))
    menu.add_command(label="Design flow", command=lambda:ViewsMenuFunction.gotoDesignView(self, view_list, dataPin, dataStates, dataFlow))

    # Connection cascade menu option
    connectionMenu = Menu(self.menubar, tearoff=0)
    serialMenu = Menu(self.menubar)

    self.menubar.add_cascade(label="Connections", menu=connectionMenu)
    connectionMenu.add_cascade(label="Serial", menu=serialMenu)
    for name in ("Set Data Transmissionrate", ""):
        serialMenu.add_command(label=name)
