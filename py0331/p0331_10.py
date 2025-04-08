import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]
        
while True:
    print("             좌표맞추기 프로그램")
    print("-"*45)


    print("*    ㅣ",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i} ㅣ",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
        
        
        # 여기서부터 입력
    print("-"*45)
    num = int(input("1-25번 숫자를 입력하세요.>> "))
        
        # 좌표에 값 넣기
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num: a_list[i][j] = "X"
            print()
                
        # num1 = int(input("X좌표 : "))
        # num2 = int(input("Y좌표 : "))            
        # a_list[num2][num1] = "X"
        # print()
                    
    
    # x좌표 : 1
# Y좌표 : 3
# 1,3 ->문자인식

# num1 = int(input("X좌표 : "))
# num2 = int(input("Y좌표 : "))
# print(f"[X,Y좌표 : {num1},{num2} ]")


        # num = input("X,Y 좌표 (0/0) : ")    #1,3,5,7
        # n_list = num.split(" ")
        # print(f"[X,Y좌표 : {n_list} ]")
    
    # a_list[num2][num1] = "X"
 
