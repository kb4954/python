# 날짜 시간.
# 날짜 클래스 시간을 가져올 수 있는 개체
import datetime 

now = datetime.datetime.now()
print("현재시간 : ",now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 시간이 12 이상이면 오후, 12 미만이면 오전이라고 하고 시간을 출력하시오. 
# 13시 -> 오후 1시
# 9시 -> 오전 9시

# 15시 -> 오후 3시라고 출력

# if 조건을 사용해서 오전, 오후라고 하고 시간을 출력하시오.

hour = now.hour
minute = (now.minute)
if hour>12:
    print("오후 {:02d}:{:02d}시".format(hour,minute)) #13 -> 오후 1시니깐 hour-12로 표현 가능
else:
    print("오전 {:02d}:{:02d}시".format(hour,minute))

# 2025-03-27
print("{}-{:02d}-{}".format(now.year,now.month,now.day))


    
    


