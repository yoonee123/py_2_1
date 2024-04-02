#1 ~ 10 = 55
#1 ~ 20 = 210
#1 ~ 30 = 465
#...
#1 ~ 100 = 5050
sum = 0

for i in range(10, 101, 10) :
    sum = 0
    for j in range(1,i+1) :
        sum = sum + j
    print("1 ~ %d = %d" %(i,sum))
