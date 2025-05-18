inFp = None
inStr = ""

# 읽기용 = open("파일명", "r")/쓰기용 = open("파일명", "w")
inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\10-week_Practice\\FileTest\\data1.txt", "r", encoding = "UTF-8")

inStr = inFp.readline() # 위의 open한 .txt 파일 한 행 씩 읽기
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close() #open한 파일 close