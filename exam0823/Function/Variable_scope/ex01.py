def function1():
    a = 10 #local variable
    print("function1()에서 a= %d" %a)
    
def function2():
    global a #global variable
    a = 10
    print("function2()에서 a= %d" %a)

def function3():
    print("function3()에서 a= %d" %a)


a = 20 #global variable # function2() global variable로 인해 위에서 먼저 선언된 a=10 이 사용됨
function1()
function2()
function3()