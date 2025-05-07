from tkinter import *

window = Tk()

#PhotoImage는 gif 파일만 지원
photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\Window_programming(week9)\\dog_photo1.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()