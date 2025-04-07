class Student:
    
    phone = "" # 인스턴스 변수 - 객체변수: 각각의 객체별로 사용되는 변수
    address = ""
    count = 1 # 클래스변수 사용 - 모든 객체가 공용으로 사용되는 변수
    
    def __init__(self,name,kor,eng,math):
        self.no = Student.count # 클래스 변수
        Student.count += 1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        
    def s_total(self):
        self.total = self.kor+self.eng+self.math
        
    def s_avg(self):
        self.avg = self.total/3
        
    def s_print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank)
        
        
# 객체선언 변수 = 생성자호출
# 객체를 선언할때 만들어지는 변수 : 인스턴스 변수
# def함수와 겹치지 않게 밖에 나와서 작성하기
# no 번호를 부여하지 않음. 그러나 1로 나옴
s = Student("홍길동",100,100,99)
s.s_print()
# print("학생 : ",s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
# no 번호를 부여하지 않음. 그러나 2로 나옴
s2 = Student("유관순",90,90,91)
s2.s_print()
s3 = Student("이순신",80,80,88) # 3번 부여
s3.s_print()

s.kor = 50
s.s_total()
s.s_avg()

# print("학생 : ",s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
    
no = 0
name = ""
kor = 0
eng = 0
math = 0
total = 0
avg = 0.0
rank = 0
# # 무조건 앞에 self 를 써야지 클래스 내에있는 함수임을 표현할 수 있음
# def total(self,kor,eng,math):
#     self.total = self.kor + self.eng+ self.math
    
# def avg(self):
#     self.total/3

# 상속: 기존 클래스에 있는 필드와 메서드를 그대로 물려받는 새로운 클래스를 받는 것, 거의 안쓰고 버전 변경을 할때나 사용.
# 기존 클래스를 변경하면 상속을 받고 있는 모든 클래스가 다 바뀜

    
    