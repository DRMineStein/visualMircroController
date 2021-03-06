from Tkinter import *
import portConfigurator as pc

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

    state = StringVar(self.top)
    stateStr = "State"
    try:
        state.set(list(dataStates.keys())[0])
        o1 = OptionMenu(self.top, state, *list(dataStates.keys()))
    except IndexError:
        o1 = OptionMenu(self.top, stateStr, "", "")

    pin = StringVar(self.top)
    pinStr = "Variable"
    variables = []
    for d in list(dataPin.keys()):
        variables.append(dataPin[d][0])
    try:
        pin.set(variables[0])
        o2 = OptionMenu(self.top, pin, *variables)
    except IndexError:
        o2 = OptionMenu(self.top, pinStr, "", "")

    o1.config(highlightbackground='gray', bg='gray')
    o2.config(highlightbackground='gray', bg='gray')

    o1.grid(row=1, column=1)
    o2.grid(row=2, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="HIGH if enabled, LOW otherwise", variable=var, bg="gray")
    c.var = var
    c.grid(row=2, column=2, sticky=W)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda s=self, t=title, state=state, var=pin, check=c, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalWrite(s, t, state, var, check, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addDigitalWrite(self, title, state, variable, check, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            logicalState = None

            if int(check.var.get()) > 0:
                logicalState = "HIGH"
            else:
                logicalState = "LOW"
            
            code = "digitalWrite(" + variable.get() + "," + logicalState + ");\n"
            updateCode(state, code, title, dataFlow)
            status_label.txtvar.set(title + " operation added.")
            self.top.destroy()
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

    state = StringVar(self.top)
    stateStr = "State"
    try:
        state.set(list(dataStates.keys())[0])
        o1 = OptionMenu(self.top, state, *list(dataStates.keys()))
    except IndexError:
        o1 = OptionMenu(self.top, stateStr, "", "")

    pin = StringVar(self.top)
    pinStr = "Variable"
    variables = []
    for d in list(dataPin.keys()):
        variables.append(dataPin[d][0])
    try:
        pin.set(variables[0])
        o2 = OptionMenu(self.top, pin, *variables)
    except IndexError:
        o2 = OptionMenu(self.top, pinStr, "", "")

    o1.config(highlightbackground='gray', bg='gray')
    o2.config(highlightbackground='gray', bg='gray')

    o1.grid(row=1, column=1)
    o2.grid(row=2, column=1)

    var2store = StringVar(self.top)
    var2storeStr = "Variable"
    variables2 = []
    for d in list(dataPin.keys()):
        variables2.append(dataPin[d][0])
    variables2.append("Add new Variable")
    try:
        pin.set(variables[0])
        o3 = OptionMenu(self.top, var2store, *variables2)
    except IndexError:
        o3 = OptionMenu(self.top, var2storeStr, "", "")

    o3.config(highlightbackground="gray", bg='gray', width=10)

    o3.grid(row=3, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save Operation",
                     command=lambda s=self, t=title, state=state, var=pin, var2store=var2store, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addDigitalRead(s, t, state, var, var2store, l, fm, dP, dS, dF))
    button1.grid(row=3, column=3)


def addDigitalRead(self, title, state, variable, var2store, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            if var2store.get() is not " ":
                self.top.destroy()

                name = var2store.get()

                if name == "Add new Variable":
                    name = "V" + str(len(dataPin))
                    pc.setPort(self, name, [], frameMaster, dataPin, dataStates, dataFlow)

                    name = "##" + name + "##"
                print name
                code = name + " = digitalRead(" + variable.get() + ");\n"
                updateCode(state, code, title, dataFlow)
                status_label.txtvar.set(title + " operation added.")
                self.top.destroy()
            else:
                status_label.txtvar.set("Variable name for storing not found.")
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

    state = StringVar(self.top)
    stateStr = "State"
    try:
        state.set(list(dataStates.keys())[0])
        o1 = OptionMenu(self.top, state, *list(dataStates.keys()))
    except IndexError:
        o1 = OptionMenu(self.top, stateStr, "", "")

    pin = StringVar(self.top)
    pinStr = "Variable"
    variables = []
    for d in list(dataPin.keys()):
        variables.append(dataPin[d][0])
    try:
        pin.set(variables[0])
        o2 = OptionMenu(self.top, pin, *variables)
    except IndexError:
        o2 = OptionMenu(self.top, pinStr, "", "")

    o1.config(highlightbackground='gray', bg='gray')
    o2.config(highlightbackground='gray', bg='gray')

    o1.grid(row=1, column=1)
    o2.grid(row=2, column=1)

    e3 = Entry(self.top, highlightbackground="gray")

    e3.grid(row=3, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda s=self, t=title, state=state, var=pin, val=e3, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addAnalogWrite(s, t, state, var, val, l, fm, dP, dS, dF))
    button1.grid(row=3, column=3)


def addAnalogWrite(self, title, state, variable, val, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        print dataPin
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            try:
                value = int(val.get())
                code =  "analogWrite(" + variable.get() + ", " + str(value) + ");\n"
                updateCode(state, code, title, dataFlow)
                status_label.txtvar.set(title + " operation added.")
                self.top.destroy()
            except ValueError:
                status_label.txtvar.set("Invalid value format.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")

def ifElse(self, title, frameMaster, v, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    # master = Tk()
    # Frame.__init__(self, master, relief=SUNKEN, bd=2)

    # self.top.geometry("{0}x{1}+0+0".format(
    #        self.master.winfo_screenwidth()/3, self.master.winfo_screenheight()/5))
    self.top.title(title)
    self.top.config(bg="gray")

    self.topFrame = Frame(self.top, bg='gray', height=self.top.winfo_screenheight() / 6,
                          width=self.top.winfo_screenwidth() / 2, highlightbackground='gray')
    self.topFrame.grid(row=1, column=0, sticky=E + W)

    self.centerFrame = Frame(self.top, bg='gray', height=self.top.winfo_screenheight() / 6,
                             width=self.top.winfo_screenwidth() / 2, highlightbackground='gray')
    self.centerFrame.grid(row=2, column=0, sticky=E + W)

    self.bottomFrame = Frame(self.top, bg='gray', height=self.top.winfo_screenheight() / 6,
                             width=self.top.winfo_screenwidth() / 2, highlightbackground='gray')
    self.bottomFrame.grid(row=3, column=0, sticky=E + W)

    label1 = Label(self.topFrame, text="State:", bg="gray")
    label1.grid(row=0, column=1, sticky=W + E)

    label2 = Label(self.topFrame, text="Condition:", bg="gray", pady=20)
    label2.grid(row=1, column=0, sticky=W + E)

    label3 = Label(self.centerFrame, text="Execution:", bg="gray")
    label3.grid(row=0, column=0, sticky=W + E)

    label4 = Label(self.centerFrame, text="Do", bg="gray")
    label4.grid(row=0, column=1, sticky=W + E)

    label5 = Label(self.centerFrame, text="Otherwise do", bg="gray")
    label5.grid(row=0, column=2, sticky=W + E)

    # Safe Arrays
    states = dataStates.keys()
    if len(states) == 0:
        states.append("")

    variables = []
    for k,v in dataPin.iteritems():
        if k[0] == "V":
            variables.append(v[0])
    if len(variables) == 0:
        variables.append("                   ")
    variables.append("Add new variable")

    functions = list(opList)
    functions.append("Pass")

    # Add components
    state = StringVar(self.top)
    state.set(states[0])
    stateMenu = OptionMenu(self.topFrame, state, *states)
    stateMenu.config(bg="gray", highlightbackground="gray")
    # Condition Dropdownmenus
    var1 = StringVar(self.top)
    var1.set(variables[0])
    var1Menu = OptionMenu(self.topFrame, var1, *variables)
    var1Menu.config(highlightbackground="gray", bg="gray")

    operators = ["equals", "is different from", "is greater than", "is greater than or equals", "is less than", "is less than or equals"]
    op = StringVar(self.top)
    op.set(operators[0])
    opMenu = OptionMenu(self.topFrame, op, *operators)
    opMenu.config(highlightbackground="gray", bg="gray")

    var2 = StringVar(self.top)
    var2.set(variables[0])
    var2Menu = OptionMenu(self.topFrame, var2, *variables)
    var2Menu.config(highlightbackground="gray", bg="gray")
    # for item in

    # code inside if condition
    # if
    opr = StringVar(self.top)
    opr.set(functions[0])
    oprMenu = OptionMenu(self.centerFrame, opr, *functions)
    oprMenu.config(bg="gray", highlightbackground="gray")

    # else
    opre = StringVar(self.top)
    opre.set(functions[0])
    opreMenu = OptionMenu(self.centerFrame, opre, *functions)
    opreMenu.config(bg="gray", highlightbackground="gray")


    stateMenu.grid(row=0, column=2, sticky=E+W)
    var1Menu.grid(row=1, column=1, sticky=E+W)
    opMenu.grid(row=1, column=2, sticky=E+W)
    var2Menu.grid(row=1, column=3, sticky=E+W)
    oprMenu.grid(row=1, column=1, sticky=E+W)
    opreMenu.grid(row=1, column=2, sticky=E+W)

    if op.get() == "equals":
        oP = " == "
    elif op.get() == "is different from":
        oP = " != "
    elif op.get() == "is greater than":
        oP = " > "
    elif op.get() == "is greater than or equals":
        oP = " >= "
    elif op.get() == "is less than":
        oP = " < "
    elif op.get() == "is less than or equals":
        oP = " <= "

    status = StringVar()
    statusLabel = Label(self.bottomFrame, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=1, column=1, sticky=W)

    button1 = Button(self.centerFrame, height=1, width=15, relief=FLAT, bg="gray", fg="gray",
                     highlightbackground="gray", text="Save condition",
                     command=lambda t=title, state=state, var1=var1, operator=oP, var2=var2, operation=opr, operationElse=opre, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addifElse(self, t, state, var1, operator, var2, opr, opre, l, fm, dP, dS, dF))
    button1.grid(row=2, column=2, sticky=W+E)


def addifElse(self,title, state, var1, operator, var2, opr, opre, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates.keys():
        if opr.get() in opList or opre.get() == "Pass":
            if opre.get() in opList or opre.get() == "Pass":
                # value = int(val.get())
                code = "if(" + var1.get() + operator + var2.get() + ") {\n\t__flag__\n} else {\n\t__flag__\n}"
                
                updateCode(state, code, title, dataFlow)
                self.top.destroy()

                opFunc[opr.get()](self, "If block - " + opr.get(), frameMaster, [], dataPin, dataStates, dataFlow)
                opFunc[opre.get()](self, "Else block - " + opre.get(), frameMaster, [], dataPin, dataStates, dataFlow)
            else:
                status_label.txtvar.set("False-case operator not found.")
                print opre.get()
        else:
            status_label.txtvar.set("True-case operator not found.")
    else:
        status_label.txtvar.set("State not found.")
    # status_label.txtvar.set("Hallo")


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

    state = StringVar(self.top)
    stateStr = "State"
    try:
        state.set(list(dataStates.keys())[0])
        o1 = OptionMenu(self.top, state, *list(dataStates.keys()))
    except IndexError:
        o1 = OptionMenu(self.top, stateStr, "", "")


    o1.config(highlightbackground='gray', bg='gray')

    o1.grid(row=1, column=1)

    e2 = Entry(self.top, highlightbackground="gray")

    e2.grid(row=2, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda s=self, t=title, state=state, timeout=e2, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addWait(s, t, state, timeout, l, fm, dP, dS, dF))
    button1.grid(row=2, column=3)

def addWait(self, title, state, timeout, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        try:
            delay = int(timeout.get())    
            code =  "delay(" + str(delay) + ");\n"
            updateCode(state, code, title, dataFlow)
            status_label.txtvar.set(title + " operation added.")
            self.top.destroy()
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

    state = StringVar(self.top)
    stateStr = "State"
    try:
        state.set(list(dataStates.keys())[0])
        o1 = OptionMenu(self.top, state, *list(dataStates.keys()))
    except IndexError:
        o1 = OptionMenu(self.top, stateStr, "", "")

    pin = StringVar(self.top)
    pinStr = "Variable"
    variables = []
    for d in list(dataPin.keys()):
        variables.append(dataPin[d][0])
    try:
        pin.set(variables[0])
        o2 = OptionMenu(self.top, pin, *variables)
    except IndexError:
        o2 = OptionMenu(self.top, pinStr, "", "")

    o1.config(highlightbackground='gray', bg='gray')
    o2.config(highlightbackground='gray', bg='gray')

    o1.grid(row=1, column=1)
    o2.grid(row=2, column=1)

    e3 = Entry(self.top, highlightbackground="gray")
    e4 = Entry(self.top, highlightbackground="gray")

    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)

    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=5, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save operation",
                     command=lambda s=self, t=title, state=state, var=pin, frq=e3, dur=e4, l=statusLabel, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                     addTone(s, t, state, var, frq, dur, l, fm, dP, dS, dF))
    button1.grid(row=4, column=3)

def addTone(title, state, variable, frq, dur, status_label, frameMaster, dataPin, dataStates, dataFlow):
    if state.get() in dataStates:
        if variable.get() in map(lambda a: a[0], dataPin.values()):
            try:
                frequency = int(frq.get())
                duration = int(dur.get())
                code = "tone(" + variable.get() + ", " + str(frequency) + ", " + str(duration) + ");\n"
                updateCode(state, code, title, dataFlow)
                status_label.txtvar.set(title + " operation added.")
                self.top.destroy()
            except ValueError:
                status_label.txtvar.set("Invalid value format.")
        else:
            status_label.txtvar.set("Variable name not found.")
    else:
        status_label.txtvar.set("State not found.")

def updateCode(state, code, title, dataFlow):
    if len(dataFlow[state.get()]) > 0 and "__flag__" in dataFlow[state.get()][-1][0]:
        last = dataFlow[state.get()][-1]
        tup = (last[0].replace("__flag__", code, 1), last[1])
        dataFlow[state.get()][-1] = tup
    else:
        print dataFlow[state.get()]
        dataFlow[state.get()].append((code, state.get()+"_"+title.replace(' ',"").replace('-', '')))

opList = ["Digital write", "Analog write", "Digital read", "Wait", "Tone", "Condition"]

opFunc = {"Digital write": digitalWrite, "Analog write": analogWrite, "Digital read": digitalRead, "Wait": wait, "Tone": tone, "Condition": ifElse}

portList = ["A0", "A1","A2", "A3", "A4", "A5", "D0", "D1","D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9" ,"D10" ,"D11" ,"D12", "D13"]