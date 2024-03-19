#bool형 true, false 두가지 값을 나타내는 자료
a=3>2
print(a)

a=2>3
print(a)
print(type(a))
print("==")
#논리연산자 not
b=not True
print(not True)
print(b)
b2=not 0
print(b2)

#산술연산 => 비교연산자 => 논리연산자
#and 연산자 결과 True, False
#or 연산자 결과 True, False
#비교연산자 ==, !=, >, >=, <, <=
print("==")
print(10>2 and 20>3)
print(10>2 and 20<3)
print("--")
print(10>2 or 20>3)
print(10>2 or 20<3)
print("--")
a=30
print(a == 10)
print(a != 10)
