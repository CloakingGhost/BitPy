# 2개정수 입력받고 사칙연산 결과를 리스트타입으로 반환

def cal():
    num1 = int(input("첫 번째 정수 >>"))
    num2 = int(input("두 번째 정수 >>"))
    
    result = [num1+num2,num1-num2,num1*num2,num1/num2]

    print("사칙연산 결과",result)
