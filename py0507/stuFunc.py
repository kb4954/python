import oracledb

# db  연결

def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn  

## 학생성적입력 ## 미구현 
def stuInsert():
    ##1. 이름, 국어, 영어,수학점수 입력 -> 합계 평균 등수 등급처리
    name = input("이름을 입력하세요.")
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    
    total = kor+eng+math
    avg = total/3
    
    
    conn= connections()
    cursor = conn.cursor()
    sql = "insert into stuscore values(stuscore_seq.nextval, :name, :kor, :eng, :math, :total, :avg,0,'F' ) "
    cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
    conn.commit()
    print(f"{name}학생 성적이 저장되었습니다.")
    rows = cursor.fetchall()
    conn.close()





## 학생 전체 출력
def stuAllSelect(sql='select * from stuscore'):
    conn= connections()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    rows = cursor.fetchall()
    for r in rows:
        print (r)

    conn.close()
    print("종료")
    pass

## 학생성적검색
def stuSearch():
    search = input("검색하려는 이름을 입력하세요.>> ")

    conn= connections()
    cursor = conn.cursor()
    sql = "select * from stuscore where name like '%||:search||%"
    cursor.execute(sql,search=search)
    conn.commit()
    rows = cursor.fetchall()
    if len(rows)>0:
        for r in rows:
            print (r)
    else:
        print(f"찾고자하는 {search}가 없습니다. 다시입력하세요.")
    conn.close()
    print("종료")
    pass

## 4. 정렬 
def stuSort():
    print("[ 학생성적 정렬 ]")
    print("1. 이름정렬")
    print("2. 성적정렬")
    print("3. 국어정렬")
    print("4. 영어정렬")
    print("5. 수학정렬")
    print("9. 번호정렬")
    choice = input("원하는 번호를 입력하세요.>> ")

    if choice =="1":
        sorting('이름','name')
    elif choice == "2":
        sorting('성적','rank')
    elif choice== "3":
        sorting('국어','kor')
    elif choice=="4":
        sorting('영어','eng')
    elif choice=="5":
        sorting('수학','math')          
    elif choice=="9":
        sorting('번호','sno')

## 순차정렬,역순정렬 함수
def sorting(sName,sName2):
    print(f"1. {sName}순차정렬")
    print(f"2. {sName}역순정렬")
    num = int(input("원하는 정렬을 선택하시오 .>>"))
    if num==1:
        sql = f"select * from stuscore order by {sName2}"
        stuAllSelect(sql)
    else:
        sql = f"select * from stuscore order by {sName2} desc"
        stuAllSelect(sql)
        
## 학생성적 아이디 전화번호 포함 출력member, stuscore 조인
def stuIdpwSelect():
    conn= connections()
    cursor = conn.cursor()
    sql="select id,phone,a.name, kor,eng,math,a.total,avg,a.rank \
        from stuscore a, member b\
        where a.name = b.name"
    cursor.execute(sql)
    conn.commit()
    rows = cursor.fetchall()
    for r in rows:
        print (r)

    conn.close()
    print("종료")

## 등수처리 
def rankUpdate():
    conn= connections()
    cursor = conn.cursor()
    sql = "update stuscore2 a set rank = (\
    select ranks from\
    (select sno,rank() over(order by total desc) ranks from stuscore2) b\
    where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    rows = cursor.fetchall()
    conn.close()


## 등급처리 - A,B,C,D,F
def gradUpdate():
    conn= connections()
    cursor = conn.cursor()
    sql = "update stuscore a set sgrade = (\
    select grada from(\
    select sno,avg, grada\
    from stuscore,scoregrade\
    where avg between minscore and maxscore) b \
    where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    rows = cursor.fetchall()
    conn.close()
    print("종료")

