# 컴퓨터와 수치 맞추는 게임
import random
tries = 0
guess = 0
answer = random.randint(1, 10)
print("1부터 10 사이의 숫자를 맞추세요.")
while guess != answer:
    guess = int(input('숫자를 입력하세요 : '))
    tries = tries + 1
    if guess < answer:
        print('낮음')
    elif guess > answer:
        print('높음')

if guess == answer:
    print('축하합니다. 시도횟수는 : ',tries)
else:
    print("정답은 :", answer)