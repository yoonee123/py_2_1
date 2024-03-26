# split() 문자열을 여러 문자열로 나누는 메소드
# 리스트[항목1, 항목2...]로 반환
# 공백은 whitespace(공백, 탭, 엔터)
st1='사과 배 복숭아 딸기'
print(st1.split())
st2='사과 100, 배 200, 복숭아 300, 딸기 50'
print(st2.split(','))


# center() 폭을 지정하고 중앙에 문자열 배치하는 메소드
# strip() 문자열 앞뒤의 특정 문자들을 제거하는 메소드
# lstrip()
# rstrip()
st1='python'
print('\n',st1.center(30,'*'))
print(st1.center(30))
print(st1.center(30,'='))
st3='***python---'
st4='   python   '
print('\n',st4.lstrip())
print(st4.rstrip())
print(st4.strip())
print(st3.strip('*'))
print(st3.strip('-'))
print(st3.strip('* -'))
