i = "inch"
c = "cm"

inch = float(input("몇 인치인지 입력하시오:"))
cm = inch * 2.54

print("인치: %.7f %s" %(inch, i))
print("센티미터: %.7f %s입니다." %(cm, c))