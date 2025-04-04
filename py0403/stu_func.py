# 화면출력 함수 선언
# 함수의 묶음 = 모듈
# ex) import sun_func, random

# 화면출력 함수 선언
def stu_print():
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("0. 프로그램종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice


# 학생성적입력 함수선언
def stu_input(count,students):
    no = count
    name = (input(f"{no}번째 학생 이름을 입력하세요.>> "))
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor + eng + math
    avg = total/3
    rank = 0
    students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
    print(f"{no}번 {name}학생이 등록되었습니다.")
    print()     
    count += 1
    return count


# 학생성적출력 함수 선언
def stu_output(students,title):
    print("[ 학생 성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
    print()
    
    # 등수 함수 선언
def stu_rank(students):
    print("[ 등수처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if s['total']<ss['total']: # 등수비교
                num += 1                #등수 1 증가
            s['rank'] = num             # 등수입력
            
    print("등수처리가 완료되었습니다.")
    print()
    
    
    