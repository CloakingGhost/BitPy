# append 추가
with open('e:/temp/test2.txt',"a",encoding='utf-8') as outFile: # 받아적을 책을 펼쳐라
    for i in range(1,11):
        data = "%d번째 행\n" %i
        outFile.write(data) # 펼친 책에 써라
