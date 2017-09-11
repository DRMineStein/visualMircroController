from Tkinter import *
import graphVizGenerator as gv
import utils

def getStateOperation(self, title, figFrame, width, height, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please select the state to configure", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    label0 = Label(self.top, text="State name:", bg="gray")
    label0.grid(row=1, sticky=W)

    e0 = Entry(self.top, highlightbackground="gray")

    e0.grid(row=1, column=1)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=2, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Retrieve state",
                     command=lambda s=self, t=e0, l=statusLable, fm=figFrame,
                                    dP=dataPin, dS=dataStates, dF=dataFlow, w=width, h=height:
                     retriveStateFlow(s, t, l, fm, dP, dS, dF, w, h))
    button1.grid(row=1, column=2)


def retriveStateFlow(self, title, statusLable, figFrame, dataPin, dataStates, dataFlow, w, h):
    readyToPlot = True
    print title.get()
    if len(title.get()) == 0 or ',' in title.get():
        title.delete(0, END)
        statusLable.txtvar.set("You have to select exactly one state.")
        readyToPlot = False
    if title.get() not in list(dataStates.keys()):
        statusLable.txtvar.set("The state selected doesn't exists.")
        readyToPlot = False

    if readyToPlot:
        statusLable.txtvar.set("State found.")
        gv.generateFlow(title.get(),dataFlow, w, h)
        utils.add_picture(self, figFrame, "empty", w*2, h*2, False)
        utils.add_picture(self, figFrame, title.get()+'_flow', w, h, False)

