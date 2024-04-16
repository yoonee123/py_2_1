# tuple unpacking 튜플의 각 요소를 여러개의 변수에 할당
b1 = 100, 200, 300
one,two,three = b1
print(one)
print(two)
print(three)

# 언패킹 실패 : 투플 요소수와 언패킹할 요소 수의 불일치
# one,two2 = b1 #value Error

# 언패킹을 이용한 변수 다중 할당
red, green, blue = 'seoul', 12.34, 123.234
print(red)
print(green)
print(blue)