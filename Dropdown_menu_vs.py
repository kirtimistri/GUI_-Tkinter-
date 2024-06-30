#this is  vs code edit page clone
from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("VS Code Editer")
def f1():
    print("meking a new file in vs code")
def f2():
    print("Editing in vs code")
#(it is a non drop dowm menu)
# mymenu=Menu(root)
# mymenu.add_command(label='file',command=f1)
# mymenu.add_command(label="Exit",command=quit)
# #config works like pack grid here(it is a non drop dowm menu)
# root.config(menu=mymenu,bg='#292a29')

mainmenu=Menu(root)
#tearoff will remove ---- line from menu which saperates the menue fro gui page
m2=Menu(mainmenu,tearoff=0,bg='#292a29',fg='white')
m2.add_command(label='New Text File',command=f1)
m2.add_command(label='New file',command=f1)
m2.add_separator()# this will add a line
m2.add_command(label='New Window',command=f1)
m2.add_command(label='Open file',command=f1)
m2.add_command(label='Open folder',command=f1)
m2.add_command(label='Open Workspace From File',command=f1)
m2.add_command(label='Open Recent',command=f1)
root.config(menu=mainmenu,bg='#292a29')
#add_cascade is used to fit menu in upper task bar
mainmenu.add_cascade(label='File',menu=m2)

m1=Menu(mainmenu,tearoff=0,bg='#292a29',fg='white')
m1.add_command(label='Undo',command=f1)
m1.add_command(label='Redo',command=f1)
m1.add_separator()# this will add a line
m1.add_command(label='Cut',command=f1)
m1.add_command(label='Copy',command=f1)
m1.add_command(label='Paste',command=f1)
root.config(menu=mainmenu,bg='#292a29')
mainmenu.add_cascade(label='Edit',menu=m1)
m2.add_command(label='Open folder',command=f1)
root.mainloop() 
 