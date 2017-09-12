import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        menubar = tk.Menu(self)
        connectionMenu = tk.Menu(self)
        serialMenu = tk.Menu(self)

        menubar.add_cascade(label="Connections", menu=connectionMenu)
        connectionMenu.add_cascade(label="Serial", menu=serialMenu)
        for name in ("Set Data Transmissionrate", ""):
            serialMenu.add_command(label=name)


        root.configure(menu=menubar)
        root.geometry("200x200")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()