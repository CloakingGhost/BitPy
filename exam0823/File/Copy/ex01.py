inFile,outFile = None,None

inStr =""
inFile = open('E:\\temp/test2.txt','r',encoding='utf-8')  # 읽을 파일을 연다
outFile = open('E:\\temp/test3.txt','w',encoding='utf-8') # 쓸 파일을 연다

inList = inFile.readlines() # 읽을 파일에 있는 모든 행을 리스트에 저장 \n기준으로저장
for inStr in inList: # 각 리스트의 원소를 문자열로 저장 문자열 안에 \n 존재하므로 자동 개행
    outFile.writelines(inStr) # 쓸 파일에 리스트의 있는 문자열을 기록한다
inFile.close()
outFile.close()
print("copy complete")