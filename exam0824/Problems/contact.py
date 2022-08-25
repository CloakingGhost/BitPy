

class Member:
    member = []
    
    def __init__(self, name, phoneNo, addr):
        self.name = name
        self.phoneNo = phoneNo
        self.addr = addr

    
    def add_contact(self):
        # 값 3개 받아서 배열에 넣어
        self.name,self.phoneNo,self.addr = input("이름, 전화번호, 주소 순서대로 입력").split()
        self.member.append(self.name)
        self.member.append(self.phoneNo)
        self.member.append(self.addr)
    def search_number(self,name):
        for i in len(self.member):
            if self.member[i] == name:
                print( self.member[i], self.member[i+1], self.member[i+2])
    def remove_number(self,name):
          for i in len(self.member)-2:
            if self.member[i] == name:
                self.member.remove(self.member[i])
                self.member.remove(self.member[i+1])
                self.member.remove(self.member[i+2])
                i+=3  
    def number_list(self):
        print("목록에 저장된 회원 수는 %f명입니다." %len(self.member)/3)
    def save(self):

        with open("E:\\temp\\contact.txt",'w',encoding='utf-8') as outFile:
          for m in self.member:
            outFile.write(m + ',')
            



# data_check = data.split("\n")
# outFile = None
# outStr = ""
# outFile = open('e:/temp/test2.txt',"w",encoding='utf-8') # 아웃풋을 받을 파일 지정
# # with open('e:/temp/test2.txt',"w",encoding='utf-8') as outFile:
# while True:
#     outStr = input("내용 입력 : ") # 아웃풋할 내용 입력
#     if outStr !="":
#         outFile.writelines(outStr + "\n") # 입력한 내용을 파일에 저장
#     else :
#         break
# outFile.close()

# []

while True:

    print("============================================================================================")
    print("1.전화번호 추가|2.전화번호 검색|3.전화번호 삭제|4.전화번호 목록|5.파일로 저장|6.프로그램 종료")
    print("============================================================================================")
    select_menu = input("메뉴를 선택하세요 >>")
    
    if select_menu == '1':
        Member.add_contact(Member)
    elif select_menu == '2':
        name = input("검색할 이름을 입력하세요>>")
        Member.search_number(Member,name)
    elif select_menu == '3':
        Member.remove_number(Member)
    elif select_menu == '4':
        Member.number_list(Member)
    elif select_menu == '5':
        Member.save(Member)
    elif select_menu == '6':
        break
    else:
        print("메뉴를 다시선택해주세요~")
