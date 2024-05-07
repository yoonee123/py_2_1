# 가변 매개변수
# 입력 개수가 달라질 수 있는 매개변수
# * 를 이용하여 정의된 가변 매개변수는 튜플
def merge_string(*text_list):
    result=''
    for s in text_list:
        result=result+s
    return result

print(merge_string('red', 'green'))
print(merge_string('aaa','bbb','ccc'))
print(merge_string('dd','ee','ff','gg'))
print('---')
# 일반 매개변수와 함께 사용하는 가변 매개변수
def print_args(argc,*argv):
    for i in range(argc):
        print(argv[i])
    
print_args(3,"red1","red2","red3")
print('---')
# 가변 매개변수와 함께 사용하는 일반 매개변수
def print_args(*argv,argc):
    for i in range(argc):
        print(argv[i])
        
print_args("argv1","argv2","argv3",argc=3)
# print_args("argv1","argv2","argv3",3) # 오류 