#finally절
#어떤 일이 있어도 반드시 실행되는 finally
my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요:")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))
finally:
    print("어떤 일이 있어도 마무리합니다.")

#raise
#예외를 직접 일으킬 수 있음
def some_funtion():
    print("1~10 사이의 수를 입력하세요:")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception("유효하지 않은 숫자입니다. :  {0}".format(num))
    else:
        print("입력한 수는 {0}입니다.".format(num))
        
#main
try:
    some_funtion()
except Exception as err:
    print("예외가 발생했습니다 ({0})".format(err))