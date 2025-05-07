from tkinter import *

window = Tk()

def myfunc():
    if var.get == 1:
        label1.configure(text = "Python")
    elif var.get == 2:
        label1.configure(text = "C++")
    else:
        label1.configure(text = "Java")

var = IntVar()
rb1 = Radiobutton(window, text = "Python", variable = var, value = 1, command = myfunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myfunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myfunc)

label1 = Label(window, text = "선택 언어: ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()