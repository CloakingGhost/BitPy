
inFile = None
inStr = ""
# 파일객체 : 읽기모드로 연다
inFile = open("E:\\temp/dorian.txt","r",encoding = 'utf-8')

while True :
    inStr = inFile.readline() # 한줄씩 읽는다
    if inStr=="":
        break
    print(inStr,end="")

# 닫기
inFile.close()