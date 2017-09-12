from Tkinter import *
import MenuBar
from PIL import ImageTk, Image
import ViewsMenuFunction as vm

class AppUI(Frame):

    def __init__(self, master=None):
        self.view_handlers = []
        self.dataPin = {}
        self.dataStates = {}
        self.dataFlow = {}
        self.view_list = []

        Frame.__init__(self, master, relief=SUNKEN, bd=2)

        self.master.title("micro-controller GUI programming")

        self.menubar = Menu(self)
        MenuBar.setupMenu(self, self.view_handlers, self.dataPin, self.dataStates, self.dataFlow)
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)

        self.master.geometry("{0}x{1}+0+0".format(
            self.master.winfo_screenwidth(), self.master.winfo_screenheight()))

        ## Define app layout.
        self.top_frame = Frame(root, bg='gray', width=self.master.winfo_screenwidth(), height=1*self.master.winfo_screenheight()/40)
        self.center_frame = Frame(root, bg='gray', width=self.master.winfo_screenwidth(), height=19*self.master.winfo_screenheight()/20)
        self.bottom_frame = Frame(root, bg='gray', width=self.master.winfo_screenwidth(), height=1*self.master.winfo_screenheight()/40, bd=0.5, relief=SOLID)
        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        self.top_frame.grid(row=0, sticky="nsew")
        self.center_frame.grid(row=1, sticky="nsew")
        self.bottom_frame.grid(row=2, sticky="nsew")
        # create the top frame widgets
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        # create the center widgets
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(1, weight=1)
        # create the bottom frame widgets
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        # Add first widget
        descriptionLable = Label(self.center_frame, text="This graphical user interface allows you to program your Microcontroller\n with specific actions and commands, without writing a single line in C/C++", bg="gray")
        descriptionLable.grid(row=0, column=1)
        self.view_handlers.append(descriptionLable)
        # Change View Buttons
        # boardView Button
        im_temp = Image.open("boardView.gif")
        im_temp = im_temp.resize((5*(self.master.winfo_screenwidth()/18), 3*(self.master.winfo_screenheight()/10)), Image.ANTIALIAS)
        im_temp.save("boardView_resized.gif", "gif")
        self.photo = PhotoImage(file="boardView_resized.gif")
        boardView_btn = Button(self.center_frame, image=self.photo, width=5*(self.master.winfo_screenwidth()/18), height=3*(self.master.winfo_screenheight()/10), highlightbackground='gray', bg='gray', command=lambda: vm.gotoBoardView(self, self.view_list, self.dataPin, self.dataStates, self.dataFlow))
        boardView_btn.grid(row=1, column=0, sticky=W, pady=100, padx=40)
        self.view_handlers.append(boardView_btn)
        self.view_list.append(boardView_btn)

        # stateView Button
        im_temp = Image.open("stateView.gif")
        im_temp = im_temp.resize(
            (5 * (self.master.winfo_screenwidth() / 18), 3 * (self.master.winfo_screenheight() / 10)), Image.ANTIALIAS)
        im_temp.save("stateView_resized.gif", "gif")
        self.photo1 = PhotoImage(file="stateView_resized.gif")
        stateView_btn = Button(self.center_frame, image=self.photo1, width=5 * (self.master.winfo_screenwidth() / 18),
                               height=3 * (self.master.winfo_screenheight() / 10), highlightbackground='gray',
                               bg='gray', command=lambda: vm.gotoStateView(self, self.view_list, self.dataPin, self.dataStates, self.dataFlow))
        stateView_btn.grid(row=1, column=1)
        self.view_handlers.append(stateView_btn)
        self.view_list.append(stateView_btn)

        # designFlow Button
        im_temp = Image.open("designFlowView.gif")
        im_temp = im_temp.resize(
            (5 * (self.master.winfo_screenwidth() / 18), 3 * (self.master.winfo_screenheight() / 10)), Image.ANTIALIAS)
        im_temp.save("designFlowView_resized.gif", "gif")
        self.photo2 = PhotoImage(file="designFlowView_resized.gif")
        designFlowView_btn = Button(self.center_frame, image=self.photo2, width=5 * (self.master.winfo_screenwidth() / 18),
                               height=3 * (self.master.winfo_screenheight() / 10), highlightbackground='gray',
                               bg='gray', command=lambda: vm.gotoDesignView(self, self.view_list, self.dataPin, self.dataStates, self.dataFlow))
        designFlowView_btn.grid(row=1, column=2, sticky=E, pady=100, padx=40)
        self.view_handlers.append(designFlowView_btn)
        self.view_list.append(designFlowView_btn)

root = Tk()

app = AppUI(root)
# app.pack()

root.mainloop()
