# 함수를 변수에 담아 사용하기 
def prn1_func(a):
    print(a)
    
p = prn1_func # ( ) 없이 함수 이름만 변수에 저장

p(123) # 변수 이름뒤에 () 를 붙여 함수 처럼 사용
p('abc')

# 함수를 변수에 담아 사용 2
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

flist=[plus,minus]
print(flist[0](1,2))
print(flist[1](1,2))

# 함수를 매개변수로 사용하기
def hello_korean():
    print('안녕하세요')
def hello_eng():
    print('hello')
def greet(hello):
    hello()    
def get_greet(where):
    if where=='K':
        return hello_korean
    else:
        return hello_eng

hello=get_greet('K')
hello()
hello=get_greet('E')
hello()