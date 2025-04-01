a_list = [1,2,3,4,5]
count = 0
while True:
    # 화면출력
    print(a_list)
    # 숫자입력
    num = int(input("숫자를 입력하세요.>> "))
    for i in range(len(a_list)): #len(a_list) = 5
        if a_list[i] == num:
            a_list[i] = "X"
            count += 1 # 내가 숫자를 입력할때마다 X표시로 카운트+1하면서 5개가 되어 빙고가 될때까지 기다리는 것
            break
        
    # X 개수 확인
    if count >= 5:
        print("빙고 완성!!")
        print(f"개수: {count}")
        break
    
    
    print(f"현재개수 : {count}")
