# p137 5-11

# 변수선언
selcet, answer, numSrt, num1, num2 = 0, 0, "", 0, 0

# 메인코드
num1 = input('숫자를 입력')
num2 = input('숫자를 입력')
d = input('기호를 입력')

if d == '+':
    print(num1+num2)
elif d == '-':
    print(num1-num2)
elif d == '*':
    print(num1*num2)
elif d == '/':
    print(num1/num2)
