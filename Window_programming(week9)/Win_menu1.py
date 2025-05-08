from tkinter import *

window = Tk()

mainMenu = Menu(window) #부모윈도(상위 메뉴)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu) #상위 메뉴->[파일] 생성
mainMenu.add_cascade(label = "파일", menu = fileMenu) #cascade로 아래 메뉴 확장
fileMenu.add_command(label = "열기")
fileMenu.add_separator() #메뉴 사이 구분선
fileMenu.add_command(label = "종료")

window.mainloop()