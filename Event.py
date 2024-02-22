#handelong events like clicking mouse,doubble clicking  for more explore all kinter events 
from tkinter import *
root=Tk()
def kirti(Event):#it takes one arrgumet to deal with a event
    print(f'you clicked the buttton {Event.x},{Event.y} ')
#by adding this f string it will keep tack on which x y cordinatre of
    # the scren u are clicking the button
root.title("Events in Tkinter")
root.geometry('500x300')
frame=Frame(root,bg="blue",borderwidth=10,relief=RAISED)
frame.pack(side=RIGHT,anchor=NE)
widget=Button(frame,text='Click Here',bg="white",fg='blue',borderwidth=10,relief=RAISED,font="simple 20 bold")
widget.bind('<Button-1>',kirti)
widget.bind('<Double-1>',quit)#it quit the program by double clicking 
widget.pack()
root.mainloop()