### 파일 - 저장해서 불러오기 방식으로 만들기
### DB에서 불러오기

#### 전역변수 선언부분 ####
# students는 리스트타입
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
]

print(students)

count = 4 # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

### 함수 부분 ###
# 학생성적입력 함수
def stu_input(count):
    while True:
            print("[ 학생성적입력 ]")
            no = count
            name = input(f"{no}번학생 이름을 입력하세요.(0.이전화면 이동) ")
            if name == "0":break # 학생성적 입력에서 전체화면으로 이동
            #------------------------------------------------------------
            score = [0]*3 # list 생성 # 주소값으로 넘겨주고 있기때문에 리턴해줄필요없다
            score_cal(0,score) # 국어점수입력,확인
            score_cal(1,score) # 영어점수입력,확인
            score_cal(2,score) # 수학점수입력,확인 
            total = score[0]+score[1]+score[2]
            avg = total/3
            rank = 0
            students.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
            print(f"{no}번 {name}학생 성적이 입력되었습니다.")
            print()
            count += 1 # 학생수 1증가
            return count

# 국어,영어,수학점수 입력하고 확인하는 함수
def score_cal(i,score):
    while True:            
        score[i] = input(f"{title[i+2]}점수를 입력하세요.>> ")
        if score[i].isdigit():
            score[i] = int(score[0])
            if i <= score[i] <= 100:
                break    
            else: print("점수는 0~100사이의 값을 입력하셔야합니다.")
        else: print("숫자만 가능합니다.")

while True:
    print(" "*10,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    # 번호선택
    if choice == 1:
        count = stu_input(count)
            
            
            
            
            
            
            
            # while True:
            #     score[1] = input(f"{title[3]}점수를 입력하세요.>> ")
            #     if score[1].isdigit():
            #         score[1] = int(score[1])
            #         if 0 <= score[1] <= 100:
            #             break    
            #         else: print("점수는 0~100사이의 값을 입력하셔야합니다.")
            #     else: print("숫자만 가능합니다.")
            # while True:    
            #     score[2] = input(f"{title[4]}점수를 입력하세요.>> ")
            #     if score[2].isdigit():
            #         score[2] = int(score[2])
            #         if 0 <= score[2] <= 100:
            #             break    
            #         else: print("점수는 0~100사이의 값을 입력하셔야합니다.")
            #     else: print("숫자만 가능합니다.")
                            
                # no,name,kor,eng,math
                # 합계,평균
                
            
                    
                    
    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        
    elif choice == 3:
        print("[ 학생성적수정 ]")
        name = input("수정하려고 하는 학생이름을 입력하세요.>> ")
        #이전화면 이동 확인 함 해보깅
        temp = 0 # 찾고자하는 학생이 없을 경우
        for s in students:
            if name in s['name']: # 찾았을 경우
                temp = 1 # 1로 변경
                print(f"{name} 학생이 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                # 수정할 과목 확인
                if choice == 1:
                    pre_kor = s['kor'] # 이전국어점수변수를 하나 받아놓기
                    print(f"현재 국어점수 : {pre_kor}")
                    s['kor'] = int(input("변경 국어점수 : "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    # 합계, 평균 수정
                    print(f"국어점수 {pre_kor}점을 {s['kor']} 으로 변경하였습니다.")
                    
                elif choice == 2:
                    pre_eng = s['eng'] # 이전영어점수변수를 하나 받아놓기
                    print(f"현재 영어점수 : {pre_eng}")
                    s['eng'] = int(input("변경 영어점수 : "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    # 합계, 평균 수정
                    print(f"영어점수 {pre_eng}점을 {s['eng']} 으로 변경하였습니다.")
                    
                elif choice == 3:
                    pre_math = s['math'] # 이전국어점수변수를 하나 받아놓기
                    print(f"현재 수학점수 : {pre_math}")
                    s['math'] = int(input("변경 수학점수 : "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    # 합계, 평균 수정
                    print(f"수학점수 {pre_math}점을 {s['math']} 으로 변경하였습니다.")
                
                
                print()
                    
            # 여기에 else를 쓰지 않는 이유: 못찾았다는 멘트가 매번 나오다가 찾았다라는 멘트가 나올 수 있기때문    
        # 수정할 학생을 찾지 못했을 경우
        if temp == 0:
            print("수정하고자하는 학생을 찾지 못했습니다. 다시 입력하세요.!!")
            
            
        
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
                