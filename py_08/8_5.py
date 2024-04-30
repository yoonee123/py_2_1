# 집합 (set) 원소는 유일하고(중복안됨) 순서는 의미 없음
# 원소를 콤마로 구분하며 중괄호로 둘러싸 표현
# 인자는 리스트나 튜플의 항목으로 구성되어 집합생성
# list 대괄호 [] 사용, tuple은 []가 아닌() 사용

s=set()
print(type(s))

d={}
print(type(d))

print(set([1,2,3]))
print(set((1,2,2)))

planets = set('해달별')
fruits = set(['감', '귤'])
print(planets)
print(fruits)

# print(fruits[0]) # TypeError 순서가 없으면 접근 불가
