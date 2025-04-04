# 로또프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력

lotto=[0]*6

win_lotto = []
lotto = [i+1 for i in range(45)]
lotto2 = [i+1 for i in range(45)]
my_lotto = [0]*6 # 이렇게 하지않고, [] 빈리스트로 두었을때 my_lotto(count)에서 인덱스범위 초과가 될 수 있다. 미리 리스트내에 방을 두는것이 좋음!
def lotto_mix():
    global lotto,lotto2
    random.shuffle(lotto)
    lotto2 = [i+1 for i in range(45)]

while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가 입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> ")) 
    
    if choice == 1: #랜덤번호랑 출력될 순차번호가 필요함
        lotto_mix()
    elif choice == 2:
            count = 0
            
    while True:
        
        print("[ 로또번호 입력 ]")
        print("-"*50)
        for i in range(45):
            if 1==0:pass
            if i%7==0: print() # 04번과 다른 수정본
            print(lotto2[i],end="\t")
        print()
        #---------------------------------------------------              
        choice = int(input("로또번호를 입력하세요.(0.이전화면 이동)"))
        if choice == 0:break
        if choice<0 or choice>45:
            print(f"{choice}는 없는 번호입니다. 다시 입력하세요.")
            continue
        temp = 0 #
        for i in lotto2:
            if i == choice:
                [lotto2[i-1]] = "X"
                my_lotto[count] = choice # count가 인덱스 역할을 함 
                count += 1
                temp = 1
        if temp ==0:
            print(f"{choice}는 입력하신 번호입니다. 다시입력하세요.")
            
        if count >= 6:
            print("로또번호 6개를 모두 입력하셨습니다!")
            break
    
                        
        elif choice == 3:
            print("[로또당첨번호 확인]")
            print("-"*50)
            for i in lotto[:6]:
                for j in my_lotto:
                    if i==j:
                        win_lotto.append(i)
            print("로또 당첨번호:",lotto[:6])
            print("내가 입력한 로또번호",my_lotto)
            print("당첨된 로또번호",win_lotto)
            print("당첨된 개수",len(win_lotto)) # len : 리스트에 있는 개수를 구해주는 함수          
        
        elif choice == 4:
            print("로또리스트: ",lotto)
        elif choice == 5:
            print("입력한 로또 번호: ",my_lotto)
        elif choice == 0:
            print("[ 프로그램 종료 ]")
            break
    



    
                    
        
        