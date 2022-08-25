with open('e:/temp/dorian.txt','r',encoding='utf=8') as inFile:
    i=0
    while True :
        line = inFile.readline()
        if line=="":
                break
        print(str(i)+". "+line.replace("\n",""))
        i+=1


