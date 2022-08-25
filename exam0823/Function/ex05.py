# 초기화된 매개변수는 값을 지정해주지 않아도 함수를 실행하는데 에러가 없음
def para_function(num1,num2,num3=0):
    result =0
    result = num1+num2+num3
    return result

sum = 0
sum = para_function(10,20,30)
print("매개변수 3개 입력 = %d"%sum)
sum = para_function(10,20)
print("매개변수 2개 입력 = %d"%sum)