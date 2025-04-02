i_list = [1,2,3,4,5,1,2,10]
dic ={"no":1,"name":"홍길동","kor":100,"eng":100,"math":80,"total":270}
print(dic)

txt_list = ['안녕','반가워','다음','내일','봐','잘','지내','봐요']

#-------------------------
# 얕은복사, 깊은복사
new_list = i_list # 얕은 복사 new_list 내의 값을 바꾸면 i_list 값도 같이 바뀌게됨. 그래서 안됨.
new_list2 = [*i_list] # 깊은복사 이런식으로 복사를 해야 i_list 내의 값이 안바뀜 근데 그럼 복사하는 이유가,.??

# # zip
# for i,t in zip(i_list,txt_list):
#     print(i,t)
# # 1 안녕
# # 2 반가워
# # 3 다음
# # 4 내일
# # 5 봐

# # zip 사용해서 list 생성
# new_list = list(zip(i_list,txt_list))
# print(new_list)
# # [(1, '안녕'), (2, '반가워'), (3, '다음'), (4, '내일'), (5, '봐')]

# # zip 사용해서 dict생성
# new_dic = dict(zip(i_list,txt_list)) # 앞(i_list)에는 키값 뒤에는 벨류값
# print(new_dic)


# 리스트 내포
# 1-10까지 리스트 생성
# a_list = [i+1 for i in range(10)]
# print(a_list)

# b_list = [0]*10
# print(b_list) # append로 추가하는 것보다 리스트를 만들어놓고 추가하는게 더 빠르다

# c_list = [i for i in range(1,51) if i%2==1] # 맨앞에 있는 i가 리턴값/ 결과값
# print(c_list)




# 딕셔너리 전체출력
# for k in dic: # dic에 있는 모든 key값을 불러옴
#     print(dic[k])

# for k,v in dic.items(): # key, value 동시출력
#     print(k,v)

# # 리스트전체출력
# for i in list:
#     print(list)
    
# (이건 복습 아님) 딕셔너리 정렬
# import operator
# dic_sort = sorted(dic.items(),key=operator.itemgetter(0))
# # [('eng', 100), ('kor', 100), ('math', 80), ('name', '홍길동'), ('no', 1), ('total', 270)]
# # 키의 순서대로 정렬해줌
# print(dic_sort)

# # 리스트정렬
# # list.sort() # 리스트 순차정렬
# # print(list)
# list.sort(reverse=True) # 리스트역순정렬
# print(list)


# 딕셔너리 keys, values
# print(dic.keys()) # key 출력
# print(dic.values()) # value 출력
# print(dic.items()) # key, value를 함께 출력 - 튜플형태

# if 'no' in dic: # 딕셔너리를 비교할때 key를 가지고 비교하게 함.
#     print("있습니다.")
    
    
# # 딕셔너리 개별출력
# print(dic['no'])
# # print(dic['kor']) # 키가 없는 것을 출력할때 에러
# print(dic.get('kor')) # get()함수 사용시 없는 키는 None 출력

# 리스트 개별출력
# print(list[0])

# # 딕셔너리 수정
# dic['name'] = "유관순"
# print(dic)

# # 리스트수정
# list[0] =100
# print(list)

# #리스트 삭제
# del list[0]
# print(list)

# # 딕셔너리 삭제
# del dic["no"]
# print(dic)

# # 딕셔너리 추가
# dic['kor'] = 100
# print(dic)

# list.append(100)
# print(list)

