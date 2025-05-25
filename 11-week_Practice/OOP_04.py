class Car:
    name = ""
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

# 두 메서드가 자동차의 이름, 속도를 반환함
    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

car1, car2, = None, None
car1 = Car("아우디", 0)
car2 = Car("벤츠", 30)

# 필드의 사용없이 메서드로 값 출력
print("%s의 현재 속도는 %d입니다."% (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다."% (car2.getName(), car2.getSpeed()))