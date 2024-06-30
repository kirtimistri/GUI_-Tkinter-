from tkinter import *
root=Tk()
root.title("List Box")
root.geometry("690x600")
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0  
lbx=Listbox(root,bg='light blue',font="lucida 19 bold")
lbx.pack()
lbx.insert(END,"First Item")
Button(root,text="Add Item",command=add).pack()
root.mainloop()