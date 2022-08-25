# return을 만나면 뒤에있는 명령을 무시하고 호출한곳으로 이동한다

def increaseStar():
    print("*")
    print("*")
    print("*")
    print("*")
    return
    print("*")
    print("*")
    print("*")

increaseStar()
