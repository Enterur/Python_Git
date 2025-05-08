from tkinter import *

btnList = [None] * 9
fnameList = ["apple.gif", "bear.gif", "cat.gif", "dog.gif", "earth.gif",
             "sheep.gif", "sun1.gif", "sun2.gif", "wolf.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\Window_programming(week9)\\" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70 #버튼 하나 크기가 70
    xPos = 0
    yPos += 70

window.mainloop()