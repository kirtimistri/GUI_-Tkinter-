#this is a working login page 
from tkinter import *
root=Tk()
root.geometry("955x560")
def getval():
    print(uservalue.get())
    print(passwordvalue.get())
l1=Label(root,text="Username",bg="lightpink",borderwidth=5,relief=RAISED,font=("Rubik",10,"bold"))
l2=Label(root,text="Pasword",bg="lightblue",borderwidth=5,relief=RAISED,font=("Rubik",10,"bold"))
l1.grid()
l2.grid(row=1)
uservalue=StringVar()
passwordvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passwordvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="submit",bg="purple",borderwidth=5,fg="white",relief=RAISED,font=("Rubik",10,"bold"),command=getval).grid()
root.mainloop()