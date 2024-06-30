from tkinter import *
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar = Label (self,textvar=self.var,relief=SUNKEN,anchor=W,font="lucida 19 bold",bg="lightblue")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def createbutton(self):
        Button(text="click me",command=self,font="lucida 19 bold",bg="lightblue").pack()
        print("you clicked the button")

if __name__=="__main__":
    windo= GUI ()
    windo.status()
    windo.createbutton()
    windo.mainloop()
