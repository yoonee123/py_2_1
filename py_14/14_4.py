#모듈 접근하는 두번째 방법
#from 기존 파일명 import 함수명

from calculator import plus, minus, multiply, divide

print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

print("----")

import calculator as c

print(c.plus(10, 5))
print(c.minus(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))