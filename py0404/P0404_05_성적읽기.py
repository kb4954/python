# with 함수 사용시 f.close()생략가능
# 모든 학생 영어점수 +2를 하시오.

# aStr = "1,홍길동,100,100,200"
# a_list = aStr.split(",")
# print(a_list) # list타입으로 변경해서 전달
# print(int(a_list[3])+1)
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ]
['1', '홍길동', '100', '99', '199']
# stu.txt -> 영어성적을 +1 증가하고 합계도 +1 증가해서 
# 전체리스트를 출력하시오.
# 1,홍길동,100,100,200
# 1,홍길동,100,99,199
# 2,유관순,50,50,100

# 1,홍길동,100,101,200
# 1,홍길동,100,100,199
# 2,유관순,50,51,100
student = []
f = open("py0404/stu.txt","r",encoding="utf-8")
while True:
    line = f.readlines()
    if not line: break
    print(line.strip())
    s = line.strip().split(",")
    print("{},{},{},{},{}".format(*s))
    print("영어: ",int(s[3])+1)
    print("합계: ",int(s[4])+1)
    # list 수정
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3]+1)
    s[4] = int(s[4]+1)
    print("{},{},{},{},{}".format(*s))
    student.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3])+1,"total":int(s[4])+1})
    
f.close()

for ss in student:
    print(ss)
    

# 내가 한거
# f = open("py0404/stu.txt","r",encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     s_list = line.strip().split(",")
#     print(s_list)
#     print([s_list[0],s_list[1],s_list[2],int(s_list[3])+1,s_list[4]])

# f.close()

# f = open("py0404/stu2.txt","r",encoding="utf-8")
# line = f.readline()
# a_list = line.strip().split(",")
# print(a_list)
# print(int(a_list[3])+1)
# f.close()


# while True:
#     line = f.readline()
#     if not line: break
#     a_list = line.split(",") # list타입으로 변경해서 전달
# print(a_list)
# print(int(a_list[3])+1)

# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
        
        