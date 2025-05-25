class Car:
    color = ""
    speed = 0

# __init__ 사용해 프로그램 작성 시 이 이름을 사용해 새로운 함수, 변수명 설정X
    def __init__(self): # 생성자 메서드가 16~17행에서 자동으로 초기화
        self.color = "빨강"
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar2 = Car()

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))