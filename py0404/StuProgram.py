# import stu_func

# import stu_func as stu # 별칭사용
# from stu_func import stu_print,stu_output,stu_input # 각각의 함수명을  갖다가 넣으면 그냥 들고옴
from StuFunc import *
import random
# 함수는 무조건 프로그램 위에 있어야함
# 함수사용 이유
# - 1. 중복된 코드의 재사용

students = []


### 파일 불러오기
# stu.txt 파일에서 데이터를 읽어와 students = []데이터 입력

with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True: # 여러줄일때 반복문 적용
        line = f.readline() # 1줄 읽어오기
        if not line: break # 데이터 없을때 종료
        s = line.strip().split(",") # 1줄 문자열을 공백제거 후, 쉼표로 구분한뒤 apppend로 student 리스트에 넣을거임
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7]),
        })
  

count = 4 # 위에 미리 3개를 입력해놨으니, 원래는 1부터 시작
title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 미리 만들어놓으면 좋음
choice = 0

# 학생점수 수정 함수선언


# global 키워드는 변수를 선언할 때 사용하지만, 동시에 값을 할당할 수 없음.
# global을 먼저 선언하고, 그 후에 값을 할당해야 함.

    
while True:
    #화면출력부분
    choice = stu_print() # 함수호출
    
    if choice == 1:
        # 학생성적 입력부분
       count = stu_input(count,students)
       # 뒤에 있는 카운트-> 함수로 날라가서 +1 되어서 5로 돌아옴
       # students가 매개변수로 stu_func 함수에 넘겨줄수 있음
       # count와 같은 1개짜리는 넘겨주고 반드시 다시 받아야함 ! 
       # 함수내에 return해서 다시 카운터를 정의해줘야 받을 수 있음 students는 여러개라서 필요없음.
    elif choice == 2: # 학생성적출력부분
       stu_output(students,title)
        
        
    # 함수: 과목 점수 수정    
    elif choice == 3: # 학생성적 수정
        print("[ 학생성적수정 ]")
        name = input("수정하려고 하는 학생이름을 입력하세요.>> ")
        temp = 0 # 찾지못했을경우
        for s in students:
            if s['name'] == name:
                temp = 1
                print(f"{name} 학생을 찾았습니다. 과목을 수정합니다.")
                print("[ 수정과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                sub_list = ['','kor','eng','math']
                if choice==1:
                    pre_score = s[sub_list[choice]] # sub_list[1]='kor' ,1 = choice
                    print(f"현재 {title[choice+1]}점수 : {pre_score}")
                    # choice+1인 이유는 title[2]=title[choice+1] 인데 choice가 1이기 때문이다.
                    # 이렇게 하는 이유는 함수로 치환하기 위해서 어느정도 공통적인 부분을 만들기 위함.
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수를 입력하세요.>>"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"변경전: {pre_score}점을 {s[sub_list[choice]]}로 변경되었습니다.")
                elif choice == 2:
                    pre_score = s['eng']
                    print(f"현재 {title[choice+1]}점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수를 입력하세요.>>"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"변경전: {pre_score}점을 {s[sub_list[choice]]}로 변경되었습니다.")
                elif choice==3:
                    pre_score = s['math']
                    print(f"현재 {title[choice+1]}점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수를 입력하세요.>>"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"변경전: {pre_score}점을 {s[sub_list[choice]]}로 변경되었습니다.")
                
                    
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시입력하세요.")
            print()    
            
                
        
        
        
    elif choice == 4:# 등수처리는 for문을 2번 돌림.
        stu_rank(students) 
    # 학생성적정렬    
    elif choice == 5:
        students2 = [*students] # 복사
        print("[ 학생성적정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면 이동")
        print()
        
        students2.sort(key=lambda x:x['name']) # 여기까지가 정렬
        
        stu_output(students2,title)
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:
            students2.sort(key=lambda x:x['name'])
        elif choice==2:
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 3:
            students2.sort(key=lambda x:x['total'])
        elif choice == 4:
            students2.sort(key=lambda x:x['total'],reverse=True)
        elif choice == 5:
            students2.sort(key=lambda x:x['no'])
        elif choice == 6:
            students2.sort(key=lambda x:x['no'],reverse=True)
        
        
        
        
    elif choice == 6:
        print("[ 학생성적삭제 ]")
        name = input("삭제하고자하는 학생 이름을 입력하세요.>> ")
        temp = 0
        for i,s in enumerate(students):
            if name == s['name']:
                temp = 1
                print(f"{s['no']} 번. {name} 학생을 찾았습니다. ")
                answer = input("학생 성적을 삭제할까요 ?(*삭제하시면 복구불가)")
                if answer == "y":del students[i]
                print(f"{name} 학생을 삭제했습니다. ")
                break
        if temp==0:
            print("삭제하고자하는 학생을 찾지못했습니다. 다시 입력하세요.!!")
            print()
                    
                    
                
        
                  
    elif choice == 7: # 학생성적 저장
        print("[ 학생성적저장 ]")            
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                # 1,홍길동,100,100,100,300,100.0,1 이 한줄을 만드는 방법 바로 아래
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다.")
        print("-"*30)
        
        
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
    
        




