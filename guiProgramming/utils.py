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
    canvasScroll = Canvas(frame, bg="grey", highlightbackground="gray")
    view_list.append(canvasScroll)
    frameScroll = Frame(canvasScroll, bg="grey", highlightbackground="gray")
    view_list.append(frameScroll)
    myscrollbar = Scrollbar(frame, orient="vertical", command=canvasScroll.yview)
    view_list.append(myscrollbar)
    canvasScroll.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="both")
    canvasScroll.pack(fill="both")
    frameScroll.pack(fill="both")

    canvasScroll.create_window((0, 0), window=frameScroll, anchor='center')
    # frameScrollBoard.bind("<Configure>", utils.myfunctionScroll)
    frameScroll.bind("<Configure>", lambda event, c=canvasScroll, width=w, height=h:
        myfunctionScroll(event, c, width, height))
    # buttonBoardScroll(frameScrollBoard)
    buttonScroll(frameScroll, title, 0, 0, scroll_list, cmd, master, view_list, dataPin, dataStates, dataFlow)

    return view_list


def buttonScroll(frameScroll, title, row, col, l, cmds, frameMaster, view_list, dataPin, dataStates, dataFlow):
    listBoardLabel = Label(frameScroll, text=title, bg="grey").grid(row=row, column=col)
    gridPos = 1
    btn_list = []

    for i in range(0, len(l)):

        b = l[i]
        cmd = cmds[i]

        btn = Button(frameScroll, height=1, width=40, relief=FLAT, bg="gray", fg="gray", highlightbackground="gray", text=b,
                         command=lambda command=cmd, f=frameScroll, t=b, fm=frameMaster, v=view_list, dP=dataPin, dS=dataStates,
                                        dF=dataFlow:
                         command(f, t, fm, v, dP, dS, dF))

        btn.grid(row=gridPos, column=0, sticky=E+W)
        btn_list.append(btn)
        gridPos += 1

    return btn_list


def myfunctionScroll(event, canvas, w, h):
        canvas.configure(scrollregion=canvas.bbox("all"), width=w, height=h, bg="gray")
