# count() 문자열 출현 수를 반환
# join() 문자열의 문자와 문자 사이에 원하는 문자열을 삽입
st1 = 'welcome'
st2 = '단순한 것이 복잡한 것보다 낫다'
num = '12345'
print(st2.count('복잡'))
print(st1.count('e'))
print(st1.count('a'))
print(st2.count('것'))

print('->'.join(st1))
print(' '.join(num))
print('aa'.join(num))
print('a'.join(num))
