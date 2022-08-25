def calculator(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    return result


operator, num1, num2 = 0, 0, 0
operator = input("계산선택(+,-,*,/)")
num1, num2 = int(input("첫번째 숫자")), int(input("두번째 숫자"))
result = calculator(num1, operator, num2)
print(result)
