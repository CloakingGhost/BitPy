# 공공데이터를 확인하는 방법 /엑셀, 노트패드++로 확인이 가능하다
# 많은 양의 데이터를 관리하는 방법

line_counter = 0 # 첫번째 줄
data_header = [] # 헤더를 따로 저장 / 필요한 부분과 아닌부분을 나눌수 있어야한다
customer_list = [] # 헤더를 제외한 필요한 데이터를 저장

# 읽을 책을 펼쳐라
with open("C:/Users/BIT/Downloads/customers.csv",'r',encoding="utf-8") as customer_data:
    while True:
        data = customer_data.readline() # 한줄씩 읽으려무나

    # 읽은걸 저장하는데 조건 3가지 1. 더이상 내용이 없을때 (data=="")2. 헤더일때 3. 나머지 원하는 데이터
    # 여기서 부터 원하는 정보를 뺀다
        if data == "":
            break
        if line_counter == 0:
            data_header = data.split(",") # 원문의 데이터가 , 로 이루워져있음 그러니 쪼개서 리스트에 저장
        else :
            customer_list.append(data.split(","))
        line_counter += 1 # 계속 읽어야 하니까 else에 넣는 것이 아님 넣을거면 모든 조건에 다 넣어야 됨 특정 조건에서만 카운터를 올리면 그때만 다음줄을 읽기 때문


        # 여기서부터 저장된 데이터를 출력
print("Header : ",data_header)
for i in range(0,10):
    print("Data",i,":",customer_list[i])
print(len(customer_list))


