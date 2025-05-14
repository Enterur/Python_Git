inFp = None
fname, inList, inStr = "", [], ""

fname = input("파일명을 입력하세요: ")
inFp = open(fname, "r")

inList = inFp.readlines()

for inStr in inList:
    print(inStr, end = "")

inFp.close()