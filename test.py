from tkinter import *

def newfile():
    pass

def openfile():
    pass

def savefile():
    pass

def quitapp():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

if __name__ == "__main__":
    # main tkinter window code
    root = Tk()
    root.title("Notepad by Kirti")
    root.geometry('600x650')
    
    # text area code
    textarea = Text(root, font=("Times New Roman", 28, "bold"), bg='#292a29', fg='white')
    textarea.pack(fill=BOTH, expand=True)
    file = None
    
    # creating menu
    menubar = Menu(root)
    
    # file menu starts
    filemenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    filemenu.add_command(label='New', command=newfile)
    filemenu.add_command(label='Open', command=openfile)
    filemenu.add_command(label='Save', command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=quitapp)
    menubar.add_cascade(label='File', menu=filemenu)
    
    # edit menu starts
    editmenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    editmenu.add_command(label='Cut', command=cut)
    editmenu.add_command(label='Copy', command=copy)
    editmenu.add_command(label='Paste', command=paste)
    menubar.add_cascade(label='Edit', menu=editmenu)
    
    # help menu starts
    helpmenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    helpmenu.add_command(label='About Notepad', command=about)
    menubar.add_cascade(label='Help', menu=helpmenu)
    
    root.config(menu=menubar)
    
    # adding scrollbar
    scrollbar = Scrollbar(textarea)
    scrollbar.pack(fill=Y, side=RIGHT)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)
    
    root.mainloop()
