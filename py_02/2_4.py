# 문자열[start:end:stop]
# step 간격 생략되면 1
# 음수일 경우 역순 문자열 반환

str = 'Python'
print(str[0:4:2])
print(str[::2]) # 2칸씩 띄면서 출
print(str[::3])
print(str[::-2])
print(str[::-3])
