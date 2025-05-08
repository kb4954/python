import oracledb

def connections():
    try: conn=oracledb.connect(user='ora_user',password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn

## 1. 학생 전체 출력 
def stuAllSelect():
    print("1. 학생전체 출력")
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
        
## 2.학년별 최고등수 출력
def stuHigh():
    print("2. 학년별 최고등수 출력 ")
    conn= connections()
    cursor = conn.cursor()
    sql = 'select * from stuscore a\
        where (a.sclass, a.total) \
        in (select sclass, max(total) from stuscore \
        group by sclass) '
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print (r)
    conn.commit()
    conn.close()
    print("종료")

        