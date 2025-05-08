from tkinter import *
from tkinter import messagebox

#event:user 행동이나 시스템 신호/bind:이벤트가 발생 시 어떤 함수(동작)를 실행할지 연결해주는 메서드
def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")

window = Tk()

window.bind("<Button-1>", clickLeft)

window.mainloop()