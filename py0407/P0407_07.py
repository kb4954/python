# 상속 예시

class Car:
    speed = 0
    tire = 4
    door = 5
    def speedUp(self,s):
        self.speed += s
        print("현재 속도 : ",self.speed)
        
class Sedan(Car):
    color = "red"


c = Car()
# print(c.gireType) # 없는 변수 출력시 에러
s = Sedan()
print(s.tire) # Sedan에 없는 변수를 넣어도 출력이 됨 -> 상속이 되었기 때문




