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

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda t=title, state=e1, var=e2, check=c, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalWrite(t, state, var, check, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addDigitalWrite(title, state, variable, check, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            logicalState = None

            if int(check.var.get()) > 0:
                logicalState = "HIGH"
            else:
                logicalState = "LOW"
            
            code = "digitalWrite(" + variable.get() + "," + logicalState + ");\n"
            dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"")))
            status_label.txtvar.set(title + " operation added.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")


def digitalRead(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLabel = Label(self.top, text="Set options for the selected operation", bg="gray")
    descriptionLabel.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Variable name of the digital PIN:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    label3 = Label(self.top, text="Variable name to store:", bg="gray")
    label3.grid(row=3, column=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")
    e3 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save pin",
                     command=lambda t=title, state=e1, var=e2, var2store=e3, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalRead(t, state, var, var2store, l, fm, dP, dS, dF))
    button1.grid(row=3, column=3)


def addDigitalRead(title, state, variable, var2store, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            code =  "digitalRead(" + variable.get() + ");\n"
            dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"")))
            status_label.txtvar.set(title + " operation added.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")

def analogWrite(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLabel = Label(self.top, text="Set options for the selected operation", bg="gray")
    descriptionLabel.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Variable name:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    label3 = Label(self.top, text="Value:", bg="gray")
    label3.grid(row=3, column=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")
    e3 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda t=title, state=e1, var=e2, val=e3, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addAnalogWrite(t, state, var, val, l, fm, dP, dS, dF))
    button1.grid(row=3, column=3)


def addAnalogWrite(title, state, variable, val, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        print dataPin
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            try:
                value = int(val.get())
                code =  "analogWrite(" + variable.get() + ", " + str(value) + ");\n"
                dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"")))
                status_label.txtvar.set(title + " operation added.")
            except ValueError:
                status_label.txtvar.set("Invalid value format.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")

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

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda t=title, state=e1, timeout=e2, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addWait(t, state, timeout, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addWait(title, state, timeout, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        try:
            delay = int(timeout.get())    
            code =  "delay(" + str(delay) + ");\n"
            dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"")))
            status_label.txtvar.set(title + " operation added.")
        except ValueError:
            status_label.txtvar.set("Invalid delay format.")
    else:
        status_label.txtvar.set("State not found.")

def tone(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLabel = Label(self.top, text="Set tone for the selected state", bg="gray")
    descriptionLabel.grid(row=0, sticky=W)

    label1 = Label(self.top, text="State name:", bg="gray")
    label1.grid(row=1, column=0, sticky=W)

    label2 = Label(self.top, text="Variable name:", bg="gray")
    label2.grid(row=2, column=0, sticky=W)

    label3 = Label(self.top, text='Frequency rate:', bg='gray' )
    label3.grid(row=3, column=0, sticky=W)

    label4 = Label(self.top, text='Duration:', bg='gray')
    label4.grid(row=4, column=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")
    e3 = Entry(self.top, highlightbackground="gray")
    e4 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=5, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda t=title, state=e1, var=e2, frq=e3, dur=e4, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addTone(t, state, var, frq, dur, l, fm, dP, dS, dF))
    button1.grid(row=4, column=3)

def addTone(title, state, variable, frq, dur, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            try:
                frequency = int(frq.get())
                duration = int(dur.get())
                code = "tone(" + variable.get() + ", " + str(frequency) + ", " + str(duration) + ");\n"
                dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"")))
                status_label.txtvar.set(title + " operation added.")
            except ValueError:
                status_label.txtvar.set("Invalid value format.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")

opList = ["Digital write", "Analog write", "Digital read", "Wait", "Tone"]

opFunc = {"Digital write": digitalWrite, "Analog write": analogWrite, "Digital read": digitalRead, "Wait": wait, "Tone": tone}

portList = ["A0", "A1","A2", "A3", "A4", "A5", "D0", "D1","D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9" ,"D10" ,"D11" ,"D12", "D13"]