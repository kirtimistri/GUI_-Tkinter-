#making basic buttons
from tkinter import *
root=Tk()
root.geometry("600x160")
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
b1=Button(frame,text="print ",font='10',fg="blue",command=f1,padx=10)
b1.pack(side=LEFT)
b2=Button(frame,text="Edit",font='10',fg="blue",command=f2,padx=10)
b2.pack(side=LEFT)
b3=Button(frame,text="HELP",font='10',fg="RED",command=f3,padx=10)
b3.pack(side=LEFT)
b4=Button(frame,text="Enter ",font='10',fg="blue",command=f4,padx=10)
b4.pack(side=LEFT)
root.mainloop()