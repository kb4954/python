def cal(*a,b=10): # 가변매개변수, 키워드매개변수 함께 사용 - 매개변수 키워드
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,3,4,5,b=100))

# # 키워드 매개변수 - 키워드변수는 무조건 마지막에 있어야함.
# def cal(a,b=10):
#     return a+b
# print(cal(1))  
  
   
# print(1,2,3,4,5)
# print(1,2)


# 가변매개변수 사용(ex. print)
def cal(*num): # 전개연산자 : 1,2,3,4,5
    result = 0
    for n in num:
        result += n
    return result
print("2개 합계 : ", cal(1,2))
print('3개 합계 : ', cal(10,20,30))
print("4개 합계 : ", cal(20,40,60,80)) # (20,40,60,80)를 리스트 타입으로 num에 넣어주겠따 : 이게 가변매개변수를 사용하는 방법


# def cal(n1,n2):
#     return n1+n2
# def cal2(n1,n2,n3):
#     return n1+n2+n3

# n1 = 10
# n2 = 20
# n3 = 30
# result = cal(n1,n2)
# print(result)
# result2 = cal2(n1,n2,n3)


# # global 변수 : 전역변수
# def func1():
#     global a # 전역변수 호출 global은 파이썬에만 있음
#     a = 20
#     # a = 20 # 지역변수이기에 함수를 벗어나면 사라짐
    
    
    
# a = 10
# print("a: ",a) # a: 10
# func1()
# print("a: ",a)# a : 10



# def cal(ss):
#     ss['kor'] = int(input("수정할 국어점수를 입력하세요.>> "))
#     ss['total'] = ss['kor']+ss['eng']+ss['math']
#     ss['avg'] = ss['total']/3


# print("[ 학생성적 수정] ")
# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

# # 국어점수변경 함수 호출
# cal(s) # 변경된 국어점수 입력됨.
# print("수정된 국어점수: ",s['kor'])
# # 더 간편해짐 아래랑 비교했을때
# #------------------------------------------------



# 매개변수로 일반변수 전달형태 : 리턴으로 값을 돌려줘서 입력을 시켜야됨.
# 국어점수변경 함수 선언
# def cal(kor):
#     kor = int(input("수정할 국어점수를 입력하세요.>> "))
#     return kor # 리턴을 해주지 않으면 무조건 지역변수는 사라지기 때문에 꼭 리턴을 해줘야함!!!!


# print("[ 학생성적 수정] ")
# kor = 100
# eng = 100
# math = 100
# # 국어점수변경 함수 호출
# kor = cal(kor) # cal(kor)에서 함수에서 return을 해준후 kor = cal(kor)로 변경해야 반영이 됨
# print("수정된 국어점수: ",kor)

# def cal(a_list):
#     a_list[0]=100
#     a_list[1]=200



# a_list=[0,0] # 리스트타입변수 : 주소값이라서 주소값이 바껴버림
# a_list[0]=10
# a_list[1]=20
 
# print("함수호출전 a_list: ",a_list[0],a_list[1])

# cal(a_list) #함수호출 b_list = a_list
# print("함수호출후 a_list: ",a_list[0],a_list[1]) # ?.?

#함수선언

# def cal(a,b):
#     a=100 # 지역변수: 함수내 변수는 함수를 벗어나면 사라짐. 근데 완전히 사라지는 것은 일반변수일때만 (int,bool,float,str과 같은것도)
#     b=200


# # 함수밖

# a = 10 # 전역변수
# b = 20
# print("함수호출전 a,b :",a,b) # 출력값: 함수호출전 a,b : 10 20

# # 함수호출
# cal(a,b)
# print("함수호출 후 a,b :",a,b) # 출력값: 함수호출 후 a,b : 10 20

# 이름,국어,영어,수학 점수를 입력바아, 합계,평균을 출력하시오.
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
# ]
# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
    
# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice = int(input("원하는 번호를 입력하세요.>> "))
# if choice == 2:
#     stu_print() # 함수호출



# 지역변수: 한정된 지역에서만 사용 함수내에서 선언되어있는 변수 새로운 저장고를 만들어 저장하게 되어있음. 매개변수가 같더라도 서로 다른값임.
# 함수를 벗어나면 값이 사라짐.
# 전역변수: 프로그램 전체에서 사용 함수밖에서 선언되어 있는 변수

# 함수선언
# def cal(kor,eng,math):
#     total = kor+eng+math
#     avg = total/3
#     return total, avg

# no = 1
# name = input("이름을 입력하세요.>> ")
# kor = int(input("국어점수를 입력하세요.>> "))
# eng = int(input("영어점수를 입력하세요.>> "))
# math = int(input("수학점수를 입력하세요.>> "))
# total,avg = cal(kor,eng,math)
# print("합계: {} , 평균: {:.2f} ".format(total,avg))

# 직사각형 넓이와 길이와 둘레를 구하는 프로그램을 구현하시오.
# 넓이: 가로 *세로, 둘레: 가로길이*2+세로길이 *2

# 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.
# 함수를 사용할 것
# def cal(num1,num2):
#     result1 = num1*num2
#     result2 = num1*2+2*num2
#     return result1,result2
# # 가로,세로 입력
# num1 = int(input("가로의 길이를 입력하시오.>> "))
# num2 = int(input("세로의 길이를 입력하시오.>> "))
# result1,result2 = cal(num1,num2)
# print("넓이 : ",result1, "길이 : ",result2)



# 입력을 5개를 받아, 짝수만 모두 더한값을 출력하시오.

# def cal(n_list):
#     sum=0
#     for n in n_list:
#         if n%2 == 0: sum += n
#     return sum
 
        
# n_list =[0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자입력"))
# result = cal(n_list)
# print("짝수의 합: ",result)


# 함수를 사용해서 두수를 입력받아
# 10-20 입력받으면 10+11+12+13....20 출력하시오.

# def add(n1,n2):# def를 우린 함수라고 부르고, n1,n2는 매개변수라고 생각
#     # 비교
#     if n1>n2:n1,n2 =n2,n1
#     sum = 0
#     for i in range(n1,n2+1):
#         sum = sum + i
#     print("합계: ",sum) # 리턴이 없으면 리턴값을 돌려줄수없음.

# n1 = int(input("숫자를 입력하세요.>> "))
# n2 = int(input("숫자를 입력하세요.>> "))
# # 큰수를 먼저 넣어도 10,2->2,10
# add(n1,n2) # 호출하는쪽 변수는 매개변수라고 해도 상관없음. 근데 인수라고도 함.

# 프로그램 구현 

    



# add() 결과값을 출력하시오.

# 함수사용
# 1. 중복코드가 있을때
# 2. 소스가 너무 복잡할때
# 먼저 프로그램을 모두 구현해놓고, 중복되고 있는지 확인후 함수를 사용

# num1,num2,num3 값을 입력받아, 합계,평균을 구하시오.
# # 함수선언
# def add(kor,eng,math): # 함수에 대한 정의
#     return kor+eng+math # return 값을 돌려줌


# kor = int(input('점수를 입력하세요.>> '))
# eng = int(input('점수를 입력하세요.>> '))
# math = int(input('점수를 입력하세요.>> '))
# total = add(kor,eng,math)
# avg = total/3

# print(kor,eng,math,total,avg)









