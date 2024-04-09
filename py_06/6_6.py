# list 데이터 목록을 다루는 자료형, 단일 데티어 사용
# 리스트는 콤마로 구분된 항목들의 리스트로 표현
# 항목은 정수, 실수, 문자열, 리스트 등이 모두 가능
# 항목 순서는 의미가 있으며, 항목 자료값은 중복돼도 무관
# 대괄호 [] 사용

# 슬라이싱, 특정 값 추출
# len()함수로 리스트 길이 계산

# coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']
# print(coffee)
# print(coffee[0])
# print(coffee[1])
# print(coffee[2])
# print('==')
# print(coffee[0:2])
# print(coffee[:2])
# print(coffee[2:])

# coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']

# num = 0
# for s in coffee:
#     num = num + 1
#     print("%d. %s" %(num, s))

coffee = ['에스프레소', '아메리카노', '카페라떼', '카페모카']

print((len(coffee)))
for i in range (len(coffee)):
    print(coffee[i])