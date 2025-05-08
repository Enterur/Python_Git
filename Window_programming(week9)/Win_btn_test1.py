from tkinter import *

window = Tk()

#버튼 위젯 생성 후 command 옵션에 quit 명령
button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button1.pack()

window.mainloop()