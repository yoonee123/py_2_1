# 1. return문에 결과 데이터를 담아 실행 => 함수 종료되고 호출자에게 결과 전달
# 2. return문에 아무결과도 넣지않고 실행 => 함수 즉시종료
# 3. return문 생략 => 함수의 모든 코드가 실행되면 종료

def multiply(a,b):
    return a*b

result=multiply(2,3)
print(result)

# 결과 없는 return
def ogamdo(num):
    for i in range(1, num+1):
        print('제 {0}의 이해'.format(i))
        if i==5:
            return

ogamdo(3)
ogamdo(8)