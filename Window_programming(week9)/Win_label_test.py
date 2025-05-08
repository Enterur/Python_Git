from tkinter import *

window = Tk()
window.title("Window창 연습")
window.geometry("250x150")
window.resizable(width = FALSE, height = FALSE)

label1 = Label(window, text = "CookBook ~~ Python을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부 중 입니다.", bg = "magenta", width = 20,
               height = 5, anchor = SE)

label1.pack() #.pack() -> widget을 화면에 배치하는 메서드
label2.pack()
label3.pack()

window.mainloop()