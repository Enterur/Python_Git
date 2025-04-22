radius = float(input("반지름의 길이를 입력하시오:")) # 간단한 코드, 정확도 낮음
pi = 3.14

print("둘레:", 2 * pi * radius)
print("넓이:f", pi * radius ** 2)

import math # math module import하는 다른 방법/코드 길어짐, 정확도 상슴
r = 'radius'
c = 'circum'
a = 'area'

radius = float(input("반지름을 입력하시오: "))
circum = 2 * math.pi * radius
area = math.pi * radius ** 2

print("둘레: %.8f %s" %(circum, c))
print("넓이: %.8f %s" %(area, a))