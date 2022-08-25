def discount():
    basket=[]
    rate = 0
    sum = 0
    stop = True
    while stop :
        choice = int(input("상품을 구매하시겠습니까? 1.구매 2.종료"))
        if choice == 1:
            stuffPrices = int(input("구매한 상품의 금액을 입력하세요>>"))
            basket.append(stuffPrices)
        
        if choice == 2:
            for price in basket:
             sum += price

            if len(basket) == 0:
                rate = 0
            elif len(basket) == 1:
                rate = 5
            elif len(basket) == 2:
                rate = 10
            elif len(basket) == 3:
                rate = 20
            elif len(basket) > 3:
                rate = 30

            result = sum*(100-rate)/100
            
            print('''
            할인율 : %d %s
            총합계 : %d 원
            지불액 : %.0f 원
            '''%(rate,"%",sum,result))
            stop = False
