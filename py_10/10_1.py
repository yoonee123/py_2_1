# 함수 zip{}
# 몇 개의 리스트나 튜플의 항목으로 조합된 튜플을 생성
# 동일한 수로 이뤄진 여러 개의 튜플 항목 시퀀스를
# 각각의 리스트로 묶어주는 역할을 하는 함수

a=['ftp', 'telnet', 'dns']
b=(20,23,25)
print(zip(a, b))
z=list(zip(a, b))
print(type(z))
print(z)
print('---')
z2=tuple(zip(a, b))
print(type(z2))
print(z2)
print('---')
print(dict(zip(a,b)))
print('---')
print(list(zip('abcd', 'xy')))
print(tuple(zip('abcd', 'xy')))
print(dict(zip('abcd', 'xy')))