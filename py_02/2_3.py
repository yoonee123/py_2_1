a="col'o'r"
b='co"lo"r'

print(a)
print(b)

#len() 문자열의 길이 반환
#슬라이싱(slicecing) 전체에서 일부분을 참조
#str[start:end] 문자열 str에서 start 첨자에서 end-1 첨자까지 문자열 반환
str = 'Monty Python'
print(len(str))
print(str[0:5],str[0:3],str[-6:],str[6:12])
print(str[-12:-7],str[-6:])
