
#  finally 예외시, 예외가 발생되지 않았을때 모두 실행
# try:
#     f = open("info.txt","w")
#     raise NotImplementedError # raise: 강제로 발생
#     f.close()
# except Exception as e:
#     print(e)
#     f.close()
# finally:
#     f.close() # 밖에다가 해도 되지만 보통 한묶음 밖에 작성하지 않음.
    
# a_list = [1,2,3,4,5]
# print(a_list)
# try:
#     print(a_list[5])
# except ValueError: #valueError만 처리함.
#     print("출력되어야 함")
# # except IndexError:
# #     print("인덱스 에러임")
# except Exception as e:
#     print(e) # 대부분의 예외의 상위 예외. 이것만 사용함.
#     print("모든 예외처리가 다 가능함.")
# print(7)
# print(8)

# 에러구문을 넣어서 에러를 낼 수 있다.
print(1)
print(2)
raise NotImplementedError("프로그램 미구현-수정부분이 프로그램 진행해야 함.")
print()

    
    