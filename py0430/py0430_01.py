import dbconn

print("----------------db연결---------------")
## db 접속
# conn = 접속이 된것임 오라클 접속과 동일
conn = dbconn.connections() # SQL dev 프로그램 오픈
cursor = conn.cursor() # sql창 오픈
name = input("검색하려는 이름을 입력하세요.")
# query = "select emp_name,employee_id, salary from employees where salary between 4000 and 6000"

name = '%'+name+'%'

query = "select emp_name,employee_id, salary from employees where emp_name like:name"
cursor.execute(query,name=name) # sql구문 F9실행
rows = cursor.fetchall() # 데이터를 가져옴
## employees 월급이 4000~6000 사이의 사번, 이름 월급을 출력하시오

for r in rows:
    print(r[0],r[1],r[2])
    



