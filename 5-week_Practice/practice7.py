for i in ['뇌를', '자극하는', '파이썬']:
    for s in i:
        print(s)

for i in ['뇌를', '자극하는', '파이썬']:
    print(i)

for k in range(0, 7, 2): #시작값, 멈춤값, 연속하는 두수의 차
    print(k)

for k in range(0, 5): #(0, 5) = (5)
    print(k)

for i in range(1, 6):
    for j in range(i):
        print('*', end='')

    print()

for i in range(10):
    if i % 2 == 1:
        continue #i가 홀수인 경우 코드가 실행되지 않고 다음 반복으로 넘어감

    print(i)