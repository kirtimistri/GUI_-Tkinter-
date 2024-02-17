# this is the simple single login page by usking Tkinter 
from tkinter import *
root=Tk()
root.geometry("955x560")
root.maxsize(1200,988)
root.title("Login page")
title_label=Label(text="CUSTOMER LOGIN ",bg="lightblue",font=("Sora",20,"bold"),borderwidth=30,relief=RIDGE,pady=20)
title_label.pack(fill=X,padx=20,pady=20)
f1=Frame(root,bg="lightgray",borderwidth=20,relief=SUNKEN)
f1.pack(side=TOP,anchor=SW)
f2=Frame(root,bg="lightgray",borderwidth=20,relief=SUNKEN)
f2.pack(side=TOP,anchor=SW)
l1=Label(f2,text="Email ID",bg="lightblue",font=("Sora",20,"bold"))
l1.pack(side=LEFT,anchor=SW,padx=30,pady=10)
box=Label(text="                                     ",bg="lightblue",relief=SUNKEN,borderwidth=40)
box.pack(side=BOTTOM,anchor=E,fill=X,padx=10)
l2=Label(f1,text="Password",bg="lightblue",font=("Sora",20,"bold"))
l2.pack(side=LEFT,anchor=SW,padx=30,pady=10)
box=Label(text="                                     ",bg="lightblue",relief=SUNKEN,borderwidth=40)
box.pack(side=BOTTOM,anchor=E,fill=X,padx=10)
root.mainloop()













