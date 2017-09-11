from Tkinter import *
import MenuBar
import ViewsMenuFunction

class AppUI(Frame):

    def __init__(self, master=None):
        self.view_handlers = []
        self.dataPin = {}
        self.dataStates = {}
        self.dataFlow = {}

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
        descriptionLable = Label(self.center_frame, text="This program bla bla bla ...", bg="gray")
        descriptionLable.pack()
        self.view_handlers.append(descriptionLable)


root = Tk()

app = AppUI(root)
# app.pack()

root.mainloop()
