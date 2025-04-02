students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":1,"name":"유관순","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
    {"no":1,"name":"이순신","kor":100,"eng":100,"math":100,"total":299,"avg":99.67,"rank":2},
]

print(students)

count = 4 # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*10,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        print("[ 학생성적입력 ]")
        no = count
        name = input(f"{no}번학생 이름을 입력하세요.(0.이전화면 이동)")
        if name == '0':
            break
        kor = int(input("국어점수를 입력하세요.>>."))
        eng = int(input("영어점수를 입력하세요.>> "))
        math = int(input("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
        print(f"{name}학생의 성적이 입력되었습니다.")
        print()
        
        count += 1
        
    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*50)
        print("{}\t,{}\t,{}\t,{}\t,{}\t,{}\t,{}\t,{}\t".format(*title))
        print("-"*50)
        for s in students:
            print(f"{s['no']}\t,{s['name']}\t,{s['kor']}\t,{s['eng']}\t,{s['math']}\t,{s['total']}\t,{s['avg']}\t,{s['rank']}\t,")
            
        print()    
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
        
            
        
    