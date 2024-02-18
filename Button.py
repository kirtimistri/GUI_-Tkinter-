#making basic buttons
from tkinter import *
root=Tk()
root.geometry("195x160")
def f1():
    print("u are pressing print button")
def f2():
    print("u are pressing Edit button ")
def f3():
    print("u are pressing HELP button")
def f4():
    print("u are pressing Enter button")
frame=Frame(root,bg="purple",borderwidth=10,relief=RAISED)
frame.pack(side=RIGHT,anchor=NE)
b1=Button(frame,text="print ",fg="blue",command=f1)
b1.pack(side=LEFT)
b2=Button(frame,text="Edit",fg="blue",command=f2)
b2.pack(side=LEFT)
b3=Button(frame,text="HELP",fg="RED",command=f3)
b3.pack(side=LEFT)
b4=Button(frame,text="Enter ",fg="blue",command=f4)
b4.pack(side=LEFT)
root.mainloop()