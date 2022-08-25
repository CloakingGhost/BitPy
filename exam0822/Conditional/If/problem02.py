#103 참고
dic = {'conan': '1111', 'rose': '2222', 'ran': '3333'}

name = input()
pw = input()
if name in dic.keys() and dic[name] == pw:
    # print(dic[name]);print(pw)
    print("로그인에 성공하셨습니다.")
elif name in dic.keys() and dic[name] != pw:
    # print(dic[name]);print(pw)
    print("비밀번호를 확인하세요.")
else:
    print("등록된 회원이 아닙니다.")
