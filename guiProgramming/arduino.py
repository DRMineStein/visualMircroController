from Tkinter import *

def digitalWrite(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Set options for the selected operation", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Variable name:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    e1 = Entry(self.top)
    e2 = Entry(self.top)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="HIGH if enabled, LOW otherwise", variable=var, bg="gray")
    c.var = var
    c.grid(row=2, column=2, sticky=W)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", text="Save pin",
                     command=lambda t=title, state=e1, var=e2, check=c, l=statusLable, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalWrite(t, state, var, check, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)


def addDigitalWrite(title, state, variable, check, status_label, frameMaster, dataPin, dataStates, dataFlow):
    setOperation = True
    print "Variable"
    print variable.get()
    print "State"
    print state.get()
    print dataStates
    for key in dataStates.keys():
        if state.get() != key:
            setOperation = False
            status_label.txtvar.set("State not found.")
            # state.delete(0, END)
        else:
            setOperation = True
            break

    for key in dataPin.keys():
        if variable.get() != dataPin[key][0]:
            setOperation = False
            status_label.txtvar.set("Variable name not found.")
            # variable.delete(0, END)
        else:
            setOperation = True
            break

    if setOperation:
        logicalState = None
        if int(check.var.get()) > 0:
            logicalState = "HIGH"
        else:
            logicalState = "LOW"
        code =  "digitalWrite(" + variable.get() + "," + logicalState + ");\n"
        dataFlow[state.get()] = (code, state.get()+"_"+title.replace(' ',""), 'exit')
        status_label.txtvar.set(title + " operation added.")

    print dataFlow

def digitalRead(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    pass


def wait(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    pass


opList = ["Digital write", "Digital read", "Wait"]

opFunc = {"Digital write": digitalWrite, "Digital read": digitalRead, "Wait":wait}

portList = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9" ,"D10" ,"D11" ,"D12", "D13"]