from Tkinter import *
import ViewsMenuFunction
import graphVizGenerator as gv
import utils

def addStartingState(dataState):
    dataState['setup'] = ([], [])

def addStateOnly(dataState, stateName):
    dataState[stateName] = ([], [])

def addState(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please configure the state option:", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    label0 = Label(self.top, text="State name:", bg="gray")
    label0.grid(row=1, sticky=W)
    label1 = Label(self.top, text="List of incoming states :", bg="gray")
    label1.grid(row=2, sticky=W)
    label2 = Label(self.top, text="List of outcoming states :", bg="gray")
    label2.grid(row=3, sticky=W)
    label3 = Label(self.top, text="Name of different states should be separated by commas", bg="gray")
    label3.grid(row=4, sticky=W)

    e0 = Entry(self.top, highlightbackground="gray")
    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")

    e0.grid(row=1, column=1)
    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="Starting state:", variable=var, bg="gray")
    c.var = var
    c.grid(row=1, column=3, sticky=W)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=5, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Save state",
                     command=lambda s=self, t=e0, ein=e1, eout=e2, check=c, l=statusLable, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     saveState(s, t, ein, eout, check, l, fm, v, dP, dS, dF))
    button1.grid(row=3, column=3)
    print dataStates

def configState(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please configure the state option:", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    # label0 = Label(self.top, text="State name:"+, bg="gray")
    # label0.grid(row=1, sticky=W)
    label1 = Label(self.top, text="List of incoming states :", bg="gray")
    label1.grid(row=1, sticky=W)
    label2 = Label(self.top, text="List of outcoming states :", bg="gray")
    label2.grid(row=2, sticky=W)
    label3 = Label(self.top, text="Name of different states should be separated by commas", bg="gray")
    label3.grid(row=3, sticky=W)

    # e0 = Entry(self.top)
    e1 = Entry(self.top, highlightbackground="gray")
    e2 = Entry(self.top, highlightbackground="gray")

    # e0.grid(row=1, column=1)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)

    var = IntVar()
    c = Checkbutton(self.top, text="Final state:", variable=var, bg="gray", highlightbackground="gray")
    c.var = var
    c.grid(row=1, column=3, sticky=W)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=4, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Set state",
                     command=lambda s=self, t=title, ein=e1, eout=e2, check=c, l=statusLable, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     setState(s, t, ein, eout, check, l, fm, v, dP, dS, dF))
    button1.grid(row=3, column=3)


def removeState(self, title, frameMaster, view_list, dataPin, dataStates, dataFlow):
    self.top = Toplevel()
    self.top.title(title)
    self.top.config(bg="gray")

    descriptionLable = Label(self.top, text="Please enter the name of the states to remove:", bg="gray")
    descriptionLable.grid(row=0, sticky=W)

    e1 = Entry(self.top, highlightbackground="gray")
    # e2 = Entry(self.top)

    e1.grid(row=1, column=0)

    stausString = StringVar()
    statusLable = Label(self.top, textvariable=stausString, bg="gray")
    statusLable.txtvar = stausString
    statusLable.grid(row=2, sticky=W)

    button1 = Button(self.top, height=1, width=15, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text="Set state",
                     command=lambda s=self, t=title, ein=e1, l=statusLable, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     rmState(s, t, ein, l, fm, v, dP, dS, dF))
    button1.grid(row=1, column=1)


def saveState(self, e0, e1, e2, c, l, fm, v, dP, dS, dF):
    save = True
    inc = e1.get()
    inc = inc.replace(" ", "")
    inc = inc.split(',')
    inc = [x for x in inc if x != '']
    outc = e2.get()
    outc = outc.replace(" ", "")
    outc = outc.split(',')
    outc = [x for x in outc if x != '']

    if e0.get() == e1.get():
        l.txtvar.set("A state cannot loop to itself")
        save = False

    print "c:" + str(c.var.get())
    if len(e1.get()) == 0 and c.var.get() == 0:
        e1.delete(0, END)
        e2.delete(0, END)
        c.var.set(0)
        l.txtvar.set("At least an incoming state is required or it should be set as initial state")
        save = False
    else:
        for key, values in dS.iteritems():
            if e0.get() == key:
                e0.delete(0, END)
                l.txtvar.set("State name should be different from the already existing ones.")
                save = False
                break
        # print type(e2.get())

        # for s in outc:
        #     if s == "init":
        #         e2.delete(0, END)
        #         l.txtvar.set("init can be only an incoming state not an outcoming one.")
        #         save = False
        #         break

        init_states = False
        for s in inc:
            if s == "init":
                if not init_states:
                    init_states = True
                else:
                    c.var.set(0)
                    l.txtvar.set("Only one initial state can exists")
                    save = False
                    break

    if save:
        for i in inc:
            if i not in list(dS.keys()) and i != '':
                addStateOnly(dS,i)
        for o in outc:
            if o not in list(dS.keys()) and o != '':
                addStateOnly(dS,o)

        if c.var.get() == 1:
            inc.append('init')

        dS[e0.get()] = (inc, outc)
        for s in inc:
            print "TEST"
            print s
            print dS

            if s == 'init':
                continue
            print dS[s]
            prevState = dS[s]
            incPrevState = prevState[0]
            outcPrevState = prevState[1]
            print outcPrevState
            if e0.get() not in outcPrevState:
                outcPrevState.append(e0.get())

            dS[s] = (incPrevState, outcPrevState)
            print dS

        for s in outc:
            prevState = dS[s]
            incPrevState = prevState[0]
            outcPrevState = prevState[1]
            if e0.get() not in incPrevState:
                incPrevState.append(e0.get())

            dS[s] = (incPrevState, outcPrevState)
            print dS

        dF[e0.get()] = []

        l.txtvar.set("State has been created correctly.")
        e0.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        ViewsMenuFunction.updateCurrentView(fm, v, dP, dS, dF)
    print dS
    print "DF="
    print dF


def setState(self, t, e1, e2, c, l, fm, v, dP, dS, dF):
    save = True
    inc = e1.get()
    inc = inc.replace(" ", "")
    inc = inc.split(',')
    inc = [x for x in inc if x != '']
    print inc
    outc = e2.get()
    outc = outc.replace(" ", "")
    outc = outc.split(',')
    outc = [x for x in outc if x != '']
    print outc

    # if len(e1.get()) == 0:
    #     e1.delete(0, END)
    #     e2.delete(0, END)
    #     c.var.set(0)
    #     l.txtvar.set("At least an incoming state is required")
    #     save = False
    # else:
    #     for s in outc:
    #         if s == "setup":
    #             e2.delete(0, END)
    #             l.txtvar.set("setup can be only an incoming state not an outcoming one.")
    #             save = False
    #             break

    if save:
        for i in inc:
            if i not in list(dS.keys()) and i != '':
                addStateOnly(dS, i)
        for o in outc:
            if o not in list(dS.keys()) and o != '':
                addStateOnly(dS, o)

        dS[t] = (inc, outc)
        for s in inc:
            prevState = dS[s]
            outcPrevState = prevState[1]
            if t not in outcPrevState:
                outcPrevState.append(t)

        for s in outc:
            prevState = dS[s]
            incPrevState = prevState[0]
            if t not in incPrevState:
                incPrevState.append(t)
        l.txtvar.set("State has been created correctly.")
        e1.delete(0, END)
        e2.delete(0, END)
        ViewsMenuFunction.updateCurrentView(fm, v, dP, dS, dF)
    # print dS

def rmState(s, t, ein, l, fm, view_list, dP, dS, dF):
    removed = False
    toremoveStr = ein.get()
    toremoveStr = toremoveStr.replace(" ", "")
    toremoveStr = toremoveStr.split(',')
    for r in toremoveStr:
        if r in list(dS.keys()):
            dS.pop(r, None)
            removed = True
        else:
            l.txtvar.set("The state doesn't exist")
            ein.delete(0, END)
        # print dS
        for key, values in dS.iteritems():
            inc = []
            outc = []
            for v in values[0]:
                if r != v:
                    inc.append(v)
            for v in values[1]:
                if r != v:
                    outc.append(v)

            dS[key] = (inc, outc)

    if removed:
        ViewsMenuFunction.updateCurrentView(fm, view_list, dP, dS, dF)
    print dS

def generateGraph(self, figFrame, w, h, dataPin, dataStates, dataFlow):
    gv.createGraph(dataStates, 'FSM', w - 5, h)
    utils.add_picture(self, figFrame, 'state_graph', w - 5, h, False)