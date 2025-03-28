# 숫자 2개를 입력받아, 사칙연산 결과값을 출력하시오. 
# 10 + 5 = 15
# 10 - 5 = 5
# 10* 5 = 50
# 10 / 5 = 2

a = int(input("숫자를 입력하시오. : "))
b = int(input("숫자를 입력하시오. : "))
# 변수: str_print
str_print1 = "{} + {} ={}".format(a,b,a+b)
str_print2 = "{} + {} ={}".format(a,b,a-b)
str_print3 = "{} + {} ={}".format(a,b,a*b)
str_print4 = "{} + {} ={}".format(a,b,a/b)
print(str_print1)
print(str_print2)
print(str_print3)
print(str_print4)

# 국어, 영어, 수학 점수를 입력받아 평균을 출력하시오.
# 합계 : 240
# 평균 : 80.00

kor = int(input("국어점수를 입력하시오. : "))
eng = int(input("영어점수를  입력하시오. : "))
math = int(input("수학점수를 입력하시오. : "))
total = (kor+eng+math)
avg = (kor+eng+math)/3

c=3
str_print5 = f"{total} / {c} = {total/c}"
print("평균 : ",str_print5)

total_score = "합계 : {}".format(total)
print(total_score)
total_avg = "평균 : {}".format(avg)
print(total_avg)




