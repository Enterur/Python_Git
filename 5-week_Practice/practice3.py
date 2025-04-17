dic = {}
dic['파이썬'] = 'www.python.org'
dic['마이크로소프트'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com' #dictionary 생성

print(dic['파이썬'])
print(dic['마이크로소프트'])
print(dic['애플'])
print(type(dic)) #dictionary class
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items()) #dictionary 메소드

print('파이썬' in dic.keys())
print('www.apple.com' in dic.values())

dic.pop('애플')
print(dic)
dic.clear()
print(dic) #dictionary의 key, value 전체 제거