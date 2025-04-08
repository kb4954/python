class Student:
    # 인스턴스 변수 - 객체선언시 각각 변수들이 존재 : 공용으로 사용안됨.
    # no = 1
    # name = "" # 인스턴스 변수
    count = 1 # 클래스변수 - 모든 객체가 공용으로 사용하는 변수
    
    # 생성자함수
    def __init__(self,name,kor,eng,math): # 초기화의 약자
        self.no = Student.count # 인스턴스 변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1
        
    def stu_total(self):
        self.total = self.kor + self.eng +self.math
        # 클래스 내에서 바뀐점수와 바뀌지 않은 점수가합계되는 거임
    def stu_avg(self):
        self.avg = self.total/3
        
    def __str__(self): # 문자열 형태로 숫자도 나올 수 있음!
        return f"{self.no},{self.name},{self.kor},{self.eng},\
    {self.math},{self.total},{self.avg:.2f},{self.rank}" # 특별함수
     
class Students:
    def __init__(self): # self.students가 아닌 이유: 무조건적인 list를 하나 생성할때는 필요없음 / 즉 받을 매개변수가 없기 때문
        self.students = [] # 인스턴스 변수가 됨.
        # 이 객체 안에 students 리스트를 하나 만들자는 의미 
    def add(self,s):
        self.students.append(s)
        

    def __ge__(self,s):
        return(self.total<=s.total)
        
    
    def __ge__(self,s):
        return(self.total>=s.total)
        
    def __eq__(self,s): # 다른객체 1개를 매개변수로 전달받음
        return(self.total == s.total) # True,  다르면 False
        
        
        
        
    def __str__(self): # 리턴이 무조건 문자열을 해줘야함.
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""
        
# ss = Students()
        
# s = Student("홍길동",100,100,99)     
# s2 = Student("유관순",90,90,91)     
# s3 = Student("이순신",80,80,89)     
# ss.add(s)   
# ss.add(s2)   
# ss.add(s3)   
# print(ss)   
        
        
        
    
# # 매개변수가 있는 생성자를 활용해서 데이터 입력
# s = Student("홍길동",100,100,99) # 매개변수가 있는 생성자 객체선언
# print(s.no,s.name,s.kor,s.eng,s.math) # 2
# s2 = Student("유관순",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math) # 3
# print(s.no,s.name,s.kor,s.eng,s.math)# 3
# s3 = Student("이순신",90,90,91)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math) # 4
# print(s.no,s.name,s.kor,s.eng,s.math) # 4


# # 기본생성자를 가지고 값을 넣는 방법
# s = Student() # 기본생성자
# s.no = 1
# s.name = "홍길동"
# print(s.no)
# print(s.name)

# s2 = Student()
# s2.no = 2
# s2.name = "이순신"
# print(s2.no,s2.name)

    
    