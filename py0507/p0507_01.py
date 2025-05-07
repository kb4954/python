from stuFunc import *

# db  연결

def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn  
    
conn= connections()
cursor = conn.cursor()

while True:
    print("[ 학생성적 프로그램 ]]")
    print("-"*20)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    print("4. 학생성적정렬")
    print("5. 학생 성적 아이디,전화번호 출력-member, stuscore 조인")
    print("8. 등수처리")
    print("9. 등급처리")
    print("0. 프로그램 종료")
    choice = input("원하는 번호를 입력하세요.")
    
    if choice == "1": ## 학생성적입력
        stuInsert()
    elif choice == "2": ## 학생성적출력
        stuAllSelect() 
    elif choice == "3": ## 학생성적검색
        stuSearch()
    elif choice == "4": ## 학생성적정렬 
        stuSort()
    elif choice == "5": ## 학생성적아이디 전화번호 출력  
        stuIdpwSelect()
    elif choice == "8": ## 학생성적정렬 
        rankUpdate()
    elif choice == "9": ## 등급처리
        gradUpdate()
    else: break
        

    
    


## update
sql = "update stuscore2 set rank = 0 "
cursor.execute(sql)
conn.commit()



## select 
sql = "select * from stuscore2"
cursor.execute(sql)

rows = cursor.fetchall()
for r in rows:
    print (r)
    

conn.close()
print("종료")


