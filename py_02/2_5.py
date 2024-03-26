# input() : 키보드로부터 입력받는 명령어
#,(콤마) 나열연산자
#"{0}{1}".format(변수1, 변수2) : 출력형식 장식하는 명령어

print("첫 번째 수를 입력하세요. : ")
a = input()
print("두 번쨰 수를 입력하세요. : ")
b = input()

result = int(a) * int(b)

print(a,"*",b,"=",result)
print("{0} * {1} = {2}". format(a, b, result))
