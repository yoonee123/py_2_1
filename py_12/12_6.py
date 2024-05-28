# readline() : 한 행씩 읽어옴
# readlines() : 파일의 내용을 통쨰로 읽어서 리스트에 저장
 
inFp = None 
inList = ""

inFp = open("C:/temp/data2.txt", "r", encoding='utf-8')

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")
    
inFp.close()