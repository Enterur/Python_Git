class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(슈퍼 클래스): %d" % self.speed)

class Sedan(Car): # 서브클래스의 upSpeed 메서드 오버라이딩
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

            print("현재 속도(서브 클래스): %d" % self.speed)

class Truck(Car):
    pass # pass:슈퍼클래스의 메서드를 그대로 상속
    
sedan1, truck1, = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ", end = "") # 슈퍼클래스의 메서드로 호출
truck1.upSpeed(200)

print("승용차 --> ", end = "") # 재정의된 메서드로 호출
sedan1.upSpeed(200)