from time import localtime, strftime


# print("오늘 날짜 : %s" %strftime('%Y-%m-%d',localtime()))
# print("현재 시간 : %s" %strftime('%H:%M:%S',localtime()))
outStr = ""
print("----------------한 줄 일기----------------")
stop = True
while stop:
    menu = input("1.일기 작성|2.일기 보기|3.종료")
    if menu == '3':
        stop = False



    elif menu == '1':
        outStr = input("%s 일기를 작성하세요" %strftime('%Y-%m-%d',localtime()))
        with open('e:/temp/test1.txt',"a",encoding='utf-8') as outFile: # 받아 적을 책을 펴라 'a' 내용을 추가한다 'w'는 없애서 새로 작성
            if outStr !="": # 무엇인가 적었다면
             outFile.writelines("%s %s \n"%(strftime('%H:%M:%S',localtime()),outStr)) # 입력한 내용을 파일에 저장
            



    elif menu == '2':
        with open('e:/temp/test1.txt','r',encoding='utf-8') as inFile:
            contents_list = inFile.read() # 리스트에 저장
            print(contents_list) # 리스트 원소에 \n 포함되있다

    else: print("다시입력해주세요")