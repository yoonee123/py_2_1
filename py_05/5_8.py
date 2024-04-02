# end = "" ,  한 줄에 모두 출력 (print로 줄바꿈된것을 한줄에 출력되도록 함
for i in range(1, 3, 1) :
    print("===> %d" % i)
    for j in range(1, 4) :
        print( "%d" % j, end = "", )
    print()
