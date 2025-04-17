print('수를 입력하세요: ')
a = int(input())

if  a == 0:
    print('0은 나눗셈에 이용 불가능')
else:
    print('3 /', a, ' = ', 3/a)

import sys

print('수를 입력하세요: ')
a = int(input())

if  a == 0:
    print('0은 나눗셈에 이용 불가능')
    sys.exit()

print('3 /', a, ' = ', 3/a)

print('수를 입력하세요: ')
a = int(input())

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수')
elif a > 10 and a % 2 != 0:
    print('10보다 큰 홀수')
elif a % 2 == 0:
    print('10 이하의 짝수')
else:
    print('10 이하의 홀수')