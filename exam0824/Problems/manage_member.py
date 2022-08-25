

class Members:
    userId =""
    userPwd =0

    def __init__(self,userId,userPwd):
        self.userId = userId
        self.userPwd = userPwd

class MemberManage(Members):
    # def __init__(self):
    #    self.userId = Members.userId
    #    self.userPwd = Members.userPwd
        
    
    members={}  
    def addMember(self,Members):
        self.userId = Members.userId
        self.userPwd = Members.userPwd
        self.members[self.userId] = self.userPwd
        
        print(self.userId,"님 가입 축하드려요")


    def loginMember(self,userId,userPwd):
        if userId in self.members.keys() and self.members[userId] == userPwd:
            # print(dic[name]);print(pw)
            print("로그인에 성공하셨습니다.")
        elif userId in self.members.keys() and self.members[userId] != userPwd:
            # print(dic[name]);print(pw)
            print("비밀번호를 확인하세요.")
        else:
            print("등록된 회원이 아닙니다.\n 가입해주세요!")


    def removeMember(self,userId,userPwd):# 조건 받고 삭제
        if userId in self.members.keys() and self.members[userId] == userPwd:
            del self.members[userId]
            print(userId,"님이 탈퇴했음")


    def printMembers(self):
        print("===== 전체 회원 =====")
        for member in self.members.keys():
            show =""
            show += "ID : %s / PWD : %s" %(member,self.members[member])
            print(show)
            print("--------------------")

# conan = Members('conan',1111)
# conan = MemberManage.addMember(Members('conan',1111))
# rose = MemberManage.addMember(Members('rose',2222))
ran = Members('ran','3333')
rose = Members("rose", '2222')
conan =Members("conan", '1111')

MemberManage.addMember(MemberManage,ran)
MemberManage.addMember(MemberManage,rose)
MemberManage.addMember(MemberManage,conan)
# MemberManage.printMembers(MemberManage)
MemberManage.loginMember(MemberManage,'ran','3333')
MemberManage.removeMember(MemberManage,'ran','3333')


# MemberManage.addMember(Members('ran',3333))

# emberManage.addMember(MemberManage, Member("conan", 1111))
# MemberManage.addMember(MemberManage, Member("rose", 2222))
# MemberManage.addMember(MemberManage, Member("ran", 3333))
# idList = list(MemberManage.members.keys())
# idList2 = []

# # 출력문
# MemberManage.printMembers(MemberManage)







# 저장시 ,로 구분