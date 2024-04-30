# 항목 조회 get()
# 항목 추가 dictionary 이름[키] = value
# 항목 삭제 pop.popitem()
# 모든 항목 삭제 clear()
color = dict(검정='black', 흰색='white', 녹색='green', 파랑='blue')
print(color)

# 항목 조회
print(color.get('녹색'))
print(color.get('노랑'))
print()

# 항목 추가
color['노랑'] = 'yellow'
color['분홍'] = 'pink'
print(color)
print()

# 항목 삭제
c = '흰색'
print('삭제 : %s %s'  %  (c, color.pop('흰색')))
print(color)
c = '빨강'
print('삭제 : %s %s'  %  (c, color.pop(c, '없어요')))
print()

print('임의 삭제 : {}'.format(color.popitem()))
print('임의 삭제 후 : {}'.format(color))
print()

c = '검정'
del color[c]
print('{} 삭제 후 : {}'.format(c, color))

# 모든 항목 삭제
color.clear()
print(color)