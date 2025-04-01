import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

while True:
    a_list = [[0]*5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            a_list[i][j] = first_list[5*i+j]
            
            print("     [좌표 맞추기 프로그램]")
            print("-"*45)
            print("* ㅣ",end="\t")
        for i in range(5):
            print(f"{i} ㅣ",end="\t")
            for j in range(5):
                print(a_list[i][j],end="\t")
            print()
            
        print("-"*45)            
        num = int(input("1-25번 숫자를 입력하세요.>>"))
        num1 = int(input("X좌료: "))
        num2 = int(input("y좌표: "))
        
        
            
        