# format() 서식형 메소드
a,b = input('2개의 수 입력 : ').split()
a=int(a)
b=int(b)
print('{1},{0}'.format(a,b))
print('{2}년 {0}월 {1}일'.format(3,2,2023))
print('{0} {1} {1}'.format('abc','def'))
print('{} + {}={}'.format(a,b,a+b))
print('{0} - {1}={2}'.format(a,b,a-b))
print('{0} / {1}={2}'.format(a,b,a/b))
print('{0} / {1}={2:.3f}\n'.format(a,b,a/b))
print('%d / %d = %d' % (a,b,(a/b)))
print('%d / %d = %.2f' % (a,b,(a/b)))
