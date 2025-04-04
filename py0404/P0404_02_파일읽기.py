# 파일에서 입력하는것 : read(),readline(),readlines()


# 파일 입출력 : 파일열기 -> 파일읽기 및 파일 쓰기 -> 파일닫기
# 파일열기 - 3가지 모드
# 읽기용 : 변수명=open("파일명","r")
# 쓰기용 : 변수명=open("파일명","w")
# 추가용 : 변수명=open("파일명","a")
# 파일복사용 : 변수명=open("파일명","b") : 이진파일 - 파일 복사를 사용함
# f = open("a.txt","r")
# f = open("a.txt","w")
# f = open("a.txt","a")

# 파일읽어오기 - 절대경로
# f = open("C:/workspace/python/a.txt","r",encoding="utf-8")
# f = open("py0404/b.txt","r",encoding="utf-8") # 폴더안에 있는 파일읽어오기
# for line in f:
#     print(line.strip())
# f.close()
# close를 안닫는 경우 윈도우탐색기로 파일삭제시 파일이 열려 있어 삭제가 안될 수 있음 

# new.txt
f = open("py0404/news.txt","r",encoding="utf-8") # 인코딩이 읽어오는것
# 폴더안에 파일이있으면 그냥 폴더이름 적고 가져오면 됨.
# 근데 폴더 밖에 있으면 그 전에 있는 폴더까지 다 적어야함. 
for line in f:
    print(line.strip())
f.close()

# while True:
#     line = f.readline()
#     print(line.strip())
    
# while True:
#     line = f.readline()
#     lf not line: break
#     print(line.strip())
# f.close()



# # 파일읽기 - readlines(): 모두 읽어오기
# f = open("a.txt","r",encoding="utf-8") 
# # 반복문이 필요없음
# lines = f.readlines()
# for line in lines:
#     print(line.strip())
# f.close()

# 파일읽기 - r 1줄읽기   read()
# f = open("a.txt","r",encoding="utf-8") # 인코딩으로 파일형식을 바꿔야 출력가능
# print(type(f))
# 모든줄을 실행: for문이 필요
# for line in f:
#     print(line.strip()) # strip: 빈공백제거 -> 엔터키도 하나의 공백이라고 생각해서 처음에 줄간격이 생긴채로 출력되므로 제거해줘야함
# f.close()







