# 의사시험에서 '의학총론' 이 포함된 항과 과목별 점수를 intro_score.csv 로 연도 포함 저장 / 연도 과목명 과목별점수

line_counter = 0
data_header = []
data_check = None
doctor_list = []
temp = []

with open('C:/Users/BIT/Downloads/doctor.csv','r') as doctor_data:
    while True:
        data = doctor_data.readline()
        if data=="":
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            data_check = data.split(",")
            if '의학총론' in data_check[4] :
                doctor_list.append(data_check)
                
        line_counter += 1

    print("Header : ",data_header)
    for i in range(0,100):
        print(doctor_list[i])
    print(len(doctor_list))

        
with open("C:/Users/BIT/Desktop/intro_score.csv",'w',encoding="utf-8") as qualifier:    # 받아적을 책을 펼쳐라
    for examinee in doctor_list: # 데이터를 파일에 저장
        qualifier.write(examinee[0]+","+examinee[4]+","+examinee[5]+'\n') # join은 ,로 구분되는 문자열로 만듬