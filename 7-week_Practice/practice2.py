def para_func(*para) : #*는 argument를 tuple로 저장
    result = 0
    for num in para:
        result += num

    return result

hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(hap)

#----------------------함수 구분선---------------------------#

def dic_func (**para): #**는 argument를 dictionary로 묶음
    for k in para.keys(): #키값을 k에 할당
        print('%s -> %d명입니다.' % (k, para[k]))

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)