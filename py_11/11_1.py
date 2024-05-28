# 변수는 자신이 생성된 범위 안에서만 유효
# 지역변수 : 함수 안에서만 살아있다가 함수코드의 실행이 종료되면 역할 끝
#           파이썬은 함수안에서 사용되는 모든 변수를 지역변수로 간주
# 전역변수 : 프로그램이 살아있는 동안 동작하다 프로그램이 종료되면 소멸
#           전역변수를 사용하기 위해서는 global 키워드 이용

def scope_test():
    global a
    a=1
    print('a:{0}'.format(a))
    
a=0
scope_test()
print('함수 밖 a:{0}'.format(a))

# 1. return문에 결과 데이터를 담아 실행 => 함수 종료되고 호출자에게 결과 전달
# 2. return문에 아무결과도 넣지않고 실행 => 함수 즉시종료
# 3. return문 생략 => 함수의 모든 코드가 실행되면 종료

def multiply(a,b):
    return a*b

result=multiply(2,3)
print(result)