# 거스름돈 계산
# 최고단위에서 밑단위까지 거스름돈 계산
#
#

stuff = int(input("물건값 입력:"))
pay = int(input("지불액 입력:"))
change = pay - stuff
change5000 = change//5000
change1000 = (change % 5000)//1000
change500 = (change % 6000)//500
change100 = (change % 6500)//100
change50 = (change % 6600)//50
change10 = (change % 6650)//10

print("거스름돈은 "+str(change)+"원이며, 5000원권"+str(change5000)+"개 1000원권 " +
      str(change1000) + "개 500원짜리 "+str(change500)+"개 100원짜리"+str(change100))
