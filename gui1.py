from tkinter import *
from PIL import Image, ImageTk
window_root=Tk()
#width x hight y
window_root.geometry("1500x1500")
window_root.minsize(300,100)
#window_root.maxsize(1200,988)
kirti = Label(text = 'Hey here this is my first GUI ᕙ( ͡° ͜ʖ ͡°)ᕗ')
#for png images 
photo=PhotoImage(file="photo.png")
study_label=Label(image=photo)
study_label.pack()
#for jpg images 
#image=Image.open("photo.jpeg")
#photo=ImageTk.PhotoImage(image)
kirti.pack()
window_root.mainloop()