k = "kg"
p = "lb"

kg = float(input("몇 킬로그램인지 입력하시오:"))
lb = kg * 2.204623

print("킬로그램: %.7f %s" %(kg, k))
print("파운드: %.7f %s입니다." %(lb, p))