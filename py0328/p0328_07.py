# 입력한 숫자를 5벉 반복해서 리스트에 추가하는 프로그램 구현

num_list = []

# 입력한 숫자
# for i in range(10):
#     num = int(input("숫자를 입력하세요.>> "))
#     # num가 num_list에 있는지 확인해서 없으면 입력시키고, 없으면 제외
#     if num not in num_list:
#         num_list.append(num)

i = 0
while i<10:
    num = int(input("{}번째 숫자를 입력하세요.>> ".format(i+1)))
    if num not in num_list:
        num_list.append(num)
        i += 1

print(num_list)

# input_list = [1,5,10,9,8,20]
# a = 5
# if a in input_list: # input_list 안에 a가 있는지 확인, list는 in으로 안에 존재하는지 안하는지 확인할 수 있음
#     print("{}가 존재합니다.".format(a))
# else:
#     print("{}가 존재하지 않습니다.".format(a))
    
# i = 0
# while True:
#     print(i)
#     i += 1

# 반복문 while : 조건이 맞으면 반복을 진행, 조건식이 맞으면 무한 반복 가능
# i = 0
# while i<10:
#     print(i)
#     i += 1 # 1씩 증가
    
# print("-"*50)

# # 반복문 for : 횟수만큼 반복을 진행
# for j in range(10):
#     print(j)