# 두수를 입력받아, 사칙연산(+,-,*,/) 출력하시오.
def cal(x,y):
    print("더하기: ",x+y)
    print("빼기: ",x-y)
    print("곱하기: ",x*y)
    print("나누기: ",x/y)
    return x+y

num1 = int(input("첫번째 숫자를 입력하세요.>> "))
num2 = int(input("두번째 숫자를 입력하세요.>> "))
result1 = cal(num1,num2) # 함수호출

num3 = int(input("첫번째 숫자를 입력하세요.>> "))
num4 = int(input("두번째 숫자를 입력하세요.>> "))
result2 = cal(num3,num4) # 함수호출

num5 = int(input("첫번째 숫자를 입력하세요.>> "))
num6 = int(input("두번째 숫자를 입력하세요.>> "))
result3 = cal(num5,num6) # 함수호출

# 결과중에 합계를 모두 더해서 총 합계를 구하시오.
print("총합계: ",result1+result2+result3)

# def add(x,y):
#     print("a:",x)
#     print("y:",y)
#     print("x+y:",x+y)
    

# # 특정값
# a = 10
# b = 20
# c = 30
# d = 40

# add(a,b)
# add(a,c)
# add(a,d)
# add(c,d)


# # 함수선언
# # 함수명령어 def 뒤에 변수 선언하듯이 선언하면됨.(동사를 많이씀)
# def add():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
    
# print("누군가 오고 있어요")
# print("인사")
# add() # 함수 호출은 def를 빼고 add()만 쓰면 위에있는 부분이 호출됨.

    







# print() # 변수뒤에 ()가 있으면 함수
# # 함수선언
# def cal(x,y):
#     result = x+y
#     print(result)
#     result2 = x-y
#     print(result2)
#     result3 = x*y
#     print(result3)
#     result4 = x/y
#     print(result4)
    
    

# a,b = 10,20
# cal(a,b)
# # result = a+b
# # result2 = a-b
# # result3 = a*b
# # result4 = a/b

# c,d = 100,200
# cal(c,d)
# # r = c+d
# # r2 = c-d
# # r3 = c*d
# # r4 = c/d

# e,f = 50,100
# cal(e,f)
# # k = e+d
# # k2 = e-d
# # k3 = e*d
# # k4 = e/d




