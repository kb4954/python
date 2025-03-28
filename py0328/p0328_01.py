# 변수에 대한 타입 설명
# 파이썬 타입
# bool 타입, 숫자 - int 타입, float 타입, str 타입

# bool 타입 - True, False
# int타입 - 정수형 타입 : 소수점 없음
# float타입 - 실수형 타입 : 소수점 있음. 더 넓음 범위 정수도 표현 가능
# str타입 - 문자열 타입 : "",''안에 입력을 해야함. 
# if True:
#     print("참입니다.")

if 10>3:
    print("정상")
else:
    print("거짓입니다.")

print(1+2)
print(1+1.2)

# print("안녕"+1)
print("안녕",1)
print("숫자 : {:.2f}".format(10/3))
    
# 타입변경 문자열 -> 숫자형태 일 경우
# print(int("안녕1")) # 숫자형태 문자열만 숫자타입으로 변경가능
print(int("1")) # str타입 ""안에는 다 문자열로 취급

print(int(1.5)) # 실수형 -> 정수형으로 타입변경 : 소수점이 사라짐.
# print(int("1.5")) # 에러남 문자열 float타입을 가지고 숫자형 int타입으로 못바꿈  
print(float("1.5")) # 가능

print(str(1.5)) # 문자열타입 변경

#-------------------------------------------------------------------------------
# 변수
a = 10 # = : 할당의 의미, 같다는 의미 아님 같다는 ==
a = 5  # int타입
b = 1.5 # float타입으로 변수가 변함
c = "안녕" # str타입

# print(c+a) # 에러, str타입 + int타입 더하기 연산은 불가능
print(a+b) # int타입 + Float타입 더하기 가능 (숫자)

# list 타입 *매우중요* 많이 사용: 기본적으로 전송해야하는 데이터가 많기 때문!
# list_a =[1,2,3,4]
# print(list_a)
# print(list_a[0]+list_a[1]+list_a[2]+list_a[3])

# input() : 데이터를 입력받는 명령어 - 무조건 str 타입 1개뿐!!
# score = input("데이터를 입력하세요.>> ")
# print("입력데이터 : ",score)

## 두수를 입력받아 합계, 평균을 출력하시오. 타입체크
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print(num1+num2) 


# 조건문
# score = int(input("점수를 입력하세요.>> "))
# if score>=60:
#     print("합격")
# else:
#     print("불합격")

# score = int(input("점수를 입력하세요.>> "))

# if score>=70:
#     print("합격")
# elif score>=60:
#     print("재시험")
# else:
#     print("불합격")
    
score = int(input("점수를 입력하세요.>> "))
# 90점 이상 A,B,C,D,F 출력하시오.
if score>=90: print("A")
elif score>=80: print("B")
elif score>=70: print("C")
elif score>=60: print("D")
else: print("F")
    
    
    
    
