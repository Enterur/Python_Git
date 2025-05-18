import os

inFp = None
fname, inList, inStr = "", [], ""

fname = input("파일명을 입력하세요: ")

if os.path.exists(fname): # os 모듈에 주어진 경로가 존재하는 지 파악
    inFp = open(fname, "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end = "")

    inFp.close()
else:
    print("%s 파일이 없습니다."% fname)