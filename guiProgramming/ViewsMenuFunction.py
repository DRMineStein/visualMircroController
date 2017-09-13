from Tkinter import *
import utils
import portConfigurator as pc
import stateConfigurator as sc
import stateDesignConfigurator as sdc
import arduino

boards = ["arduino_uno_board"]

stateOptions = ["Add new state", "Remove state", "Generate states graph"]

boardSelected = None
pins = []


# def selectBoard(board, self, view_list):
#     global boardSelected
#     global pins
#     boardSelected = board
#     pins = pinLayoutNucleoBoard
#     print pins
#     gotoBoardView(self, view_list)


# def selectPin(pin, self, view_list):
#     pass


def gotoBoardView(self, view_list, dataPin, dataStates, dataFlow):
    global boards
    global pins
    # dataPin = {}
    while len(view_list) != 0:
        view_list.pop().destroy()

    # Top frame label
    lViewName = Label(self.top_frame, text="Board view", bg="light green")
    lViewName.grid(row=0, column=0, stick=E+W)
    view_list.append(lViewName)

    # Bottom frame label
    lStatus = Label(self.bottom_frame, text="Not saved", bg="gray")
    lStatus.grid(row=0, column=0, sticky=E+W)
    view_list.append(lStatus)

    # Create left frame
    left_frame = Frame(self.center_frame, bg='gray', width=3*self.master.winfo_screenwidth()/4,
                       height=self.master.winfo_screenheight())
    left_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(left_frame)


    # Add picture in the left frame
    left_frame_picture = utils.add_picture(self, left_frame, "arduino_uno_boardlayout", 3 * self.master.winfo_screenwidth() / 4 - 5,
                                           self.master.winfo_screenheight() - 210, True)
    view_list.append(left_frame_picture)


    # Separator line
    line = Canvas(self.center_frame, width=100, highlightbackground="light green", bg="light green", height=self.master.winfo_screenheight())
    line.grid(row=0, column=1)
    view_list.append(line)

    # Create right frame
    right_frame = Frame(self.center_frame, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                        height=self.master.winfo_screenheight())
    right_frame.grid(row=0, column=2, sticky="ns")
    view_list.append(right_frame)

    # Split right frame in top and bottom
    rightTop_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                           height=1*self.master.winfo_screenheight()/3)
    rightTop_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(rightTop_frame)

    rightBottom_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray', width=1 * self.master.winfo_screenwidth()/4,
                              height=2*self.master.winfo_screenheight()/3)
    rightBottom_frame.grid(row=1, column=0, sticky="ns")
    view_list.append(rightBottom_frame)

    # Add scroll bar in the top right frame for the list of boards
    rightTop_frame_scrollbar = utils.add_scrollbar(self, rightTop_frame, "List of boards:", boards, [pc.setPort] * len(boards),
                                                   1*self.master.winfo_screenwidth()/4 - 25,
                                                   1 *self.master.winfo_screenheight() / 3, view_list, dataPin, dataStates, dataFlow, 'pin')
    view_list = view_list + rightTop_frame_scrollbar

    # Add scroll bar in the top right frame for the list of boards
    rightBottom_frame_scrollbar = utils.add_scrollbar(self, rightBottom_frame, "List of pins:", arduino.portList, [pc.setPort] * len(arduino.portList),
                                                      1 * self.master.winfo_screenwidth() / 4 - 25,
                                                      2 * self.master.winfo_screenheight() / 3 - 180, view_list, dataPin, dataStates, dataFlow, 'pin')
    view_list = view_list + rightBottom_frame_scrollbar
    # data["PIN"] = dataPin
    print dataPin


def gotoStateView(self, view_list, dataPin, dataStates, dataFlow):
    global stateOptions
    while len(view_list) != 0:
        view_list.pop().destroy()

    # Top frame label
    lViewName = Label(self.top_frame, text="State transition view", bg="light blue")
    lViewName.grid(row=0, column=0, stick=E + W)
    view_list.append(lViewName)

    # Bottom frame label
    lStatus = Label(self.bottom_frame, text="Not saved", bg="gray")
    lStatus.grid(row=0, column=0, sticky=E+W)
    view_list.append(lStatus)

    # Create left frame
    left_frame = Frame(self.center_frame, bg='gray', highlightbackground="gray", width=3 * self.master.winfo_screenwidth() / 4 - 5,
                       height=self.master.winfo_screenheight())
    left_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(left_frame)


    # Separator line
    line = Canvas(self.center_frame, width=0, highlightbackground="light blue", height=self.master.winfo_screenheight())
    line.grid(row=0, column=1)
    view_list.append(line)

    # Create right frame
    right_frame = Frame(self.center_frame, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                        height=self.master.winfo_screenheight())
    right_frame.grid(row=0, column=2, sticky="ns")
    view_list.append(right_frame)

    # Split right frame in top and bottom
    rightTop_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                           height=1 * self.master.winfo_screenheight() / 3)
    rightTop_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(rightTop_frame)

    rightBottom_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray',
                              width=1 * self.master.winfo_screenwidth() / 4,
                              height=2 * self.master.winfo_screenheight() / 3)
    rightBottom_frame.grid(row=1, column=0, sticky="ns")
    view_list.append(rightBottom_frame)

    # Add buttons in the top right frame for the list of boards
    # b = Button(rightTop_frame, text="OK", command=quit)
    # b.grid(row=0, column=0, sticky="we")

    buttonAddState = Button(rightTop_frame, text="Add new state", width= 37, highlightbackground="gray",
                     command=lambda s=rightTop_frame, t="Add new state", m=self, v=view_list, dP=dataPin, dS=dataStates, dF=dataFlow:
                     sc.addState(s, t, m, view_list, dP, dS, dF))
    buttonAddState.grid(row=0, column=0, sticky="we")
    view_list.append(buttonAddState)

    buttonRemoveState = Button(rightTop_frame, text="Remove state", width=37, highlightbackground="gray",
                            command=lambda s=rightTop_frame, t="Add new state", m=self, v=view_list, dP=dataPin,
                                           dS=dataStates, dF=dataFlow:
                            sc.removeState(s, t, m, view_list, dP, dS, dF))
    buttonRemoveState.grid(row=1, column=0, sticky="we")
    view_list.append(buttonRemoveState)

    buttonGenerateGraph = Button(rightTop_frame, text="Generate graph", width=37, highlightbackground="gray",
                            command=lambda s=rightTop_frame, figFrame = left_frame,
                                           w=3 * self.master.winfo_screenwidth() / 4,
                                           h=self.master.winfo_screenheight() - 150,
                                           dP=dataPin, dS=dataStates, dF=dataFlow:
                            sc.generateGraph(s, figFrame, w, h, dP, dS, dF))
    buttonGenerateGraph.grid(row=2, column=0, sticky="we")
    view_list.append(buttonGenerateGraph)

    # Add scroll bar in the top right frame for the list of boards
    rightBottom_frame_scrollbar = utils.add_scrollbar(self, rightBottom_frame, "List of states:", list(dataStates.keys()),
                                                      [sc.configState] * len(dataStates),
                                                      1 * self.master.winfo_screenwidth() / 4 - 25,
                                                      2 * self.master.winfo_screenheight() / 3 + 60, view_list, dataPin, dataStates, dataFlow, 'state')
    view_list = view_list + rightBottom_frame_scrollbar


def gotoDesignView(self, view_list, dataPin, dataStates, dataFlow):
    while len(view_list) != 0:
        view_list.pop().destroy()

    # Top frame label
    lViewName = Label(self.top_frame, text="Design view", bg="salmon")
    lViewName.grid(row=0, column=0, stick=E+W)
    view_list.append(lViewName)

    # Bottom frame label
    lStatus = Label(self.bottom_frame, text="Not saved", bg="gray")
    lStatus.grid(row=0, column=0, sticky=E+W)
    view_list.append(lStatus)

    # Create left frame
    left_frame = Frame(self.center_frame, bg='gray', width=3*self.master.winfo_screenwidth()/4 - 5,
                       height=self.master.winfo_screenheight())
    left_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(left_frame)

    # Separator line
    line = Canvas(self.center_frame, width=0, highlightbackground="salmon", height=self.master.winfo_screenheight())
    line.grid(row=0, column=1)
    view_list.append(line)

    # Create right frame
    right_frame = Frame(self.center_frame, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                        height=self.master.winfo_screenheight())
    right_frame.grid(row=0, column=2, sticky="ns")
    view_list.append(right_frame)

    # Split right frame in top and bottom
    rightTop_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray', width=1 * self.master.winfo_screenwidth() / 4,
                           height=1*self.master.winfo_screenheight()/3)
    rightTop_frame.grid(row=0, column=0, sticky="ns")
    view_list.append(rightTop_frame)

    rightBottom_frame = Frame(right_frame, relief=GROOVE, bd=0, bg='gray', width=1 * self.master.winfo_screenwidth()/4,
                              height=2*self.master.winfo_screenheight()/3)
    rightBottom_frame.grid(row=1, column=0, sticky="ns")
    view_list.append(rightBottom_frame)

    # Add scroll bar in the top right frame for the list of boards
    buttonGenerateGraph = Button(rightTop_frame, text="Generate state flow", width=37, highlightbackground="gray",
                                 command=lambda s=rightTop_frame, t="State flow", figFrame=left_frame,
                                                w=3 * self.master.winfo_screenwidth() / 4,
                                                h=self.master.winfo_screenheight() - 150,
                                                dP=dataPin, dS=dataStates, dF=dataFlow:
                                 sdc.getStateOperation(s, t, figFrame, w, h, dP, dS, dF))
    buttonGenerateGraph.grid(row=2, column=0, sticky="we")
    view_list.append(buttonGenerateGraph)

    # Add scroll bar in the top right frame for the list of boards
    rightBottom_frame_scrollbar = utils.add_scrollbar(self, rightBottom_frame, "Add building block:", arduino.opFunc.keys(), arduino.opFunc.values(),
                                                      1 * self.master.winfo_screenwidth() / 4 - 25,
                                                      2 * self.master.winfo_screenheight() / 3 + 60, view_list, dataPin, dataStates, dataFlow, 'pin')
    view_list = view_list + rightBottom_frame_scrollbar
