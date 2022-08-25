import os
if not os.path.isdir('C:/log'):
    os.mkdir('c:/log')
if not os.path.exists('c:/log/mylog.txt'):
    with open('c:/log/mylog.txt','w',encoding='utf-8') as outFile:
        outFile.write('기록시작\n')
with open('c:/log/mylog.txt','a',encoding='utf-8') as outFile:
    import random,datetime
    for i in range(1,11):
        timestamp = str(datetime.datetime.now())

        num = random.randint(1,100)
        log_line = timestamp + "\t"+str(num)+" 생성"+"\n"
        outFile.write(log_line)