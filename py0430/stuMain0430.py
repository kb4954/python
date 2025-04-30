## 학생성적 프로그램 
## 진행하세요
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
]

print("[ 학생성적 프로그램 ]")
print("-"*40)
print("1. 학생성적입력")
print("2. 학생성적출력")
print("3. 학생성적수정")
print("4. 등수처리")
print("5. 학생성적정렬")
print("6. 학생성적삭제")
print("7. 학생성적저장")
print("0. 프로그램종료")
choice = int(input("원하는 번호를 입력하세요.>>"))

students = []
title = ['번호','이름','국어','영어','수학','합계','평균','등수'] 
count = 4
if choice == 1:
    while True:
            print("학생성적입력")
            no = count
            name = (input(f"{no}번째 학생이름을 입력하세요.(0.이전화면 이동)"))
            if name == "0": break
            while True:
                kor = int(input("국어점수를 입력하세요."))
                eng = int(input("영어점수를 입력하세요."))
                math = int(input("수학점수를 입력하세요."))
                total = kor+eng+math
                avg = total/3
                rank = 0   
                students.append({"no":no, "name":name ,"kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank}) 
                count += 1 
                print()
                
                
            
        
elif choice ==2:
    while True:
        print("학생성적출력")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
        print()
            
elif choice==3:
    while True:
        print("학생성적 수정")
        name = input("수정하려고 하는 학생 이름을 입력하세요.")
        temp = 0 # 찾았는지 못찾았는지 변수로 확인
        for s in students:
            if name is s['name']:
                temp = 1
                print(f"{name}학생을 찾았습니다.")
                print("[수정과목 선택]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("원하는 번호를입력하세요"))
                if choice==1:
                    pre_kor = s['kor']
                    print(f"현재 국어 점수 : {pre_kor}")
                    s['kor'] = int(input("변경 국어점수 : "))
                    s['total']=s['kor'] +s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"국어점수 {pre_kor}점을 {s['kor']}으로 변경하였습니다. ")
                print()
                if choice==2:
                    pre_eng = s['eng']
                    print(f"현재 영어 점수 : {pre_eng}")
                    s['eng'] = int(input("변경 영어점수 : "))
                    s['total']=s['kor'] +s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"영어점수 {pre_eng}점을 {s['eng']}으로 변경하였습니다. ")
                print()
                if choice==3:
                    pre_math = s['math']
                    print(f"현재 수학 점수 : {pre_math}")
                    s['eng'] = int(input("변경 수학점수 : "))
                    s['total']=s['kor'] +s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"수학점수 {pre_math}점을 {s['math']}으로 변경하였습니다. ")
                print()
                
                
                
            if temp == 0:
                print("수정하고자 하는 학생을 찾지 못했습니다. 다시 입력하세요.")
                
                
                
            elif choice == 0:
                print("[프로그램 종료]")
                break
            
            
elif choice==4:
    print("등수처리")
    for s in students:
        num =1
        for ss in students:
            if s['total']<ss['total']:
                num+=1
            s['rank'] = num
            
            
    print("등수처리가 완료되었습니다.")
    print()        
    
elif choice==5:
    print("[학생성적정렬]")
    
    
elif choice==7:
    print("[학생성적저장]")
    with open("py0430/stu0430.txt","w",encoding="utf8") as f:
        for s in students:
            data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
            f.write(data)
    print("파일저장완료")
    print("-"*30)

        
   
    
    