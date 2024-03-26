# 입력 단어가 지금까지 배운 파이썬의 키워드인지를 in문으로 결과 출력
inkey = input('배운 파이썬 키워드를 입력하세요 : ')
keywords = "'False', 'True', 'and', 'in', 'is', 'not', 'or'"
print('입력 단어 {}, 배운 키워드인가? {}'.format(inkey, inkey in keywords))

# if문
# 키가 140 이상이면 롤러코스터 타기
height = int(input('키를 입력하세요 : ')) # 탑승 체크할 키 입

if height <= 140:
    print('롤러코스터를 즐기세요!') # 첫번째 열이 띄어쓰기가 되어있어야 함

#if... else
print('수를 입력하세요 : ')
a = int(input())

if a == 0:
    print('0은 나눌수 없음')
    print("참이면 이 문장도 보임")
else :
    print('3 / ', a, '=', 3/a)
    print("거짓이면 이 문장도 보임")
print("이 문장은 항상 보임") # 파이썬은 중괄호가 필요없음
