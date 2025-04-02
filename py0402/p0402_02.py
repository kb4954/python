# #문자열

print('1234'.isdigit()) # 정수인지 확인
print('abc'.isalpha()) # 알파벳인지 아닌지 확인 - 한글안됨.
print('abc123'.isalnum()) # 글자 및 숫자인지 확인 - abc,a1, 123 모두가능
print('abc'.islower()) # 모두 소문자인지 확인
print('ABC'.isupper()) # 모두 대문자인지 확인 

# a = "1234"
# if a.isdigit(): # 숫자로 변환가능
#     print("숫자로 가능합니다.")



# while True:
#     my_input = input("숫자를 입력하세요.>>")    
#     if my_input.isdigit():
#         my_input = int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력하셔야 합니다.")

# my_input = int(input("숫자를 입력하세요.>>")) 
# 이렇게 하지 않는 이유는 사람이 int만 적지 않을수도 있기때문에 다른 문자를 적을 경우 동요가 일어날 수 있음    

# zfill = 문자열 왼쪽 정렬
# map
# score = ['100','99','90']
# # 함수 def cal(매개변수)
# def cal(x):
#     return int(x)*100

# s_list = list(map(cal,score))
# print(s_list)
# # 모든 문자를 숫자로 타입을 바꿔줌.


# sum = 0
# for s in score:
#     sum = sum + int(s)
# print("합계 : ",sum)






# txt = ","
# txt2 = txt.join("안녕하세요") # 안,녕,하,세,요 사이사이에 쉼표
# print(txt2)

# api 공공데이터에서 사용하는것
# csv(문서파일), json, XML
# 원래 XML이었는데 json으로 점점 바뀜
# 문자열

# 데이터베이스(DB)는 리스트를 저장할 수 없음. 따라서 문자열로 저장
# txt = "1/홍길동/100/100/100/300/100.0/1"
# txt_list = txt.split("/") # 쉼표나 슬래시에 따라 글자를 나누고 리스트도 만드는건가 ?
# print(txt_list)
# txt_list[1] = '유관순'
# print(txt_list)

# txt = "a,b,c,d,안녕,반가워"
# # 쉼표를 기준으로 글자를 다 나누고 싶을때
# txt_list = txt.split(",")
# print(txt_list)
# # 출력값 : ['a', 'b', 'c', 'd', '안녕', '반가워']

# txt = "     안녕하  세요   "
# print(txt.replace(" ","")) # 문자를 다른문자로 치환인데 공백있는걸 공백 없는걸로 바꿔줘 이런식으로 사용가능

# txt2 = "파이썬 공부가 쉬워요. 너무 쉬워요. 파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))

# txt3 = "----파이썬 ---"
# print(txt3.strip("-")) # 앞뒤공백제거뿐만 아니라 앞뒤특정글자도 제거 가능
# print(txt3.replace("-","")) 

# print(txt)
# print(txt.strip()) # 앞뒤공백제거: 중간은 제거 안해줌, rstrip(), lstrip() -> 오른쪽 왼쪽 공백제거

# txt = "파이썬 공부가 쉬워요. 너무 쉬워요. 파이썬은 재미있어요."
# print(txt.count("파이썬")) # 문자열의 검색하려고 하는 글자 개수
# print(txt.count("요")) 
# print(txt.find("공부")) # index 번호, 몇번째방에 공부라는 단어가 있는지 알려줌
# print(txt.find("자바")) # 없을때는 -1를 출력함.

# t = "aaa.py"
# print(t.endswith("py")) # 문장의 끝단어가 맞는지 확인해줌 True라고 출력, 아니면 False



# txt = "abBBcDd"       # 대소문자
# print(txt.upper())    # 대문자만 출력
# print(txt.lower())    # 소문자만 출력
# print(txt.swapcase()) # 대문자는 소문자로, 소문자는 대문자로
# print(txt.title())    # 단어 첫글자만 대문자 나머지 다 소문자


# txt = "안녕하세요"
# a_list = [1,2,3,4,5]


# print(a_list[1:3]) # [2, 3] 출력 3번째 앞에꺼까지
# print(txt[1:3])    # 녕하
# print(txt[2:])     # 하세요
# print(txt[:3])     # 안녕하

# print(txt*3)
# print("-"*50) 
# print(len(txt))    # 글자길이

# print(txt[::-1]) # 요세하녕안 글자역순출력

# # 문자열 index 번호 가짐.
# print(txt[1])
# print(a_list[1])













