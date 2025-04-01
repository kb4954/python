# 1차원 리스트
import random
s_list = [i for i in range(1,26)] # 1차원 리스트 생성
# s_list = [i+1 for i in range(25)] 위에랑 동일한 방식
random.shuffle(s_list)
# random.random(), random.randint(), random.sample(),random.shuffle()


# 2차원 리스트
my_list = [[0]*5 for _ in range(5)] # 2차원 리스트 생성, _를 적어도 되는데 아무것도, 아무런 변수도 안받겠다라는 뜻임
# my_list[0][1] = 1 # 값을 변경하는 방법


# 1차원 리스트 값 -> 2차원리스트 입력
for i in range(5):
    for j in range(5):
        my_list[i][j] = s_list[5*i+j] # [5*i+j] 5x+y와 같은 공식임
# 화면 출력
while True:
    print(" "*10,end="\t")
    print("[ 좌표 맞추기 프로그램 ]")
    print("-"*45)
    print("*  ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5): # 2차원 리스트 채우기
        print(f"{i}  ㅣ",end="\t") # 세로줄
        for j in range(5):
            print(my_list[i][j],end="\t")
        print() # 다섯개를 찍고나서 출력
    print("-"*45)
    # --------------------------------------------여기까지는 동일!!        
    # 좌표입력
    # x = int(input("X좌표를 입력하세요.>> "))
    # y = int(input("Y좌표를 입력하세요.>> "))

    # my_list[y][x] = "X"
    # 혹은 num1 = int(input("X좌표 : "))
    # num2 = int(input("y좌표 : "))
    # my_list[num1][num2] = "X"
    
    
    #여기서 숫자를 쳤을때 x표시가 나타나게끔 변경하고 싶을때ㅣ
    num = int(input("1-25까지 번호를 입력하시오.>> "))
    # 내가 입력한 번호랑 25개 모두 비교-> for문 2번 돌아야함
    stop = 0
    for i in range(5):
        for j in range(5):
            if my_list[i][j] == num:
                my_list[i][j] = "X" # my_list[i][j] i,j위치에 있는 값을 말해줌
                stop = 1
                break
        if stop == 1: break
    print()
    
   
     









