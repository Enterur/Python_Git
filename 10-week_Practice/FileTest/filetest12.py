from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, "rb")

    for i in range(0, XSIZE):
        tmpList = [] # tmpList를 비움
        for k in range(0, YSIZE): # 1byte씩 256번 읽어 tmpList에 저장
            data = int(ord(fp.read(1))) 
            tmpList.append(data)
        inImage.append(tmpList) # inImage에 256크기의 1차의 list를 inImage에 저장
    
    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, width = XSIZE, height = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

filename = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\10-week_Practice\\FileTest\\Citrus.raw"
loadImage(filename) # loadImage함수에 파일명을 전달해  imImage 리스트에 불러들임

displayImage(inImage) # imImage 리스트를 전달해 window창에 출력

canvas.pack()
window.mainloop()