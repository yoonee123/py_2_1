# outFp=open("저장할파일경로및파일명", "W", encoding='utf-8')
# =>해당경로와 경로파일명에 저장
# outFp.writeIines(변수+"\n")
# =>변수에 저장된 내용을 줄바꿈해서 out.Fp에 저장

outFp = None
outStr = ""

outFp = open("c:/temp/data2.txt", "w", encoding='utf-8')
            
while True:
    outStr = input("내용 입력: ")
    if outStr != "" :
        outFp.writelines(outStr+"\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 저장됨. ---")
