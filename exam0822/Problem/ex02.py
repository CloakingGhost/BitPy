num1 = int(input("구구단의 시작단 입력:"))
num2 = int(input("구구단의 끝단 입력:"))

for i in range(1,10):
    multi = ""
    if(num1<=num2):
        for j in range(num1,num2+1):
            multi +="%d * %d = %2d " %(j,i,i*j)
        
    else:
        for j in range(num1,num2-1,-1):
            multi +="%d * %d = %2d " %(j,i,i*j)
    print(multi)



# 요약

for i in range(1,10):
    multi = ""
    for j in range(num1,num2+1):
        multi +="%d * %d = %2d " %(j,i,i*j)
    print(multi)