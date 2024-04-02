#1 ~ 10 = 55
#11 ~ 20 = 155
#21 ~ 30 = 255
#...
#90 ~ 100 = 955
sum = 0

for i in range(10, 101, 10) :
    sum = 0
    for j in range(i-9,i+1) :
        sum = sum + j
    print("%d ~ %d = %d" %(i-9,i,sum))
