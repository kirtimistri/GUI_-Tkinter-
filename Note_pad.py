from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        with open(file, "r") as f:
            textarea.insert(1.0, f.read())

def savefile():
    global file
    if file is None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(textarea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        with open(file, "w") as f:
            f.write(textarea.get(1.0, END))

def quitapp():
    root.destroy()

def cut():
    textarea.event_generate('<<Cut>>')

def copy():
    textarea.event_generate('<<Copy>>')

def paste():
    textarea.event_generate('<<Paste>>')

def about():
    showinfo('Notepad', "This Notepad was created by Kirti on 28/6/2024")

if __name__ == "__main__":
    # Main tkinter window code
    root = Tk()
    root.title("Notepad by Kirti")
    root.geometry('600x650')
    
    # Text area code
    textarea = Text(root, font=("Times New Roman", 28, "bold"), bg='#292a29', fg='white')
    textarea.pack(fill=BOTH, expand=True)
    file = None
    
    # Creating menu
    # File menu starts
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    
    # To open new file
    filemenu.add_command(label='New', command=newfile)
    
    # To open already existing file
    filemenu.add_command(label='Open', command=openfile)
    
    # To save file
    filemenu.add_command(label='Save', command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=quitapp)
    menubar.add_cascade(label='File', menu=filemenu)
    
    # File menu ends
    # Starting of edit menu
    editmenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    
    # To add cut, copy, paste feature
    editmenu.add_command(label='Cut', command=cut)
    editmenu.add_command(label='Copy', command=copy)
    editmenu.add_command(label='Paste', command=paste)
    menubar.add_cascade(label='Edit', menu=editmenu)
    
    # Edit menu ends
    # Help menu start
    helpmenu = Menu(menubar, tearoff=0, bg='#292a29', fg='white')
    helpmenu.add_command(label='About Notepad', command=about)
    menubar.add_cascade(label='Help', menu=helpmenu)
    root.config(menu=menubar)
    
    # To add scrollbar
    scrollbar = Scrollbar(textarea)
    scrollbar.pack(fill=Y, side=RIGHT)
    
    # Set scrollbar to the text area
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)
    
    root.mainloop()
