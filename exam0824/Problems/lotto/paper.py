# 1~45까지 6개 정수
# 컴퓨터에게 미리 6개 저장
# 사용자에게 6개 받아서 확인
from random import randint

def ShowMeTheMoney():
    cmp = set()
    myLuck = set()
    check = []
    while len(cmp)<6:
        cmp.add(randint(1,45))
    
    for i in range(1,7):
        # myLuck.add(int(input('Number %s : '%i))) # 수동입력
        myLuck.add(randint(1,45))  # 자동입력

    cmp = list(cmp)
    myLuck = list(myLuck)
    for cmpNum in cmp:
        if cmpNum in myLuck:
            check.append(cmpNum)

    print("이번주 당첨 로또 번호 : ",cmp)
    print("내가 선택한 로또 번호 : ",myLuck)
    print("일치하는 숫자 : ",check)
#     return ""
    
# dic = {1:ShowMeTheMoney}

# print (dic[1]())