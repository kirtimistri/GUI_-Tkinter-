from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Radio Button")
root.geometry("690x600")
def order():
    tmsg.showinfo('order resived',f"your {var.get()} order has been conform")
var=StringVar()
var.set("dishes")
frame=Frame(root,bg="purple",borderwidth=10,relief=RAISED)
frame.pack(side=BOTTOM)
Label(text="What you will like to order from menu,Sir?",font="lucida 19 bold",bg="lightblue").pack()
dishes={"Dosa","Utappa","Idli","usal","Misal","Pavbhaji","Mendu vada","Masala dosa","pannir","Pannir masala"}
for dishes in enumerate(dishes,start=1):
    #print(dishes)
 radio =Radiobutton(root,text=dishes,variable=var, value=dishes,font="lucida 15 bold",fg="purple").pack(anchor="w")
Button(frame,text="Order Now !",font="lucida 19 bold",fg="white",bg="red",command=order).pack()
root.mainloop()

