# 1-100까지 랜덤숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.
# 도전 횟수 : 10
# 도전 번호 : [1,2,3,4,5]
# 랜덤번호 : 5

import random
# 1.랜덤숫자 생성
ran_num = random.randint(1,100)
# 2. num list 생성
num = []
# 3. n 변수 생성 
n = 0 
# 4. 10번 for문생성
# 5. 입력한 숫자, num list에 저장
# 6. 정답비교
for n in range(1,11):
    in_num = int(input("숫자를 입력하세요.>> "))
    num.append(in_num)
    if ran_num == in_num:
        print("정답입니다. 랜덤숫자 : {}".format(ran_num))
        break
    else:
        print("오답입니다 다시 입력하세요. 입력숫자: {}".format(in_num))
        
# 7. 데이터 출력         
print("도전횟수 : {}".format(n))
print("도전번호 : {}".format(num))
print("랜덤번호 : {}".format(ran_num))





