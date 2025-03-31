import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]
        

print("             좌표맞추기 프로그램")
print("-"*45)
print("*    ㅣ",end="\t")
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
            
            
    a_list[num2][num1] = "X"
    print()    
