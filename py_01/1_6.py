#두수 입력받아 +,-,*,/ 결과값 출력 이때 실수는 소숫점 첫째자리까지
print("첫 번째 수를 입력하세요.")
a = input()
print("두 번째 수를 입력하세요.")
b = input()

add = int(a) + int(b)
sub = int(a) - int(b)
mul = int(a) * int(b)
div = int(a) / int (b)

print(a,"+",b,"=",add)
print(a,"-",b,"=",sub)
print(a,"*",b,"=",mul)
print(a,"/",b,"=",div)
print(a,"/",b,"=","%7.1f" %div)
