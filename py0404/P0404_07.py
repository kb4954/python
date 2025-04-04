# 파일 읽어오기 기본

# 1. open()
# 2. f.read()
# 3. f.close
# r: 읽기, w: 쓰기, a: 이어쓰기
students = []
f= open("py0404/stu.txt","r",encoding="utf8")
# 1줄이면 여러줄이 반복문을 실행
while True:
    data = f.readline()
    if not data: break
    # data : 1,홍길동,60,100,100,260,86.66666666666667,4
    # 데이터를 쉼표가 있는 s형태로 분리
    s = data.strip().split(",")
    # students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ]
# 무조건 이 형태로 바꿔서 해야지 데이터를 가져오거나 할 수 있음
    students.append({
        "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":s[7]
    })
f.close()

print(students)




