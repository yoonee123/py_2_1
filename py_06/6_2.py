while True :
    print('반복을 계속할까요? [예/아니오] : ')
    answer = input()

    if answer == "예":
        num=int(input("1부터 합을 낼 수치를 입력 : "))
        i=1
        sum=0
        while i<=num:
            sum = sum+i
            i= i + 1
        print("1부터",num,"까지의 합 : ",sum)
    elif answer == "아니오" :
        break
    else :
        print("정상적인 답변이 아닙니다.")

print('반복이 종료되었습니다.')