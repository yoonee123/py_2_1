#index(): 입력한 데이터와 일치하는 튜플 내 요소의 첨자를 알려줌
# 찾고자하는 데이터와 일치하는 요소가 없으면 에러발생
a2=('abc', 'def', 'ghi')
print(a2.index('def'))
# print(a2.index('aaa')) # ValueError

# count() : 매개변수로 입력한 데이터와 일치하는
# 요소가 몇개 존재하는지
a3 = (1,100,2,100,3,100)
print(a3.count(100))
print(a3.count(10))