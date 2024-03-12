'''
변수 distFromSun에 지구에서 태양까지의 거리인 149600000을 저장
변수 distFromMoon에 지구에서 달까지의 거리인 384400을 저장
지구에서 태양까지의 거리를 출력
지구에서 달까지의 거리를 출력
변수 ration에 distFromSun이 distFromMoon의 몇 배인지 계산
변수 ration를 정수로 출력
'''

distfromsun = 149600000
distfrommoon = 384400
print(distfromsun)
print(distfrommoon)
ration = distfromsun / distfrommoon
print(int(ration))

a = int(input())
b = int(input())
print('입력한 값',a,'(실수형)몫',b,'은 :',a/b)
print('입력한 값',a,'나머지',b,'는 :',a%b)
print('입력한 값',a,'(정수형)몫',b,'은 :',a//b)
print('입력한 값',a,'제곱',b,'는 :',a**b)
