class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no = no
        self.__name = name
        self.__kor = kor # __ : 언더바2개 private하게 접근제한 -> 캡슐화라고 함
        self.__eng = eng
    def getNo(self): return self.__no
    def getNamee(self):
        return self.__name
    # @어노테이션 @property, @ 변수 ,setter - getter,setter  만들어짐.
    # @property # 이 형태로 하면 setter가 됨. # print(Stu.kor())
    # def getKor(self):
    #     return self.__kor
    
    # @kor.setter  # s.kor = 90 s.kor =150 # raise 에러
    # def kor(self.kor):
    #     self.__kor = kor
    #     if kor>=0 and kor<=100:
    #             self.__kor = kor  
    #     else:
    #         raise NotImplementedError("유효한값이 아닙니다.")
    
    # setter    
    def SetKor(self,kor):
        pass
        
        
    def getEng(self):
        return self.__eng
    def setEng(self,eng):
        if eng>=0 and eng<=100:
            self.__eng = eng
        else: raise NotImplementedError("유효한 데이터가 아닙니다.")
    
    
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}"
        
s = Stu(1,"홍길동",100,99)
s.__kor = 200
print(s.__no,s.__name,s.__kor) # 지역변수개념의 s.__kor 값 출력
s.eng = 300
s.Setkor(500)

print(s) # 1,홍길동,100,300 __를 넣은 kor는 값이 100으로 안바뀌고 eng는 바뀜 근데 Setkor로 했을때는 kor도 바뀜
