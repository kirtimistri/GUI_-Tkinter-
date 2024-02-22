# this will add an massage box to vs code editr
#this is vs code edit page clone
from tkinter import *
import tkinter.messagebox as tmsg# it imports bult in massage box of tkinter
root=Tk()
root.geometry("800x400")
root.title("VS Code Editer")
def f1():
    print("meking a new file in vs code")

    # this function will show two pop up massage as a responce to yes or no
def rate():
    print("Rate us")
    #askquestion will display question massage 
    #it talkes 2 arguments tittle of massage box and queston
    Value=tmsg.askquestion('was your experiance good?',"was your experiance good?")
    print(Value)
    if Value=='yes':
        msg=("Great!! Rate us on playstore")
    else:
        msg=("Tell us what went wrong we will fix it")
    tmsg.showinfo('Experiance',msg)

def help():
    print("kirti will help you")
    #tmsg will create a massage box and
    # showinfo will display tittle of masssage box and the final message 
    a=tmsg.showinfo("message","Kirti will help u")

#create ok and cancel button message box
def Error():
    ans=tmsg.askokcancel("Error","can't load...Sorry")
    if ans:
        print("we will try to resolve it soon")
    else:
        print("you clicked cancil button")

#criate retry and cancil button
def uplod():
    ans=tmsg.askretrycancel("message","Faild to uplod...sorry")
    if ans:
        print("Retraying to uplod it")
    else:
        print("you clicked cancil button")

mainmenu=Menu(root)
#tearoff will remove ---- line from menu which saperates the menu for gui page
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

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label='Undo',command=f1)
m1.add_command(label='Redo',command=f1)
m1.add_separator()# this will add a line
m1.add_command(label='Cut',command=f1)
m1.add_command(label='Copy',command=f1)
m1.add_command(label='Paste',command=f1)
root.config(menu=mainmenu,bg='#292a29')
mainmenu.add_cascade(label='Edit',menu=m1)
m2.add_command(label='Open folder',command=f1)

m3=Menu(mainmenu,tearoff=0)
root.config(menu=mainmenu,bg='#292a29')
m3.add_command(label='Help',command=help)
m3.add_command(label='Rate us',command=rate)
m3.add_command(label='Error',command=Error)
m3.add_command(label='Uplod New File',command=uplod)
mainmenu.add_cascade(label='Help',menu=m3)
root.mainloop() 
 