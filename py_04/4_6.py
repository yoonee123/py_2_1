#정수의 홀수와 짝수 판정
n = int(input('정수 입력 : '))
#n = 10
if n%2 == 0:
    print('%d는 짝수입니다.' %n)
else:
    print('%d는 홀수입니다.' %n)

# if, elif, else
print ('수를 입력하세요 : ')
a = int(input())

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수')
elif a > 10 and a % 2 != 0:
    print('10보다 큰 홀수')
elif a % 2 == 0:
    print('10이하의 짝수')
else :
    print('10이하의 홀수')

if a > 10 :
    if a % 2 == 0:
        print('10 > 짝수')
    else :
        print('10 > 홀수')
else :
    if a % 2 == 0:
        print('10 < 짝수')
    else :
        print('10 < 홀수')
