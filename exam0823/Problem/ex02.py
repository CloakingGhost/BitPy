
# 상품 진열
priceList = {'쌀':9900,'상추':1900,'고추':2900,'마늘':8900,'통닭':5600, '햄':6900, '치즈':3900}


def getDiscountPrice(rate):
    new = {}
    new.update(priceList)
    
    for key in new.keys():
        new[key] *= (100-rate)/100
    
    return new # 할인율 적용한 배열을 리턴




def printPrice(priceList):
    rate = int(input("오늘의 할인율을 입력하세요>>"))
    new = getDiscountPrice(rate)
    for price in priceList:
        print('%s : %s 원 %d %s -> %d'%(price,priceList[price],rate,'%DC',new[price]))


printPrice(priceList)


























# def getDiscountPrice(rate):
#     new={}
#     new.update(priceList)

#     discountPrice = (100-rate)/100
#     for key in new.keys():
#         new[key] *= discountPrice

#     return new


# def printPrice(priceList):
#     rate = int(input("오늘의 할인율을 입력하세요>>"))
#     new = getDiscountPrice(rate)
#     for price in priceList.keys():
#         print("%s : %s 원 %s %s -> %.0f 원"%(price,priceList[price],rate,"%DC",new[price]))


# printPrice(priceList)