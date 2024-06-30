from tkinter import*
root=Tk()
root.title("userfrendly resizable GUI")
def resize():
    root.geometry(f"{hight.get()}x{Width.get()}")
Label(text="Resize This GUI").pack()
hight=StringVar()
Width=StringVar()
root.geometry("390x300")
Entry(root,textvariable=hight).pack()
Entry(root,textvariable=Width).pack()
Button(root,text="Apply",command=resize).pack()
root.mainloop()