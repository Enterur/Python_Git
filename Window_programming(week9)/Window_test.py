from tkinter import * #파이썬에서 GUI 모듈 제공 라이브러리

window = Tk()
window.title("Window창 연습")
window.geometry("350x200")
window.resizable(width = TRUE, height = TRUE) #T, F로 윈도우 창 크기 조절

#mainloop()는 항상 마지막에 호출, 호출 후에는 GUI가 사용자 이벤트에 응답
window.mainloop()