class Car:
    color = ""
    speed = 0

    def __init__(self, value1, value2): # 생성자에서 parameter 2개 받도록 설정
        self.color = value1
        self.speed = value2

myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 100)

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))