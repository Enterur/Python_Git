inFp = None
inList = ""

inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\10-week_Practice\\FileTest\\data1.txt", "r", encoding = "UTF-8")

inList = inFp.readlines() # readline과 달리 한 번에 읽음
print(inList)

inFp.close()