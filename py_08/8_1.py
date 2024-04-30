# Dictinary는 list와 비슷
# 리스트처럼 첨자를 이용해서 요소에 접근
# 키-값의 쌍으로 구성
# 탐색속도가 빠르고 사용하기도 편리
# 중괄호 {} 사용
# 특정슬롯에 새로운 키-값을 입력하거나 딕셔너리 안에 있는 요소를
# 참조할때는 리스트와 튜플처럼 대괄호[] 이용
dic = {}
dic['r'] = 'red'
dic['g'] = 'green'
dic['b'] = 'blue'

print(dic['r'])
print(dic['g'])
print(dic['b'])

print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

print('r' in dic.keys())
print('t' in dic.keys())