#try 절 안에 문제가 없을 경우의 코드 블록을 배치하고
#except 절에는 문제가 생겼을 떄 뒤처리를 하는 코드 블록 배치

try:
    print(1/0)
except:
    print("예외가 발생하였습니다")
    
#복수 개의 except 절 사용하기
my_list = [10, 20, 30]

try:
    print("첨자를 입력하세요:")
    index = int(input())
    print(my_list[index]/0)
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다. ({0})".format(err))
except IndexError as err:
    print("잘못된 첨자입니다. ({0})".format(err))
    
# else
# try절을 무사히 실행하면 만날 수 있는 else절

my_list = [1, 2, 3]
try:
    print("첨자를 입력하세요 : ")
    index = int(input())
    print("my_list[{0}]:{1}".format(index, my_list[index]))
except Exception as err:
    print("예외가 발생했습니다.[{0}]".format(err))
except:
    print("리스트 요소 출력에 성공했습니다")