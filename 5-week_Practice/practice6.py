print('몇 번 반복할까요?: ')
limit = int(input())

count = 0
while count < limit:
    count += 1
    print('{0}회 반복'.format(count))

print('반복이 종료되었습니다.')

i = 0
while(True):
    i += 1
    if i == 20:
        print('i가 {0}이 됐습니다. 반복문을 중단합니다'.format(i))
        break #루프 중단

    print(i)