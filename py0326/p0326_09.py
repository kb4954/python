# # 이름입력, 국어, 영어, 수학 성적을 입력받아 합계, 평균을 출력하시오.
# # 이름 : 홍길동
# # 합계 : 300
# # 평균: 100.0 소수점은 1자리까지 출력하시오.

# name = input("이름을 입력하시오. : ")
# kor = int(input("국어점수를 입력하시오. : "))
# eng = int(input("영어점수를  입력하시오. : "))
# math = int(input("수학점수를 입력하시오. : "))
# sien = int(input("과학점수를 입력하시오. :"))

# total = (kor+eng+math+sien)
# avg = (kor+eng+math+sien)/4

# print("이름 : ",name)
# print("국어 : ",kor)
# print("영어 : ",eng)
# print("수학 : ",math)
# print("과학 : ",sien)
# print("합계 : ",kor+eng+math+sien)
# print("평균 : %.1f" % avg)
# 프린트시 \n : 엔터키 \t : tap키
print("안녕하세요.\n 반갑습니다.\t 저는 홍길동이라고 합니다. ")

# format() 문자형태 함수
a = 10
b = 3
print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} + {} ={:.2f}".format(a,b,a/b)
print(str_print)
# f함수 = format()
str_print2 = f"{a} / {b} = {a/b:.2f}"
print(str_print2)





