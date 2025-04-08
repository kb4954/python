# 5*5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호를 넣기

import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]
# 1차원 인덱스 = (행 번호) × (열 개수) + (열 번호) = i * 5 + j

while True:
    print("[ 좌표맞추기 프로그램  ]")
    print("-"*45)
    print("* ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i} ㅣ",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
        
        
        
        
    print("-"*45)
    num = int(input("1-25번 숫자를 입력하세요.>> "))
    
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num: a_list[i][j] = "X"
            print()
            
            
        
        
        
    
    
