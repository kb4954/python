### 학생성적프로그램에서 1명의 학생을 등록해보세요.

from stuConn import *

conn = connections()


name = input("학생 이름을 입력하세요")
kor = input("국어점수를 입력하세요")
eng = input("영어점수를 입력하세요")
math= input("수학점수를 입력하세요")
total = kor+eng+math
avg = total/3
query ="insert into stuscore values(\
stuscore_seq.nextval,':name',:kor,:eng,:math,total,avg,0)"
cursor = conn.cursor()
cursor.execute(query)
conn.commit

conn.close()
print("프로그램을 종료합니다.")

