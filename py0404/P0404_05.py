students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]
# 1. students 리스트를 문자열로 변환
# 2. 파일쓰기 해서 문자열을 저장



f = open("py0404/stu.txt","a",encoding="utf-8")
for s in students:
    line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
    f.write(line)
f.close



# 1,2,3
# stu.txt

# 1,홍길동,100,100,100,300,100.0,1
# 2,유관순,100,100,99,299,99.67,2
# 3,이순신,100,100,99,299,99.67,3