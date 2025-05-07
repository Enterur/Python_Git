from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "고양이에서 마우스가 클릭됨")

window = Tk()
window.geometry("200x200")

photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\Window_programming(week9)\\cat.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()