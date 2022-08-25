# w 기존파일을 삭제하고 새로씀
# a 기존파일에 입력내용 추가함

inFile = None
inStr = ""
# 파일객체 : 읽기모드로 연다
inFile = open("E:\\temp/dorian.txt","r",encoding = 'utf-8')

# 읽고
inStr = inFile.readline()
# 출력
print(inStr, end=" ")
# 읽고
inStr = inFile.readline()
# 출력
print(inStr, end=" ")
# 닫기
inFile.close()