a = 10
a_list = [1,2,3,4,5]

print("a : ",a)
a_list[0] = 100
print("a_list :",a_list) # [100,2,3,4,5]

# a변수와 b변수는 다른 변수임.
b = a # a에 b값을 넣었지만 변화없음
b = 1000
print("a: ",a) # 10
print("b: ",b) # 1000

# (매우 중요) 새롭게 복사 : 깊은 복사.  리스트 자체는 별도(*) 복사해야함 
a_list = [1,2,3,4,5]
b_list = [*a_list]
b_list[1] = 200
print(a_list)
print(b_list)


# 주소값 복사 : 얕은 복사
# a_list, b_list 다른 리스트인가?? : 아님.
# a_list = [1,2,3,4,5]
# b_list = a_list
# b_list[1] = 200

# print(a_list) # [100, 200, 3, 4, 5] b_list의 값을 변환했는데 a_list의 값이 바뀜. 이ㄴ







# a_list = [1,2,3,4,5]
# sum = 0
# for i in a_list:
#     sum = sum + i
# print(sum)

# 구구단
# 2 X 1 = 2  i X j
# for i in range(2,10):
#         print("[ {} 단 ]".format(i))
#         print() # 줄의 위치는 상관 없음. 들여쓰기 tap의 위치에 따라 한줄 띄는 위치가 달라짐.
#         for j in range(1,10):
#             print("{} X {} = {}".format(i,j,i*j))
               