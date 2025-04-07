# 파일불러오기 # 1---------------------------
print("[ 학생성적프로그램 ]")
print("-"*40)
print("1. 학생성적입력") # 6.
print("2. 학생성적출력") # 2---------------------
print("3. 학생성적수정") # 7
print("4. 등수처리")     # 8
print("5. 학생성적정렬") # 3-----------------
print("6. 학생성적삭제") # 5-----------------
print("7. 학생성적저장") # 4-------------
print("0. 프로그램종료")

# 1. 먼저 students 불러오기
from StuFunc import *

students = []
with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline() # 1줄씩 가져오는거라서 반복문 사용
        if not data: break
        s = data.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":(s[7])
        })
        
students = []
# 숙제 이거 2번 작성하기
# with open("py0404/stu.txt","r",encoding="utf8") as f:
#     While True:
#         data = f.readline()
#         if not data: break
#         s = data.strip().split(",")
#         student.append({
#             "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":(s[7])
#         })



# 최대값 +1 증가       
# count = (max(students,key=lambda x:x['no'])['no']+1)
count = max(students,key=lambda x:x['no'])['no']+1
title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 미리 만들어놓으면 좋음
choice = 0
        
while True:
    choice = stu_print()
    
    
    if choice == 1:
        count = stu_input(count,students)
    
    if choice == 2:
        stu_output(students,title)
    if choice == 3:
        pass
    if choice == 4:
        pass
    # if choice == 5: # 정렬에서는 원래 리스트를 보호하기 위해서 얕은 복사를 함
    #     print("[ 학생성적정렬 ]")
    #     students2=[*students]
    #     print("[ 학생성적정렬 ]")
    #     print("1. 이름 순차정렬")
    #     print("2. 이름 역순정렬")
    #     print("3. 합계 순차정렬")
    #     print("4. 합계 역순정렬")
    #     print("5. 번호 순차정렬")
    #     print("6. 번호 역순정렬")
    #     print("0. 이전화면 이동")
    #     print()
        
    #     students2.sort(key=lambda x:x['name'])
    if choice == 7:
        print("[ 학생성적저장 ]")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}"
                f.write(data)
        print("파일 저장 완료")
        print("-"*30)
        
        
        
    






