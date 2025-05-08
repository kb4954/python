from pyFunc import *
 
## db 연결
def connections():
    try: conn=oracledb.connect(user='ora_user',password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
conn= connections()
cursor = conn.cursor()

1256
while True:
    print("[ 학생성적  프로그램 ]")
    print("1. 학생전체 출력 ")
    print("2. 학반별 최고등수 출력 ")
    print("3. 학반별 최하등수 출력 ")
    print("4. 부서별 최고연봉 출력 ")
    print("5. stusocre2 학반 부여(1-10,1...) ")
    print("6. 회원정보 rownum 11-20번 출력 ")
    print("-"*20)
    choice = input("원하는 번호를 입력하세요.>> ")
    
    if choice == "1": # 학생전체출력
        stuAllSelect()
    if choice == "2": # 학년별 최고등수 출력
        stuHigh()
    if choice == "3":pass
    if choice == "4":pass
    if choice == "5":
        print("5. stusocre2 학반 부여(1-10,1...)")
        conn= connections()
        cursor = conn.cursor()
        sql = 'select * from stuscore '
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        
        conn.close()
        print("종료")
        
         
        
        