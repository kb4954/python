# num = 7
# if 10>=num>=0:
#     print("10에 해당되는 숫자입니다.")
# # 파이썬은 위처럼 가능 모든 언어는 아래처럼 표시
# if 10>=num and num>=0:
#     print("10에 해당되는 숫자입니다.")

# 숫자를 입력받아, 봄,여름,가을.겨울을 출력하시오.

# 3,4,5 -> 봄의 계절입니다.
# 6,7,8 -> 여름의 계절입니다.
# 9,10,11 -> 가을의 계절입니다.
season= int(input("숫자를 입력하세요.>> "))
if 2<season<6:
    print("봄의 계절입니다.")
elif 5<season<9:
    print("여름의 계절입니다.")
elif 8<season<12:
    print("가을의 계절입니다.")
elif 12==season and season==1 and season==2:
    print("겨울의 계절입니다.")














