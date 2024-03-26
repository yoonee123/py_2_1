str = input('다섯 문자 이상의 문자열 입력 >> ')
print('입력 문자열: %s' %str)
print('입력 문자열 길이: %d' %len(str))

print("첫 문자: %c" %str[:1])
print("마지막 문자: %c" %str[-1:])

print("첫 문자를 제외한 부분 문자열: %s" %str[1:])
print("마지막 문자를 제외한 부분 문자열: %s" %str[:-1])

print("맨 앞과 뒤 두 문자씩 제외한 부분 문자열: %s" %str[2:-2])

print("문자 하나씩을 건너 뛴 부분 문자열: %s" %str[::2])
print("역 문자열: %s" %str[::-1])

