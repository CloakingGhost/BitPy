# 방사선사 파일에서 49회차 응시자 선별하여 49_qualifier.csv/radio_applier.csv

# 라인카운터 , 헤더를 담을 리스트, 데이터 확인용 리스트, 확인된 데이터를 담을 리스트 , 조건식,
# 초기화 후 책을 펼치고 조건식 넣고 데이터 확인해서 맞으면 리스트에 넣고 넣은 리스트를 미리 만들어놓은 파일에 저장하고 확인

line_counter = 0
data_header = []
data_check = None
examinee_list = []

with open('C:/Users/BIT/Downloads/radio_applier.csv','r') as examinee_data:
    while True:
        data = examinee_data.readline()
        if data=="":
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            data_check = data.split(",")
            if data_check[2] == '49':
                examinee_list.append(data_check)
        line_counter += 1

    print("Header : ",data_header)
    for i in range(0,30):
        print(examinee_list[i])
    print(len(examinee_list))

        
with open("C:/Users/BIT/Desktop/49_qualifier.csv",'w',encoding="utf-8") as qualifier:    # 받아적을 책을 펼쳐라
    for examinee in examinee_list: # 데이터를 파일에 저장
        qualifier.write(",".join(examinee)+'\n') # join은 ,로 구분되는 문자열로 만듬