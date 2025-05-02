## board table, bfile table bno 번호는 동일 
## bno = 시퀀스에 있는 bno를 쓸것임
## bfile에 a1.jpg, a2.jpg를 저장해보시오

## 1. db 연결 
from stuConn import *

conn = connections()

# 게시글 작성 
btitle = "파일첨부 게시글 제목입니다."
bcontent = "파일첨부 게시글내용입니다."
query = "insert into board values(:bno,:btitle,:bcontent,'aaa',':bno,\
    0,0,0,sysdate)" # bno를 가져오기 위해
    
    
## 2. 시퀀스 번호 생성 : bno에 저장
cursor = conn.cursor()
cursor.execute("select board_seq.nextval from dual")
bno =cursor.fetchone()[0]

## 3-1 db의 게시글 저장
cursor.execute(query,bno=bno,btitle=btitle,bcontent=bcontent)
conn.commit()

## 3. 리스트 생성 - a1.jpg, a2.jpg
##[[bno,a1.jpg],[bno,a2.jpg]]
bfilelist =[]
bfilelist.append([bno,'b1.jpg'])
bfilelist.append([bno,'b2.jpg'])

## 4. db의 파일저장
query = "insert into bfile values(:1,:2)"
cursor.executemany(query,bfilelist)
conn.commit()

## 5. 프로그램 종료
conn.close()
print("프로그램을 종료합니다.")