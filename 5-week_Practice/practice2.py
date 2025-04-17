a = (1, 2, 3, 4, 5, 6) #list와 달리 ()사용
print(a)
print(a[0]) #a[0] = x는 tuple에서 지원하지 않으므로 error
print(a[:2]) #나머지도 list와 같이 len이나 tuple끼리 덧셈 가능
print(a[3:5])
print(type(a))

a_1 = 1, 2, 3 #()없이 ,만 사용 가능
print(a_1)
print(type(a_1))

b_0 = 1
b_1 = 1, #요소가 1개인 경우 뒤에 ,추가
print(b_1) 
print(type(b_0), type(b_1))

c_0 = 4, 6, 7 #패킹:여러 data를 tuple로 묶음
one, two, three = c_0 #언패킹:tuple의 요소를 각 변수에 할당
print(one, two, three) #tuple의 요소와 할당할 변수의 수가 같음
#다른 메소드 index, count도 똑같이 적용 가능