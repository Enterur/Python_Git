from tkinter import *

def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("

    txt += str(event.y) + ", " + str(event.x) + ")에서 클릭 됨" #누른 마우스 버튼 + 좌표 값 처리
    label1.configure(text = txt)

window = Tk()
window.geometry("300x300")

label1 = Label(window, text = "이 곳이 바뀜")

window.bind("<Button>", clickMouse) #<Button>-마우스 버튼 공통

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()