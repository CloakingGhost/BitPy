with open('e:/temp/dorian.txt','r',encoding='utf=8') as inFile:
    contents = inFile.read()
    print(type(contents), contents)

#파일 자동 닫기