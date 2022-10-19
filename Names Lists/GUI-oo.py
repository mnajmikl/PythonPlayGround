from random import shuffle
from tkinter import *
from tkinter import messagebox

boysnames = ["Michael", "John", "Chad", "Greg", "Peter", "Patrick", "Carter", "Franz", "Stewie"]
girlsnames = ["Mary", "Jane", "Amye", "Lois", "Megan", "Bonnie", "Consuela", "Kate", "Trisha"]

"""
MyGUI window class
"""
class MyGUI(Tk):
    def __init__(self, width: bool, height: bool, geometry: str='420x360+10+10',
                 title: str='MyGUI'):
        super().__init__(screenName="mygui_screen", baseName="mygui",
                         className="MyGUI", useTk=TRUE)
        self.title(title)
        self.geometry(geometry)
        self.resizable(width=width, height=height)

        wpadding = {'padx' : 5, 'pady' : 5}

        self.mainframe = Frame(self)
        self.mainframe.pack(expand=True, fill=BOTH)
        
        self.frame1 = Frame(self.mainframe)
        self.frame1['relief'] = 'ridge'
        self.frame1.pack(expand=False, fill=X, anchor=N)
        
        self.buttonrandomize = Button(self.frame1, text='Randomize Lists')
        self.buttonrandomize.pack(**wpadding, expand=False, fill=X)

        self.frame2 = Frame(self.mainframe)
        self.frame2['relief'] = 'ridge'
        self.frame2.pack(expand=False, fill=X, anchor=N)
        
        self.buttonaddboys = Button(self.frame2, text='Add to Boys list')
        self.buttonaddboys.pack(**wpadding, expand=True, fill=X, side=RIGHT)
        
        self.editboys = Entry(self.frame2, font=('Arial 14'))
        self.editboys.pack(**wpadding, expand=True, fill=X, side=LEFT)

        self.frame3 = Frame(self.mainframe)
        self.frame3['relief'] = 'ridge'
        self.frame3.pack(expand=False, fill=X, anchor=N)
        
        self.buttonaddgirls = Button(self.frame3, text='Add  to Girls list')
        self.buttonaddgirls.pack(**wpadding, expand=True, fill=X, side=RIGHT)
        
        self.editgirls = Entry(self.frame3, font=('Arial 14'))
        self.editgirls.pack(**wpadding, expand=True, fill=X, side=LEFT)

        self.frame4 = Frame(self.mainframe)
        self.frame4['relief'] = 'ridge'
        self.frame4.pack(expand=True, fill=BOTH, anchor=N)

        self.frameleft = LabelFrame(self.frame4)
        self.frameleft['relief'] = 'groove'
        self.frameleft['text'] = "Boy's Names"
        self.frameleft.pack(**wpadding, expand=True, fill=BOTH, side=LEFT)

        self.frameright = LabelFrame(self.frame4)
        self.frameright['relief'] = 'groove'
        self.frameright['text'] = "Girl's Names"
        self.frameright.pack(**wpadding, expand=True, fill=BOTH, side=RIGHT)
        
        boysnamesvars = StringVar(value=boysnames)
        self.listbox1 = Listbox(self.frameleft, listvariable=boysnamesvars)
        self.listbox1['relief'] = 'flat'
        self.listbox1.pack(**wpadding, expand=True, fill=BOTH, side=LEFT)

        self.scrollbar1 = Scrollbar(self.listbox1, orient="vertical")
        self.scrollbar1.pack(side=RIGHT, fill=Y)
        self.listbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)

        girlsnamesvars = StringVar(value=girlsnames)
        self.listbox2 = Listbox(self.frameright, listvariable=girlsnamesvars)
        self.listbox2['relief'] = 'flat'
        self.listbox2.pack(**wpadding, expand=True, fill=BOTH, side=RIGHT)

        self.scrollbar2 = Scrollbar(self.listbox2, orient="vertical")
        self.scrollbar2.pack(side=RIGHT, fill=Y)
        self.listbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.listbox2.yview)

        self.frame5 = LabelFrame(self.mainframe)
        self.frame5['relief'] = 'ridge'
        self.frame5.pack(expand=False, fill=X, anchor=S)

        self.labelstatus = Label(self.frame5)
        self.labelstatus.pack(expand=False, fill=X, side=LEFT)
        self.labelstatus['text'] = "Status: "
        
        self.create_mainmenu()

        self.protocol("WM_DELETE_WINDOW", lambda: MyGUI.exit_app(self))

        """
        Bind event to randomize button
        """
        self.buttonrandomize.bind('<Button-1>',
                                  lambda event:
                                  randomizelist(self.listbox1.get(0, END),
                                                              self.listbox1), add="+")
        self.buttonrandomize.bind('<Button-1>',
                                  lambda event:
                                  randomizelist(self.listbox2.get(0, END),
                                                              self.listbox2), add="+")

        """
        Bind event to add names buttons 
        """
        self.buttonaddboys.bind('<Button-1>', resetrelief, add="+")
        self.buttonaddboys.bind('<Button-1>',
                                lambda event:
                                addnametolist(self.listbox1,
                                              self.editboys,
                                              self.labelstatus, "Boy's"), add="+")
        self.buttonaddgirls.bind('<Button-1>', resetrelief, add="+")
        self.buttonaddgirls.bind('<Button-1>',
                                 lambda event:
                                 addnametolist(self.listbox2,
                                                self.editgirls,
                                                self.labelstatus, "Girl's"), add="+")
        
    """
    Create main menu for the main window
    """
    def create_mainmenu(self):
        self.mainmenu = Menu()
        
        self.filemenu = Menu(master=self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Open", accelerator='Ctrl+O',
                                  command=openf)
        self.filemenu.add_command(label="Save", accelerator='Ctrl+S',
                                  command=save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", accelerator='Alt+F4',
                                  command=lambda: MyGUI.exit_app(self))

        self.editmenu = Menu(master=self.mainmenu, tearoff=0)
        self.editmenu.add_command(label="Cut", accelerator='Ctrl+X',
                                  command=cut)
        self.editmenu.add_command(label="Copy", accelerator='Ctrl+C',
                                  command=copy)
        self.editmenu.add_command(label="Paste", accelerator='Ctrl+V',
                                  command=paste)

        self.helpmenu = Menu(master=self.mainmenu, tearoff=0)
        self.helpmenu.add_command(label="About", accelerator="F1", command=about)
        
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)
        self.mainmenu.add_cascade(label="Edit", menu=self.editmenu)
        self.mainmenu.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.mainmenu)

        """
        Bind all the keyboard inputs
        """
        self.bind("<Alt-F4>", lambda event: MyGUI.exit_app(self))
        self.bind("<F1>", about)
        self.bind("<Control-o>", openf)
        self.bind("<Control-s>", save)
        self.bind("<Control-x>", cut)
        self.bind("<Control-c>", copy)
        self.bind("<Control-v>", paste)

    """
    Static method to end the application
    """
    @staticmethod
    def exit_app(window: Tk) -> None:
        if messagebox.askyesno(title="Close window",
                               message=
                               "Do you want exit this application?") == True:
            window.destroy()

"""
Events commands
"""
def print_menu_command(command: str):
    print(f"Command selected was {command}")

def openf(event=None):
    print_menu_command('File->Open')

def save(event=None):
    print_menu_command('File->Save')

def cut(event=None):
    print_menu_command('Edit->Cut')

def copy(event=None):
    print_menu_command('Edit->Copy')

def paste(event=None):
    print_menu_command('Edit->Paste')

def about(event=None):
    messagebox.showinfo(message = "Names Lists 0.0.1", title = "About")

"""
Randomize content of listbox
"""
def randomizelist(l, lbox: Listbox):
    names = list(l)
    shuffle(names)
    namesvars = StringVar(value=names)
    lbox['listvariable'] = namesvars

def addnametolist(lbox: Listbox, edit: Entry, status: Label, gender: str):
    name = edit.get()
    if name in list(lbox.get(0, END)):
        showstatus(f"{name} has already exists in {gender} list", status)
        return
    if name == "":
        return
    lbox.insert("end", name)
    edit.delete(0, END)
    showstatus(f"{name} has been added to {gender} list", status)

def showstatus(details: str, status: Label):
    status['text'] = f"{details}"

def resetrelief(event=None):
    if isinstance(event.widget, Button):
        event.widget.config(relief=RAISED)
    
"""
Launch the window and start the application
"""
if __name__ == "__main__":
    mygui = MyGUI(width=FALSE, height=FALSE,
                  title='Names Lists')
    mygui.mainloop()
