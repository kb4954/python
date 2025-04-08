# lotto 프로그램
import random

# 랜덤 1-45번까지 숫자 6개 ran_list 저장
# 입력받은 숫자 6개를 my_list에 저장을 시키는 프로그램을 구현하시오.
# 랜덤번호 : 
# 입력번호 :
# 당첨개수 : 
# 당첨번호 :
# 내가 입력한 번호 리스트
my_list = []
# 랜덤 번호 리스트 
i = 0
# 당첨번호 리스트
lotto_list = []
# 당첨 개수
lotto_count = 0
ran_list = random.sample(range(1,46),6)

while i < 6:
    my_input = int(input("{}번째 번호를 입력하세요.>> ".format(i+1)))
    if my_input not in my_list: # 중복입력을 막기위해서씀 내가 입력한 값이 내 리스트에 없으면 
        my_list.append(my_input)
        i += 1
 
# 랜덤 리스트를 확인하고 랜덤 리스트 숫자가 내 리스트에 있다면 당첨개수+1 증가하고 당첨리스트에 내 리스트속 숫자가 등록된다.        
for j in ran_list:
    if j in my_list:
        lotto_count = lotto_count+1
        lotto_list.append(my_list[j])
        
    
print(f"입력번호 : {my_list}")
print(f"랜덤번호 : {ran_list}")
print(f"당첨번호 : {lotto_list}")
print(f"당첨개수 : {lotto_count}")