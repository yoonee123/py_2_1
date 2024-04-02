# 1+2+3+4+....>=100

hap, i = 0,0

for i in range(1,101) :
    hap = hap + i
    if hap >= 100 :
        break;

print("1~100의 합에서 최초로 100이 넘는 위치 : %d 합 : %d" %(i, hap))

# 1부터 100사이에 3의 배수만 출력하지 않고 나머지의 합 출력하기
hap, i = 0, 0

for i in range(1,101) :
    if i % 3 == 0 :
        continue
    hap = hap + i
print("1~100의 합계(3 제외) : %d" %hap)
