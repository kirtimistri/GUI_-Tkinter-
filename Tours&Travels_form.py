from tkinter import *
root=Tk()
root.geometry("800x400")
root.maxsize(800,400)
root.configure(bg='#0a7e8c',relief=GROOVE,borderwidth=10)
img=PhotoImage(file='download.png')
Label(root,image=img).place(x=10,y=10)
def getvals():
    print("submititng form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}")
    with open("records.txt",'a')as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}\n")

#initializing and decorating label
welcome=Label(root,text="Welcome to Yatra Tours & Travels",fg="#002366",bg="lightblue",font="Latha 20 bold",borderwidth=10,relief=SUNKEN,pady=10,padx=30).grid(row=0,column=2)
name=Label(root,text="name",font="Helvetica",bg='#002366',fg='white')
phone=Label(root,text="Phone Number",font="Helvetica",bg='#002366',fg='white')
gender=Label(root,text="Gender",font="Helvetica",bg='#002366',fg='white')
emergency=Label(root,text="Emergency",font="Helvetica",bg='#002366',fg='white')
payment=Label(root,text="Payment mode",font="Helvetica",bg='#002366',fg='white')
#mentioning grid position of lebals
name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
payment.grid(row=5,column=1)
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
nameentry.grid(row=1,column=2)
phoneentry.grid(row=2,column=2)
genderentry.grid(row=3,column=2)
emergencyentry.grid(row=4,column=2)
paymententry.grid(row=5,column=2)
#check box & its packing 
foodservise=Checkbutton(text="Want to prebook your meals?",font="Helvetica 10 bold",bg="lightblue",padx=65,variable=foodvalue)
foodservise.grid(row=6,column=2,padx=10)
#button paking and assign commmand 
Button(text="submit to yatra",font="Helvetica 10 bold",fg="white",bg="#002366",command=getvals,padx=60,relief=RAISED,borderwidth=10).grid(row=7,column=2)
root.mainloop()
