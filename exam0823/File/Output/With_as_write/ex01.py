outFile = open('e:/temp/test2.txt',"w",encoding='utf-8') 
for i in range(1,11):
    data = "%d번째 행\n" %i
    outFile.write(data)
outFile.close()
