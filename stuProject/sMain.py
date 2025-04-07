# 1. sModule.py - class 2개
# 2. sMain.py
# 2번 다 입력하고 나중에 sFunc.py로 옮기기
# - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄

from sModule import *
students = Students()

title = ['번호','이름','국어','영어','수학','합계','평균','등수']


while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램종료")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요.>> "))
    except Exception as e:
        print(e)
     
    if choice == 1: 
        print("[] 학생성적입력 ]")  
        # no는 없고 바로 name으로 
        name = input(f"{Students.count}번째 학생이름을 입력하세요.>>")
        score = [0]*3
        for i in range(len(score)):
            score[i] = int(input(f"{title[i+2]}의 점수를 입력하세요."))
            students.add(Students(name,*score))
            print(f"{name}학생 성적이 등록되었습니다.")
            print()
            
            
    if choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t,{}\t,{}\t,{}\t,{}\t,{}\t,{}\t,{}".format(*title))
        print("-"*60)
        # 반복문 써야됨
        for s in students.students:
            print(s.no,s.n)
        