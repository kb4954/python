# 카드 프로그램 - card 객체
import random

shape = ["CLOVER","HEART","DIAMOND","SPADE"]
number = ["","A","2","3","4",'5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self,number,shape):
        self.number = number
        self.shape = shape
        
    def __str__(self):
        return f"{self.number},{self.shape}"
    # self.shape
    # self.number
    # __str__
    pass
class CardFunc:
    # 함수 사용
    pass

class MyCard:
    def __inti__(self):
        self.mycard = []
        

# cardMain.py
# 카드리스트 호출
# 카드객체 호출 45장을 만들어서 리스트에 추가하고
# 각각 5장을 나눠준다음, 비교해서 큰 수가 승리하는 형태로 구현



 
    
