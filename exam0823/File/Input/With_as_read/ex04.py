with open('e:/temp/dorian.txt','r',encoding='utf=8') as inFile:
    contents = inFile.read() # 글자수 읽어서 리스트에 저장 기준 \n
    word_list = contents.split() # 공백기준 단어의 수 \n은 단어와 붙어있어서 숫자를 증가시키지 않는다
    line_list = contents.split("\n") # 엔터마다 구분하여 행의 수를 확인할수 있다
    

print("총 글자 수 : ",len(contents))
print("총 단어의 수 : ",len(word_list))
print("종 행의수 : ",len(line_list))
# print(contents)
