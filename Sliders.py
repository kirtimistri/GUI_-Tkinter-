from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
#from PIL import Image, ImageTk
root=Tk()
root.geometry("600x800")
root.configure(bg='#6495ed',relief=RAISED,borderwidth=20)
root.title("Voice Editer")

def messagebox():
    print(f"volume is set to{slider2.get()}and bass is set to{slider2.get()}")
    tmsg.showinfo('volume',f"volume is set to{slider2.get()} and bass is set to{slider2.get()}")
img=PhotoImage(file='music.png')
Label(root,image=img).pack(side='bottom')
Label(text='volume setting').pack(side='top')
Label(text='BASS').pack()
Label(text='VOLUME').pack()
slider1 = ttk.Label(root, text='Slider:')
slider1=Scale(root,from_=0,to=100,bg='red',fg='white',orient='horizontal')
slider1.pack()
slider2= Scale(root,from_=0,to=100,bg='blue',fg='white')
slider2.pack()
slider3= Scale(root,from_=0,to=100,bg='yellow',fg='black',tickinterval=50)
slider3.pack()
b1=Button(root,text="Save changes",font='10',fg="blue",command=messagebox,padx=10)
b1.pack()
root.mainloop()