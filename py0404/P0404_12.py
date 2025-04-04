students = [
    {'no': 4, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': '4'}, 
    {'no': 3, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': '2'}, 
    {'no': 5, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': '1'}, 
    {'no': 1, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': '5'}, 
    {'no': 2, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': '3'}
    ]

# max : 최대값함수 students 리스트, x['no']
print(max(students,key=lambda x:x['no']))
# 출력: {'no': 5, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': '1'}
# students 최대값 1 증가한 값
print(max(students,key=lambda x:x['no'])['no']+1)
