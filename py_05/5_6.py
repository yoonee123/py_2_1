## 변수 선언 부분
money = 0
c=[500,100,50,10]

## 메인(main) 코드 부분
money=int(input("교환할 돈은 얼마 ? : "))

for i in range(0,4):
    tt = money / c[i]
    money = money % c[i]
    print("%d원 =>%d개 " %(c[i], tt))
print("바꾸지 못한 잔돈 =>%d원 " %money)
