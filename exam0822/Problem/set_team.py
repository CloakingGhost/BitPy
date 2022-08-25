

import random


helpers = {1:'   이재현   ', 2:'   이윤후   ', 3:'   이주엽   ', 4:'   홍혁기   ', 5:'   이기태   '}
members = {1:'성유빈', 2:'이솔지', 3:'이  식', 4:'정성근', 5:'윤지훈', 6:'김대성', 7:'이정빈', 8:'신길호'}

helper = []
member = []

for select1 in helpers:
    choice = random.randint(1,5)
    while helpers[choice] in helper: 
        choice = random.randint(1,5)
    helper.append(helpers[choice])

print(helper)

for select2 in members:
    choice = random.randint(1,8)
    while members[choice] in member: 
        choice = random.randint(1,8)
    member.append(members[choice])

print(member)
    
    
    

