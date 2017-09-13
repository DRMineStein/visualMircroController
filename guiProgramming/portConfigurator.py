from Tkinter import *
import ViewsMenuFunction

def configurePin(self, frameMaster, type, pins, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(type)
    self.top.config(bg="gray")

    label = Label(self.top, text="Pin ID:", bg="gray")
    label.grid(row=0, column=0)

    var = StringVar()
    var.set(pins[0])

    options = apply(OptionMenu, (self.top, var) + tuple(pins))
    options.config(bg="gray")
    options.grid(row=0, column=1)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Configure",
                    command=lambda s=self, fm=frameMaster,
                                    dP=dataPin, dS=dataStates, dF=dataFlow:
                    setPortAndDestroyTopLevel(s, var.get(), fm, [], dP, dS, dF))

    button1.grid(row=0, column=2)

def setPortAndDestroyTopLevel(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):   
    self.top.destroy()
    setPort(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow)

def setPort(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):        
    self.top = Toplevel()

    if title[0] == "V":
        self.top.title("Configuring variable")
    else:
        self.top.title(title)
    
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please configure the variable:", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    label1 = Label(self.top, text="Variable name:", bg="gray")
    label1.grid(row=1, sticky=W)
    label2 = Label(self.top, text="Initial value:", bg="gray")
    label2.grid(row=2, sticky=W)
    label3 = Label(self.top, text="Options:", bg="gray")
    label3.grid(row=3, sticky=W)
    
    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")      

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    flags = StringVar()
    strings = []

    if title[0] == "D":
        strings.append("Input")
        strings.append("Output")
    else:
        strings.append("Default")

    if title == "A4":
        strings.append("SDA")
    elif title == "A5":
        strings.append("SCL")

    flags.set(strings[0])
    options = apply(OptionMenu, (self.top, flags) + tuple(strings))
    options.config(bg="gray")
    options.grid(row=3, column=1, sticky=W+E)

    if title in dataPin.keys():
        e1.insert(END, dataPin[title][0])
        e2.insert(END, dataPin[title][1])
        flags.set(dataPin[title][2])
    
    status = StringVar()
    statusLabel = Label(self.top, textvariable=status, bg="gray")
    statusLabel.txtvar = status
    statusLabel.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save pin",
                     command=lambda s=self, t=title, varN=e1, varV=e2, options=flags, l=statusLabel, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     savePort(self, t, varN, varV, options, l, fm, v, dP, dS, dF))
    button1.grid(row=2, column=3)

    print dataPin

def savePort(self, title, e1, e2, options, l, fm, v, dP, dS, dF):
    save = True
    if len(e1.get()) == 0:
        e1.delete(0, END)
        e2.delete(0, END)
        l.txtvar.set("In order to save the pin at least a variable name is required")
        save = False
    else:
        for key, values in dS.iteritems():
            if values[0] == e1.get() and key!=title:
                e1.delete(0, END)
                l.txtvar.set("Variable name already used for " + key + ". Change the variable name.")
                save = False
                break

    if save:
        dP[title] = (e1.get(), e2.get(), options.get())
        self.top.destroy()
        ViewsMenuFunction.gotoBoardView(self, v, dP, dS, dF)
    
    print dP

