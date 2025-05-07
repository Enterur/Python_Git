from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지 ㄱㅇㅇ")

window = Tk()

photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\Window_programming(week9)\\dog_photo2.gif")
button1 = Button(window, image = photo, command =myFunc)

button1.pack()

window.mainloop()