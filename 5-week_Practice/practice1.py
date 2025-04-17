a = ['ronaldo', 'messi', 'zlatan', 'neymar', 'suarez', 'hazard']
print(a[2])
print(a)
a[4] = 'ramos'
print(a)
print(a[1:4]) #슬라이싱 index~index-1
print(a[4:])
print(a[:2])
print(type(a)) #'list' class

b = [5, 6, 7, 8]
c = [1, 2, 3, 4]
print(b + c)
b.append(9) #list 끝에 요소 추가
print(b)
print(b.index(6)) #list에서 데이터와 일치한 요소 index/일치하는 요소 없으면 error
c.insert(0, 0) #데이터를 list에 index에 삽입
print(c)
print(len(b + c)) #list의 길이

d = [10, 2, 5]
d.extend([7, 3]) #list에 list 합침
print(d)
d.remove(7) #입력 데이터를 list에서 삭제
print(d)
d.pop() #list내 요소 뒤부터 제거
print(d)
d.pop(0) #list내 제거하고자 하는 요소의 index 입력 
print(d)
print(d.count(2)) #list 내 데이터와 일치한 요소의 갯수
print(d.count(4))

e = [4, 5, 7, 1, 2]
e.reverse() #list 요소 반대
print(e)
e.sort() #list 오름차순
print(e)
e.sort(reverse = True) #list 내림차순
print(e)