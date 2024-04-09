# + 연산자를 통한 리스트간의 결합
# 리스트내의 특정위치에 있는 데이터 변경
# b = [1,2,3,4,5]
# c = [6,7,8]

# print(b+c)

# print(b)
# b[2] = 20
# print(b)

# append() 리스트 끝에 새 요소를 추가
# extend() 기존 리스트에 다른 리스트를 이어 붙임
# a = ['red', 'green', 'blue']
# b = [1,2,3,4,5]
# c = [6,7,8]

# b.append(100)
# print(b)

# c.extend([4,5,6])
# print(c)

# d2 = [2,4,6]
# d2.insert(0,10)
# print(d2)
# b.insert(3,100)
# print(b)

# a.remove('green')
# print(a)

# pop() 리스트의 마지막 요소를 뽑아내며 리스트에서 제거
# pop(인덱스번호) 해당 인덱스 번호의 요소를 리스트에서 제거

# d4 = [1,2,3,4,5]
# d5 = [5,6,7,8]
# d4.pop()
# print(d4)

# d5.pop(2)
# print(d5)

# no_list = ['red', 'green', 'blue']
# while no_list :
#     print('{0}'.format(no_list.pop())) # pop으로 맨 마지막 문자열 뽑아서 첫 번째 열로 옮겨옴

# a=['book']
# b=list('book')
# c=list()

# print(a)
# print(b)
# print(c)
# c.append(123)
# print(c)

# index() 리스트내에서 매개변수로 입력한 데이터 추출
# 일치하는 데이터가 없을 경우 오류 발생
# count() 매개변수로 입력한 데이터와 일치하는 요소가 몇개인지 센다

# d6 =['red', 'green', 'blue']
# print(d6.index('green'))
# # print(d6.index('book')) # ValueError

# d7=[1,2,3,2,5,7,2]
# print(d7.count(2))
# print(d7.count(10)) # 인덱스가 없어서 0 출력

# sort() 리스트 내의 요소를 정렬
# 매개변수 reverse = True로 입력하면 내림차순 아무것도 입력 안하면 오름차순
# reverse() 리스트 내 요소의 순서를 반대로 변경
d8 = [3,1,20,6,15]
d8.sort()
print(d8)

d8.sort(reverse=True)
print(d8)

d9 = [3,4,5,1,2]
d10 = ['red', 'green', 'blue']

d9.reverse
print(d9)

d10.reverse()
print(d10)