a_list = [ [1,"X",3,"X",5], [6,"X",8,9,10] ]

# 현재 리스트의 X개수 확인
no = 0 # no가 곧 X개수세는 변수
for i in range(5):
    if a_list[0][i] == "X":
        no += 1
if no == 5:
    print("빙고완성!!")
print(f"현재 [0]방의 X개수 : {no}")
#----------------------------------------------------------







