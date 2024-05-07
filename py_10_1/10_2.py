#enumerate() 0부터 시작하는 첨자와 항목 값의 튜플리스트를 생성

lst=[10, 20, 30]
print(lst)
print(list(enumerate(lst)))

print(list(enumerate([22,33,44], start=1)))

lst2 = 'python'
print(list(enumerate(lst2)))

# 튜플과 시퀀스 간의 변환 // 리스트와 집합 간의 변환
print('---')
space = '밤', '낮', '해', '달'
print(space)
print(list(space)) #리스트 변환
print('---')
singer = ['bts', '블랙핑크'] #list
print(singer)
print(tuple(singer)) #tuple 변환
print(set(singer)) #list 변환
print('---')
game=dict(일='밤', 이='낮', 삼='해', 사='달')
print(game)
print(list(game)) #key로만 구성됨
print(tuple(game)) #key로만 구성됨
print(set(game)) #key로만 구성됨