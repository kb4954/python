# 파일 이어쓰기 = a
f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("1,홍길동,100,100,99\n")
f.close()
# W는 모두 삭제 후 다시쓰는 개념 이라서 둘이 같이 인코딩할 경우 유관순 정보만 출력됨.
f = open("py0404/memo2.txt","a",encoding="utf-8")
f.write("2,유관순,2,50,50,50\n")
f.close()
# a는 이어서 쓰기 가능



# # # 파일쓰기 - w

# f = open("py0404/memo.txt","w",encoding="utf-8")
# print("[ 메모장 ]")
# print("-------------")
# print("저장하려는 글자를 입력하세요.(x. 종료)>> ")

# while True:
#     line = input("")
#     if line.lower() == "x":
#         break
#     f.write(line+"\n")
# f.close()

# print("글쓰기 종료")

# 안녕하세요. 글자를 10번 반복해서 저장하시오.
# f=open("py0404/aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write(f"{i+1}. 안녕하세요.\n")
# f.close()
    

# f = open("aa.txt","w",encoding="utf-8")
# # 없으면 없는걸 새로 넣어서 만들어줌
# f.write("안녕하세요.\n") #\r\n \r: 문장에 끝으로 이동
# f.write("반가워요")
# f.close()
