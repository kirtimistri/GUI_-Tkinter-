from tkinter import * 
root=Tk()
root.title("scroll bar")
root.geometry("690x600")
# for connection scrool bar to a widget 
# step 1= widget(yscroll command= scrool bar.set())
#step 2= scrollbar.config (command =widget.yview)
scrollbar=Scrollbar(root)
scrollbar.pack(fill=BOTH,side= RIGHT)
listbox= Listbox(root,font="lucida 19 bold",yscrollcommand=scrollbar.set)
scrollbar.config (command =listbox.yview)
for i in range(344):
    listbox.insert(END,f"Item {i}")
    listbox.pack(fill=BOTH)
root.mainloop()