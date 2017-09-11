from Tkinter import *

def digitalWrite(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLabel = Label(self.top, text="Set options for the write operation", bg="gray")
    descriptionLabel.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Variable name:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="HIGH if enabled, LOW otherwise", variable=var, bg="gray")
    c.var = var
    c.grid(row=2, column=2, sticky=W)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save pin",
                     command=lambda t=title, state=e1, var=e2, check=c, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalWrite(t, state, var, check, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addDigitalWrite(title, state, variable, check, status_label, frameMaster, dataPin, dataStates, dataFlow):
    for key in dataStates.keys():
        if state.get() != key:
            status_label.txtvar.set("State not found.")
            return
        else:
            break

    for key in dataPin.keys():
        if variable.get() != dataPin[key][0]:
            status_label.txtvar.set("Variable name not found.")
            return
        else:
            break

    logicalState = None
    if int(check.var.get()) > 0:
        logicalState = "HIGH"
    else:
        logicalState = "LOW"
    code =  "digitalWrite(" + variable.get() + "," + logicalState + ");\n"
    dataFlow[state.get()] = (code, state.get()+"_"+title.replace(' ',""), 'exit')
    status_label.txtvar.set(title + " operation added.")

def digitalRead(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    pass


def wait(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLabel = Label(self.top, text="Set options for the write operation", bg="gray")
    descriptionLabel.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Timeout:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save pin",
                     command=lambda t=title, state=e1, timeout=e2, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addWait(t, state, timeout, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addWait(title, state, timeout, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        try:
            delay = int(timeout.get())    
            code =  "delay(" + str(delay) + ");\n"
            dataFlow[state.get()] = (code, state.get()+"_"+title.replace(' ',""), 'exit')
            status_label.txtvar.set(title + " operation added.")
        except ValueError:
            status_label.txtvar.set("Invalid delay format.")
    else:
        status_label.txtvar.set("State not found.") 

opList = ["Digital write", "Digital read", "Wait"]

opFunc = {"Digital write": digitalWrite, "Digital read": digitalRead, "Wait": wait}

portList = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9" ,"D10" ,"D11" ,"D12", "D13"]