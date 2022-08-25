# p272 9-9

def multi(v1,v2):
    resultList=[]
    sum = v1+v2
    sub = v1-v2
    resultList.append(sum) # 비어있는 공간에 추가
    resultList.append(sub) # 값을 추가하는 메소드
    return resultList


print(multi(200,170))