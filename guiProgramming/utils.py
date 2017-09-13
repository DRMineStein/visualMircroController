from Tkinter import *
from PIL import ImageTk, Image
import arduino

def clear_frame(frame):
    for child in frame.winfo_children():
        child.destroy()

def add_picture(self, frame, picture_name, width, height, resize):
    path = picture_name+".gif"
    im_temp = Image.open(path)
    if resize:
        im_temp = im_temp.resize((width, height),
                                 Image.ANTIALIAS)
        im_temp.save(picture_name+"resized.gif", "gif")
        self.photo = PhotoImage(file=picture_name+"resized.gif")
    else:
        self.photo = PhotoImage(file=picture_name + ".gif")
    picture = Label(frame, bg="gray", image=self.photo)  # Sets the image to the label
    picture.grid(row=0, column=0)
    return picture


def add_scrollbar(master, frame, title, scroll_list, cmd, w, h, view_list, dataPin, dataStates, dataFlow, type):
    # view_list = []
    label = Label(frame, text=title, bg="grey", highlightbackground="gray")
    subFrame = Frame(frame, bg="grey", highlightbackground="gray")
    
    label.grid(row=0, column=0, sticky=N+S)
    subFrame.grid(row=1, column=0, sticky=N+S)

    canvasScroll = Canvas(subFrame, bg="grey", highlightbackground="gray")
    view_list.append(canvasScroll)
    frameScroll = Frame(canvasScroll, bg="grey", highlightbackground="gray")
    view_list.append(frameScroll)
    myscrollbar = Scrollbar(subFrame, orient="vertical", command=canvasScroll.yview)
    view_list.append(myscrollbar)
    canvasScroll.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="both")
    canvasScroll.pack(fill="both", expand=1)
    frameScroll.pack(fill="both", expand=1)

    canvasScroll.create_window((0, 0), window=frameScroll, width=w)
    # frameScrollBoard.bind("<Configure>", utils.myfunctionScroll)
    frameScroll.bind("<Configure>", lambda event, c=canvasScroll, width=w, height=h:
        myfunctionScroll(event, c, width, height - 20))
    # buttonBoardScroll(frameScrollBoard)
    buttonScroll(master, frameScroll, title, 0, 0, scroll_list, cmd, master, view_list, dataPin, dataStates, dataFlow)

    return view_list


def buttonScroll(master, frameScroll, title, row, col, l, cmds, frameMaster, view_list, dataPin, dataStates, dataFlow):
    gridPos = 1
    btn_list = []

    for i in range(0, len(l)):

        b = l[i]
        ref = b

        for key in dataPin.keys():
            if dataPin[key][0] == title.split()[0]:
                ref = key
                break

        print dataPin
        print b
        cmd = cmds[i]

        btn = Button(frameScroll, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text=b,
                         command=lambda command=cmd, f=master, t=b, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates,
                                        dF=dataFlow:
                         command(f, t, fm, v, dP, dS, dF))

        btn.pack(fill=X)
        btn_list.append(btn)
        gridPos += 1

    return btn_list


def myfunctionScroll(event, canvas, w, h):
    canvas.configure(scrollregion=canvas.bbox("all"), width=w, height=h, bg="gray")
