daysA = {'월', '화', '수', '목'}
daysB = set(['수', '목', '금', '토', '일'])
weekends = set(('토', '일'))

alldays = daysA | daysB # 합집합, 중복은 한번만 출력
print(alldays)

workdays = alldays - weekends
print(workdays)

print(daysA & daysB) # 교집합, 중복만 출력

# 중복된거 빼고 모두 출력
print(daysA.symmetric_difference(daysB))