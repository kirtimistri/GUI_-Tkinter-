#here are some canvous widgits
from tkinter import *
root=Tk()
Canvas_width=800
Canvas_hight=400
root.geometry(f"{Canvas_width}x{Canvas_hight}")
can_widget=Canvas(root,width=Canvas_width,height=Canvas_hight)
can_widget.pack()
root.title("GUI shapes")
#the line goes from x1,y1 & x2,y2
can_widget.create_line(0,0,800,400,fill='red')
can_widget.create_line(80,400,80,0,fill='blue')
can_widget.create_line(0,400,800,0,fill='orange')
can_widget.create_line(0,800,400,80,fill='blue')
#to create a rectangle spacify parameters in this order - courners of top letf and courners of bottom right 
can_widget.create_rectangle(10,70,70,300,fill='lightblue')
can_widget.create_text(70,100,fill='purple',text='kirti',font="helvatika 40 bold")
can_widget.create_oval(340,244,244,355,fill='blue')
root.mainloop()
