from tkinter import *
root=Tk()
root.title("Watsapp")
root.geometry("690x300")
root.configure(bg='#0a7e8c',borderwidth=10)
def see():
    statusbar.set("Loding....")
    import time
    time.sleep(2)
    statusbar.set("View")
Label(text="View WhatsApp Satus Updates",bg='#0a7e8c',fg='white',font="lucida 19 bold").pack()
statusbar=StringVar()
statusbar.set("Loding....")
sbar=Label(root,textvariable=statusbar,relief=SUNKEN,anchor=W).pack(fill=X,side=BOTTOM)
Button(root,text="view Satus",command=see).pack()
root.mainloop()