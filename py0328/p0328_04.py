# 1,3,5,7,9......99 1-100사이의 홀수만 숫자를 더해서 합계를 구하시오.
# sum = 0
# for i in range(1,100+1,2):
#     sum = sum + i

# print("합계 : ",sum)

# 3의 배수 또는 7의 배수에 해당되는 배수만 더하기 해서 sum을 구하시오.
sum = 0
for i in range(1,100+1):
    if i%3 == 0 or i%7 == 0: sum = sum + i
    print("i : {}, sum : {}".format(i,sum))

print("합계 : ",sum)    







