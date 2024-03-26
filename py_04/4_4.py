#체질량 지수(bmi) 키가 h 미터(m), 체중 w (kg)일 때

h, w = input('당신의 키와 몸무게를 입력하세요. : ').split()
height = float(h)
weight = float(w)
bmi = weight / (height/100)**2

print('키 : %.1f(cm) 몸무게 : %.1f(kg) bmi : %.1f' %(height, weight, bmi))
print('{} {}'.format('고도비만', 40 <= bmi))
print('{} {}'.format('중등도비만', 35 <= bmi < 40))
print('{} {}'.format('비만', 30 <= bmi < 35))
print('{} {}'.format('과체중', 25 <= bmi < 30))
print('{} {}'.format('정상', 18.5 <= bmi < 25))
print('{} {}'.format('저체중', bmi < 18.5))
