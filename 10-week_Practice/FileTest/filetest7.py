outFp = None
outStr = ""

outFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\10-week_Practice\\FileTest\\data2.txt", "w")

while True:
    outStr = input("내용 입력: ")
    if outStr != "": # 내용이 비어있지않으면 입력내용을 4행이 파일에 작성
        outFp.writelines(outStr + "\n")
    else: # 비어있으면 10행가서 무한루프 종료
        break

outFp.close()
print("---정상적으로 파일에 씀---")