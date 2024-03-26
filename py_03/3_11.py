# find() 문자열 찾는 메소드 없으면 -1을 반환
# index() find와 같지만 찾는 메소드가 없으면 valueError 발생
st1='python'
st2='자바 C 파이썬 코틀린'
print(st1.find('h'))
print(st1.find('a')) 
print(st2.find('자바'))
print(st2.find('파이'))
print(st2.find('파이썬'))

print(st1.index('h'))
print(st2.index('파이'))
print(st1.index('a'))
