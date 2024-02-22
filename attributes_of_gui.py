# here some attributes of Label and pack 
from tkinter import *
root=Tk()
root.geometry("1500x1500")
root.configure(bg='#333333',relief=GROOVE,borderwidth=30)
root.title(" a short story for you ")
# importent Label attributes
title_label=Label(text=''' \nEmily is 8 years old. She lives in a big house. She has a huge room.
 She has many toys and she has a lot of friends. But Emily is not happy. She has a secret.
She doesn't want to tell anyone about her secret.
\nShe feels embarrassed. The problem is that if nobody knows
 about it, there is no one that can help her.
Emily doesn't write her homework. When there is an exam ,
 \nshe gets sick. She doesn't tell anyone, but the truth is she can't read and write. 
Emily doesn't remember the letters of the alphabet.
One day, Emily's teacher finds out. She sees that Emily can't write on the board. 
\nShe calls her after class and asks her to tell the truth. Emily says,
 "It is true. I don't know how to read and write". The teacher listens to her. She wants to help Emily.
 She tells her, "That's ok. You can read and write if we practice together".
So Emily and her teacher meet every day after class.
 They practice together. \nEmily works hard. Now she knows how to read and write!''',bg="lightblue",fg="purple",padx=113,pady=120,font=("Modern",20,"bold"),borderwidth=30,relief=RIDGE)
#Importent pack attribute
title_label.pack(anchor=NW,side=BOTTOM,fill=X,padx=34,pady=20)
root.mainloop()

