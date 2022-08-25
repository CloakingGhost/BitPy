outFile = None
outStr = ""
outFile = open('e:/temp/test2.txt',"w",encoding='utf-8') # 아웃풋을 받을 파일 지정
# with open('e:/temp/test2.txt',"w",encoding='utf-8') as outFile:
while True:
    outStr = input("내용 입력 : ") # 아웃풋할 내용 입력
    if outStr !="":
        outFile.writelines(outStr + "\n") # 입력한 내용을 파일에 저장
    else :
        break
outFile.close()