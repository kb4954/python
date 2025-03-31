# (중요)삭제 de1, pop, remove, clear
a_list = [1,2,3,4,5]
del a_list[2]
print(a_list) # [1, 2, 4, 5] 위치값 삭제

a_list.pop() # 맨뒤삭제, 특정위치 삭제
print(a_list)

a_list.remove(1) # 위치값이 아니라 데이터값 삭제
print(a_list)

a_list.clear() # 전체삭제
print(a_list)

# 리스트 - 리스트에 .append로 추가하는 방법
# a_list = []
# for i in range(1,11):
#     a_list.append(i)
 
# 총 추가하는 방법은 3가지
# append,insert,extend
# a_list = [1,2,3]
# a_list.append(4) # list 마지막에 추가하는 방법
# print(a_list) # [1, 2, 3, 4]

# a_list.insert(1,100) #1이라는 위치에 100을 넣으라는 명령어. 잘안씀 효율떨어짐
# print(a_list) # [1, 100, 2, 3, 4]

# a_list.extend([100,200,300]) # 다른 리스트를 추가하는 방법
# print(a_list) # [1, 100, 2, 3, 4, 100, 200, 300]

# 리스트 내포로 더 빠른 방법(파이썬에만 있는 방법)
# a_list = [i+1 for i in range(1,11)]
# print(a_list)
    
# print(a_list)

# (중요)index 번호를 넣으려면 enumerate를 사용 
# a_list = [273,10,5,9,100,1000,50]
# for idx,value in enumerate (a_list):
#     print(f"{idx+1} : {value}")
    
    
    
    
    


