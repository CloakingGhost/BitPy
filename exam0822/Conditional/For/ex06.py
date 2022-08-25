#p154~5 6-3/6-4
i, sum= 0,0

for i in range(501,1001,2):
    sum += i

print(sum)

i, sum , num= 0,0,0

num = int(input("값을 입력하세요 :"))

for i in range(1, num+1,1):
    sum += i
print(sum)