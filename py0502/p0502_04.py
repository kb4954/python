from stuConn import *

conn = connections()

## 여러개 저장
## 시퀀스 번호 생성

cursor = conn.cursor()
query = "select board_seq.nextval from dual"
cursor.execute(query)
rows = cursor.fetchone()[0]

query = "select board_seq.nextval from dual"
cursor.execute(query)
bno = cursor.fetchone()[0]
cursor = conn.cursor()
### 여러개 파일 리스트 생성  
bfile= []
bfile.append([bno, '11.jpg'])
bfile.append([bno, '12.jpg'])
bfile.append([bno, '13.jpg'])

## 여러개 파일 db에 저장
query = "insert into bfile values(:1,:2)" # (bno, bfile)
cursor.executemany(query,bfile)           # executemany 여러번 실행
conn.commit()

# 프로그램 종료
print(bfile)
print("프로그램 종료")


