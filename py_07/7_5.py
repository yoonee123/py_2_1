i, k, ch, starNum = 0, 0, 0, 0
numStr, starstr = "", ""
## 메인 코드 부분
numStr = input("숫자를 여러개 입력하세요 : ")
print("")
i=0
ch = numStr[i]
while True:
    starNum = int(ch)
    starStr = ""
    for k in range (0, starNum) :
        starStr = starStr + "\u2665"
        
    print(starStr)
        
    i = i + 1
    if(i > len(numStr)-1) :
         break
    ch = numStr[i]