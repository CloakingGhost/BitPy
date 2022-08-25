def print_info(name,age,address = "비밀"):
    print('이름 :',name)
    print('skdl :',age)
    print('주소 :',address)

print_info('conan',8,"Brown's")


def print_info(name,age,address = "비밀"):
    print('이름 :',name)
    print('skdl :',age)
    print('주소 :',address)

print_info('conan',8)


# SyntaxError: non-default argument follows default argument 발생
# 매개변수이 초가화되면 끝으로 가야함
# def print_info(name,address = "비밀",age):
#     print('이름 :',name)
#     print('skdl :',age)
#     print('주소 :',address)

# print_info('conan',8,"Brown's")