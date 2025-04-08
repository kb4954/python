from stuModule import * # 별표하면 두가지 다 가져오는거임 
# 객체선언, students 객체변수
students = Students()

title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# -----------------------------------------------------------------------------------------------------------
# 상단메뉴부분
def tmenu_print():
    print("-"*20)
    print("[ 학생성적처리 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요. "))
    except Exception as e: print(e)
    return choice

#------------------------------------------------------------------------------------------------
# 1. 학생성적입력 함수 선언
def stu_input():
    print("[ 학생성적입력 ]")
    name = input(f"{Student.count}번째 학생 이름을 입력하세요.>> ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]} 점수를 입력하세요.>> "))
    # students.add(Student(name,score[0],score[1],score[2])) # 들어가면서 저절로 no, total, avg가 생성됨
    students.add(Student(name,*score)) #바로 윗줄이랑 같은내용 
    print(f"{name} 학생 성적이 등록되었습니다. ")
    print()


#-------------------------------------------------------------------------------------------------------------------------------
# 2. 학생성적출력 함수 선언    
def stu_output():
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students:# 앞 students : stuFunc에 있는 객체선언 , 뒤 students : stuModule에 있는 students라는 변수
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")
        
        
#-------------------------------------------------------------------------------------------------------------
# 3. 학생성적수정함수 선언
def stu_modify():
    print("[ 학생성적수정 ]")    
    search = input("수정하고자하는 학생 이름을 입력하세요.>> ")
    temp = 0 # 찾지 못했을때 사용변수
    for s in students.students:
        if search == s.name:
            temp = 1
            print(f"{search} 학생을 찾았습니다. 성적을 수정합니다. ")
            print("[ 수정과목선택 ]")
            print("1. 국어")
            print("2. 영어")
            print("3. 수학")
            print("-"*40)
            try:
                choice = int(input("원하는 번호를 입력하세요.>> "))
            except Exception as e: print(e)
            # s.kor, s.math, s.eng는 매개변수로 활용할것 함수에서
            if choice == 1:
                s.kor = sub_Modify(choice,s.kor)

            elif choice == 2:
                s.eng = sub_Modify(choice,s.eng)
                                
            else:
                s.math = sub_Modify(choice,s.math)
            s.stu_total() # 합계수정
            s.stu_avg() # 평균수정
            print()

    if temp == 0:
        print(f"{search} 학생을 찾지못했습니다. 다시입력하세요!")
        
# 3-1. 선택된 과목 수정함수 
def sub_Modify(choice,subject): # subject : s.kor, s.math, s.eng
    print(f"[ {title[choice+1]}과목 수정 ]")
    print(f"현재{title[choice+1]}점수: {subject}")
    subject = int(input(f"수정할 {title[choice+1]}점수 입력: ")) 
    print(f"{subject}점으로 {title[choice+1]} 점수가 변경되었습니다. ") 
    return subject


#-------------------------------------------------------------------------------------------------------