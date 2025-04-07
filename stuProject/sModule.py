class Student:
    count = 1
    def __init__(self,no,name,kor,eng,math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1
        
    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
        
class Students:
    def __init__(self):
        self.students = []
        # s = 연속된 학생들을 나타내는 임시변수
    def add(self,s):
        self.students.append(s)
        
    def __str__(self):
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
            return ""
            
            
            
        