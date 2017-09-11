from Tkinter import *


def setPort(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please configure the pin option:", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    label1 = Label(self.top, text="Variable name:", bg="gray")
    label1.grid(row=1, sticky=W)
    label2 = Label(self.top, text="Initial value:", bg="gray")
    label2.grid(row=2, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="OUTPUT", variable=var, bg="gray", highlightbackground="gray")
    c.var = var
    c.grid(row=1, column=3, sticky=W)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=3, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save pin",
                     command=lambda t=title, varN=e1, varV=e2, check=c, l=statusLable, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     savePort(t, varN, varV, check, l, fm, v, dP, dS, dF))
    button1.grid(row=2, column=3)
    print dataPin


def savePort(title, e1, e2, c, l, fm, v, dP, dS, dF):
    save = True
    if len(e1.get()) == 0:
        e1.delete(0, END)
        e2.delete(0, END)
        c.var.set(0)
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
        dP[title] = (e1.get(), e2.get(), c.var.get())
        l.txtvar.set("Pin has been set correctly ")
    print dP
