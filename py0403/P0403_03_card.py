# 카드 모양 SPADE-4, DIAMOND-3, HAERT-2, CLOVER-1
# 번호 1,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K

# 카드 1장 -카드 모양, 번호
# 카드모양 4개
# 번호는 13개
# 카드총개수 52장

# 리스트 -딕셔너리
cList = [
{"shape": "SPADE","no":1},
{"shape": "SPADE","no":2}
]

import random
cList = []
sh = ["CLOVER", "HEART","DIAMOND" , "SPADE"]
no = ["","A",'2','3','4','5','6','7','8','9','10','J','Q','K']

# 카드생성
for i in range(52):
    cList.append({"shape":i//13,"no": i%13+1})
    # cList.append({"shape":cShape[i//13],"no": i%13+1})
# 카드 랜덤으로 섞기
random.shuffle(cList)

# my card, youcard
# 5장을 입력(5장을나눠줌)
myCard = []
youCard = []

# 카드 5장씩 배분

for i in range(5):
    myCard.append(cList[i])
    
for i in range(5,10):
    youCard.append(cList[i])

# 내 카드출력 - 번호에 해당되는 글자를 출력
print("[ 내 카드 ]")
for i in myCard:
    print(f"[{sh[i['shape']]},{no[i['no']]}]")
    # print(i['shape'],no[i['no']])


# 내카드, 상대카드를 비교해서 - 승리, 패배, 무승부
# 숫자만 비교해서 숫자가 높은 카드 - 승리
# 0,0 1,1 2,2 3,3
# score = {"myWin":0, "youWin":0,"draw":0}
# for i in range(5):
#     if myCard[i]['no'] > youCard[i]['no']:
#         score['myWin']+1
#     elif myCard[i]['no'] < youCard[i]['no']:
#         score['youWin'] += 1
#     else:
#         score['draw'] += 1

# print("[ 카드 승부 확인 ]")
# print(f"승리: {score['myWin']}, 패배:{score['youWin']}, 무승부: {score['draw']}")
print()
# 상대카드 출력
print("[ 상대카드 ]")
for i in youCard:
    print(f"[{sh[i['shape']]},{no[i['no']]}]") 
    
    
    
score = [0,0,0,0,0] # [2,1,2,2,0]
for i in range(5):
    if myCard[i]['no'] > youCard[i]['no']:
        score[i]=2
    elif myCard[i]['no'] < youCard[i]['no']:
        score[i]= 1
    else:
        score[i] += 0
        
print(f"승리: {score.count(2)}, 패배:{score.count(1)}, 무승부: {score.count(0)}")

print("[ 승리 카드 ]")
for i,c in enumerate(myCard):
    if score[1] == 2:
        print(f"[{sh[c['shape']]}, {no[c['no']]}]",end=",")
        
# 11-J, 12-Q, 13-K, 1-A로 출력이 됐음 좋겠댜
# 전체 카드 출력
# for c in cList:
#     print(c['shape'],c['no'])
    


# import math
# import random

# # 0.0000000000000000 <= x <1.00000000000000000
# # 평균적으로 소수점 16개로 나옴
# print(random.random())

# # 1-45가지 숫자 중 1개를 랜덤으로 추출
# print(random.randint(1,45))

# # 리스트에서 1개 랜덤추출
# a_list = [1,2,3,4]
# print(random.choice(a_list))

# # 리스트에서 개수만큼 랜덤추출 - 중복없이(강조)
# print(random.sample(a_list,2))

# # 리스트를 랜덤으로 섞기 - 리스트 순서를 랜덤으로 섞기
# random.shuffle(a_list)
# print(a_list)
 


# a = 3.141592
# b = 3.51582
# # a 에서 소수점 3자리에서 올림해서 2자리까지 표시해서 출력하시오.
# # a * 100/100

# # a * 100 = 314.1592
# # math.ceil(a*100)/100 #3.15

# # b 에서 소수점 5자리에서 ceil올림해서 4자리까지 표시해서 출력하시오.
# # b * 10000 = 35159.2
# # math.ceil(b*10000)/10000

# print((math.ceil(b*10000)/10000))


# # math 안에 있는 함수를 출력
# print(dir(math))


# # ## 올림
# # print(math.ceil(a)) # 4

# # # 반올림
# # print(round(a)) # 3
# # print(round(b,3)) # 3.516 b옆에있는 3은 셋째짜리에서 반올림하라는 뜻
# # print(round(a,4)) # 3.1416 4자리까지 표시

# # # 버림
# # print(math.floor(a)) #3
# # print(math.floor(b)) #3

