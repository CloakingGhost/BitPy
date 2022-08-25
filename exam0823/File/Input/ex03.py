# 한번에 읽어오기
# \n을 만날때마다 리스트에 저장

inFile = None
inStr=""

inFile = open("e:\\temp/dorian.txt","r",encoding='utf-8')
inList = inFile.readlines() # 모든줄 읽어 리스트에 저장

print(inList)

inFile.close()