# instr = inFp.readline()
# => 한줄씩 읽어옴

inFp = None #입력 파일
inStr = "" #읽어온 문자열
inFp = open("C://temp/data2.txt","r", encoding="utf-8")

inStr = inFp.readline() #한줄 읽어옴
print(inStr, end="")
inStr = inFp.readline() 
print(inStr, end="")
inStr = inFp.readline() 
print(inStr, end="")

inFp.close