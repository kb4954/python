# 변수 
# 수학 = 같다의미, 프로그래밍 = 할당
# 변수명 규칙
# 대소문자를 구분함
# 변수명 : 특수문자가 올 수 없음. $a, &&bab 안됨.
# 특수문자 : _ 언더바만 가능함. _abc, _num 가능
# 숫자가 제일 앞에 올 수 없음. - 100top, 7up 안됨
# 숫자가 중간에 오는 것은 가능 top100 , up7, a1
# 예약어는 사용불가 True, False, None, and, of, for ...

A = 100
a=10
b=5
true = 100 #True 예약어, true는 가능 근데 잘 안씀 

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 타입 - bool타입 : True, False
aaa = True
bbb = False
ccc = 100

print(aaa)
print(ccc)
ddd = 3.14
print(ddd)
eee="안녕"
print(eee)

print(type(aaa)) # bool 타입
print(type(ccc)) # 숫자 - 정수
print(type(ddd)) # 숫자 - 실수
print(type(eee)) # 문자열

