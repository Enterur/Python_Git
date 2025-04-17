def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 -> %d" %hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 -> %d" %hap)

def para_func(v1, v2,v3 = 0) :
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 -> %d" %hap)
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 -> %d" %hap)

def para_func(*para) : #*는 포인터가 아니라 가변인자(variadic argument)
    result = 0
    for num in para:
        result += num

    return result

hap = 0

hap = para_func(10, 20) #argument를 tuple로 저장
print("매개변수가 2개인 함수를 호출한 결과 -> %d" %hap)
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 -> %d" %hap)