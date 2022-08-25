inFile = None
inStr=""

inFile = open("e:\\temp/dorian.txt","r",encoding='utf-8')
inList = inFile.readlines() # 모든줄 읽어 리스트에 저장

for inStr in inList:
    print(inStr,end="") # 리스트안의 있는 요소마다 이미 \n이 존재하기때문에 프린트로 문장열을 넣으면 자동으로 출력됨



inFile.close()