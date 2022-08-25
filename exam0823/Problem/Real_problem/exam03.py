# 중환자실 20대 남성 추출 male_20.csv

line_counter = 0
data_header = []
data_check = None
sick_list = []

with open('C:/Users/BIT/Downloads/sick.csv','r') as sick_data:
    while True:
        data = sick_data.readline()
        if data=="":
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            data_check = data.split(",")
            if data_check[1] == '남' and (data_check[2] == '20~24세' or data_check[2] == '25~29세'):
                sick_list.append(data_check)
        line_counter += 1

    print("Header : ",data_header)
    for i in range(0,2):
        print(sick_list[i])
    print(len(sick_list))

        
with open("C:/Users/BIT/Desktop/male_20.csv",'w',encoding="utf-8") as qualifier:    # 받아적을 책을 펼쳐라
    for examinee in sick_list: # 데이터를 파일에 저장
        qualifier.write(",".join(examinee)+'\n') # join은 ,로 구분되는 문자열로 만듬