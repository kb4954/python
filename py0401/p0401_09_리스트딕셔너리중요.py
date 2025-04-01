# zip() -> 2개 리스트를 합치는 것 -> list 타입 변경, dict 타입 변경 가능
n_list = ['홍길동','유관순','이순신','강감찬','김구']
t_list = [100,99,89,79,100]
a_list = [10.0,9.0,8.0,7.0,10.0]
# 3개의 리스트는 list 타입은 가능함. 근데 dict타입은 불가능

print(list(zip(n_list,t_list))) # 출력 : [('홍길동', 100), ('유관순', 99), ('이순신', 89), ('강감찬', 79), ('김구', 100)]
[
    ['홍길동',100], 
    ['유관순',99], 
]
print(dict(zip(n_list,t_list)))
# tupple은 수정할 수 없음!
# tupple_list = list(zip(n_list,t_list)) # zip으로 하면 두개의 리스트를 묶어서 전달 가능 tupple은 dic과 유사
# tupple은 []라고 보면 됨.
# zip 자체로는 출력이 안되지만 튜플이나 딕셔너리로 가능 둘다가능한데 딕셔너리로 하면 더 좋음 왜냐면 튜플은 수정이 안되니까

# students = {"no":1,"name":"홍길동","kor":100}
# dic = {1,3,4,5,6,1}
# for key,value in students.items(): # 반드시 items로 해야 key값이 넘어옴!!!
#     print(f"{key} : {value}")
    
# # 2개의 리스트를 출력할 수 있음
# n_list = ['홍길동','유관순','이순신','강감찬','김구']
# t_list = [100,99,89,79,100]
# for n,t in zip(n_list,t_list):
#     print(f"{n} : {t}")


# 리스트 내포: if 조건절 넣을 수 있음
# n_list = [i for i in range(1,51)if i%3==0]
# print(n_list)

# list = [1,2,3,4,5]
# # list +100*100
# # list2 = ['10,100','10,200','10,300','10,400','10,500']

# # format함수 천단위 표시(암기 중요)
# list2 = ["{:,d}".format((i+100)*100) for i in list] # :,d에서 쉼표는 무조건 천단위로 지정
# print(list2)

# list2 = [i for i in list]
# print(list2)

#-------------------------------------------------------
# # set -> 중복을 제거해서 키를 확인
# # 어떤 데이터를 합칠때 사용

# myset1 = {1,2,2,3,3,3,5,5,7}
# print(myset1)

# menu_list = ['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']
# print(set(menu_list)) # list 타입을 set타입으로 변경해서 확인


# 스택(stack): 한 쪽 끝이 막혀 먼저 들어간 것이 가장 나중에 나오는 형태의 자료구조

# 






