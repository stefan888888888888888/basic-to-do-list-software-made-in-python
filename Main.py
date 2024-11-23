from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("List to-do")
window.geometry("350x200")

txt = Entry(width = 30)
txt.grid(column = 0, row = 0)

Combo = Combobox(window)
Combo["values"] = (1, 2 ,3 ,4 ,5 ,6 ,7 ,8, 9, 10)
Combo.current(1)
Combo.grid(column = 1, row = 0)

def sumbit():
    lbl = Label(window, text = txt.get())
    lbl.grid(column = 0, row = Combo.get())

btn = Button(window, text = "Add item", command = sumbit)
btn.grid(column = 2, row = 0)
window.mainloop()