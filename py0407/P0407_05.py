# # 변수,함수 집합체 - 변수에 대한 그룹핑 kor,eng,math
# # 그룹핑 종류 - list, dict 타입/ 함수까지

# # 입력받을때...처리. 수정할때 ... 직접처리
# # 특정데이터값이 들어왔을때... 잘못된 데이터는 입력이 안되도록 구현
# # -> 따라서 클래스 사용

# # 클래스는 처음에 정의할게 많음. 대신 리스트보다 보안성이 높다



class Car:
    def __init__(self,color,tire,door): # 생성자 : __init__ 100% 사용!
        self.color = color # self.color : Car 변수, color: 요청받은 변수
        self.tire = tire
        self.door = door
        self.speed = 0

# 생성자를 사용한 객체선언                     
c = Car("red",5,4) # 아래내용을 미리 정해진 함수하나만 있으면 한줄로 간결하게 표현가능
# # red, 5, 4
# a2 = Car() # 차를 구매한 후 색칠도 다시하고, 문짝도 달고, 타이어도 달고
# a2.color = "red"
# a2.tire = 5
# a2.dodr = 4

c2 = Car("blue",5,5)           
    
# 속도올리기
def speedUp(self,s):
    self.speed += s
def speedDown(self,s):
    self.speed -= s
    
# # 리스트 선언        
# a_list = [1,2,3,4,5]
# # 리스트 값 입력
# a_list[0] = 90
# # 리스트 출력
# print(a_list)

# # 클래스 객체선언
# a = Car() # 선언한 순간 위의 값이 들어옴.
# # 클래스 변수에 값 입력 - 참조변수.변수명
# a.speed =50 
# # 클래스 변수 값 출력 - 참조변수.변수명
# print(a.speed)


# # 함수 사용 방법 - 참조변수.함수명
# a.speedUp(20)
# print(a.speed)

# a_list2 = [1,2,3,4,5]
# a_list2 = a_list # 얕은복사
# a_list2 = [*a_list]


# a2 = Car() # a와 똑같은게 만들어지지만 서로 다른 변수임 각각의 변수, 함수가 됨.

# 기본형태 객체선언 후 데이터 입력
# # red, 5, 4
# a2 = Car() # 차를 구매한 후 색칠도 다시하고, 문짝도 달고, 타이어도 달고
# a2.color = "red"
# a2.tire = 5
# a2.dodr = 4

# # blue, 5,5
# a3 = Car() 
# a3.color = "blue"
# a3.tire = 5

