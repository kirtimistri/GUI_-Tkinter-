from tkinter import *
root=Tk()
root.geometry("1300x600")
root.configure(bg='orange',relief=GROOVE,borderwidth=30)
def getvals():
    print("submititng form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}")
    with open("records.txt",'a')as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}\n")

#initializing and decorating label
welcome=Label(root,text="Welcome to Yatra Tours & Travels",bg="black",fg="pink",font="helvatika 40 bold",borderwidth=20,relief=RAISED,pady=20,padx=50).grid(row=0,column=3)
name=Label(root,text=" name",bg="lightblue",font="Helvetica 20 bold",relief=GROOVE,padx=65,borderwidth=10)
phone=Label(root,text=" Phone Number",bg="lightblue",font="Helvetica 20 bold",relief=GROOVE,borderwidth=10)
gender=Label(root,text="Gender",bg="lightblue",font="Helvetica 20 bold",relief=GROOVE,padx=60,borderwidth=10)
emergency=Label(root,text="Emergency",bg="lightblue",font="Helvetica 20 bold",relief=GROOVE,padx=35,borderwidth=10)
payment=Label(root,text="Payment mode",bg="lightblue",font="Helvetica 20 bold",relief=GROOVE,padx=15,borderwidth=10)
#mentioning grid position of lebals
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)
#mentioning entyry type of labels
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodvalue=IntVar()
#making entry box of that label
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)
#mentioning grid position of Entry lables
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)
#check box & its packing 
foodservise=Checkbutton(text="Want to prebook your meals?",font="Helvetica 10 bold",bg="lightyellow",relief=GROOVE,padx=65,borderwidth=10,variable=foodvalue)
foodservise.grid(row=6,column=3,padx=10)
#button paking and assign commmand 
Button(text="submit to yatra",font="Helvetica 10 bold",fg="white",bg="purple",command=getvals,padx=60,relief=RAISED,borderwidth=10).grid(row=7,column=3)
root.mainloop()