# 함수
def hello(): # 함수 정의
    print("hello world")
    
hello() # 함수 호출
# 함수의 매개변수
def print_string(text,count=2): 
    for i in range(count):
        print(text)
# main
print_string('안녕하세요')
print_string('수업중',3)

def print_string(text,count): #초기값이 없으면
    for i in range(count):
        print(text)
print_string('안녕하세요') # typeError
