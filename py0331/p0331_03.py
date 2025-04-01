# 5x5 리스트 - 0으로 초기화
sample_list = [[0]*5 for i in range(5)]
print(sample_list)


# 5x5 리스트 - 0으로 초기화
sample_list = list() #list 초기화 변수를 0이라고 하는것과 같음
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0) # [0,0,0,0,0]
    sample_list.append(temp) #[[0,0,0,0,0]]

print(sample_list)



# a_list =[i+1 for i in range(25)]
# [1,2,3,4.....23,24,25]
# 위의 리스트를 아래처럼 바꾸고 싶을때
# a_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25] # 젤 마지막에 , 없음
#     ]

# import random
# # 1. 순차적 리스트 생성
# sample_list=[i+1 for i in range(25)]
# # 2. 리스트 섞기
# random.shuffle(sample_list) # 랜덤리스트 - 리스트의 숫자가 랜덤으로 섞음.
# # 3. 2차원 초기화 리스트 생성
# a_list = [[0]*5 for i in range(5)] # 깊은복사
# # 4. 2차원 리스트에 랜덤리스트의 값을 입력
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = sample_list[5*i+j] # 랜덤숫자가 들어감
# # print(a_list)

# # 5X5 리스트 출력
# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j],end="\t")
#     print()




# # 5X5리스트 초기화
# a_list = [[0]*5]*5 # 얕은 복사
# a_list = [[0]*5 for i in range(5)] # 깊은복사
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = 5*i+(j+1) # 1,2,3,4.....23,24,25
# print(a_list)



# # 1-25
# import random
# a_list = [i+1 for i in range(25)]
# random.shuffle(a_list)
# # 랜덤으로 섞여진 리스트 출력
# print(a_list)


# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 출력하시오 . 
# a_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25] # 젤 마지막에 , 없음
#     ]

# print(a_list)

#  for i in range(5): # 0,1,2
#     for j in range(5): # 0,1,2
#         print(a_list[i][j],end="\t")
#     print()


# a_list = [
#     [1,2,3], # [0][0],[0][1],[0][2]
#     [4,5,6], # [1][0],[1][1],[1][2]
#     [7,8,9]  # [2][0],[2][1],[2][2]
# ]

# for i in range(3): # 0,1,2
#     for j in range(3): # 0,1,2
#         print(a_list[i][j],end="\t")
#     print()
    
    
# # 1차원 리스트
# aa = [10,20,30] 
# print(aa[0]) # 10

# # (중요)2차원 리스트
# aa = [
#     [1,2,3,4], # 0번째
#     [5,6,7,8], # 1번째
#     [9,10,11,12] # 2번째
# ]
# print(aa[0]) # [1,2,3,4]
# print(aa[0][0]) # 1


# # 리스트값 변환
# a_list = [1,2,3,4,5,6,7,8,9]
# a_list[5] = 10
# print(a_list)

# # 값을 변경할때 1:2, 2의 위치값이 포함, 출력할때는 그 앞에까지만 출력되므로 좀 다름
# a_list[1:2] = [100,200]
# print(a_list)

# 역순출력
# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list[::-1])



# for i in range(10):
#     if i%2==0:continue
#     print(i)

# 모양출력
# for i in range(10):
#     for j in range(i): # 0,1,2,3,4,5,6,7,8,9
#          print("*",end="")
#     print()
    


# continue, break, pass
# 1-10까지 진행을 하는데, 1,2,3-continue : 3번은 제외하고 4,5,6,7,8,9,10까지 진행함
# break - 반복문 완전 중지 1-10까지 진행을 하는데, 1,2,3-break 반복문 끝
# pass 1-10까지 진행을 하는데, 1,2,3-pass, 4,5,6,7,8,9,10  무조건 10번 실행함.

# 입력한 숫자의 합이 50을 넘으면 프로그램을 종료하고
# 총합을 구하시오.
# 입력한 숫자중 5의 배수는 제외시킬것. 제외시킬때 쓰는 명령어: continue

# sum = 0
# while True:
#     if sum<50:
#         num = int(input("숫자를 입력하시오.>>"))
#         if num%5==0:
#             print(f"입력한 숫자 : {num}, 5의 배수는 제외!")
#             continue # 실행을 1번 중지하고 안 합쳐지며, 다시 for문 실행함 
#                      #pass는 다음걸 계속 진행하고 실행할 구문이 없음, for문을 계속 반복
#         sum = sum+num
#     else:
#         break
    

# print(f"합계: {sum}")
# 반복문 - for, while

# 1-100까지의 숫자의 합을 구할때 합계가 200을 넘을때 숫자를 출력하시오.
# 1+2+3+4+....200이 넘는 위치값과 합계를 출력하시오.
# break
# a_list = [i+1 for i in range(100)]
# sum = 0
# i = 0
# for i in a_list:
#     sum = sum +i
#     if sum>=200:
#         print("합계 : ",sum)
#         break
        
# print("i가 {}일때 합계 {}".format(i,sum))        
# print("i 이전 : {}, 합계 {}".format(i-1,sum-i))
# 200 이전의 값

# 1-100까지 리스트 생성
# a_list = [i+1 for i in range(100)]
# print(a_list)

# a_list 홀수의 합계를 구하시오.
# sum = 0 # 변수 sum 선언
# for i in a_list:
#     if i%2==1:  # 홀수이면
#         sum = sum +i # i의 값을 합계변수에 더함.
        
# print("홀수합계 : ",sum)
    


# random.random()함수 : 0<=x<1 사이의 랜덤실수를 가져옴.
# import random
# print(random.random()) #0.0000000000 <= x < 1.0000000000 java나 c에는 랜덤만 존재
# print(int(random.random()*10)+1) # 1,10
# print(int(random.random()*10)+0) # 0,9

# print(random.randint(1,10))


# import random
# a_list = [i+1 for i in range(45)]
# print(a_list)

# random.shuffle(a_list)
# print(a_list[:6])


# 로또 프로그램
# 6개 랜덤숫자와 입력숫자 6개 출력하시오.
# import random
# lotto = [i+1 for i in range(45)]
# lotto_input=[]
# my_lnput = []

# lotto_input = random.sample(lotto,6) # lotto에서 중복없이 6개 갖고오라는 명령어 : sample 파이썬에만 있음
# for i in range(6):
#     my_list = int(input("숫자를 입력하시오.>> "))
#     my_lnput.append(my_list)
    
# print("로또번호 : {} ".format(lotto_input))
# print("입력숫자 : {} ".format(my_lnput))    

# 10번의 숫자를 입력받아, 합계를 구하시오
# for문, while문
# sum = 0 

# for i in range(10):
#     num = int(input("숫자를 입력하시오.>> "))
#     sum = sum +num
# print(sum)

# while i<10:
#     num = int(input("숫자를 입력하시오.>> "))
#     sum = sum +num

# print("합계 : ",sum)    

# <반복문> 둘다 많이 씀 java,c 같은 방식으로 사용함.
# while 문 조건문 반복 / while True는 무한루프
# i = 0
# while i<10:
#     print(i)
#     i = i+1 # i가 1씩 증가하면서 계속 반복됨.
    
# # for 문
# for i in range(10): # 0~9까지 반복
#     print(i)
    