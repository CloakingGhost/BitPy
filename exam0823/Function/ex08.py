

def printAverage(*scores):
    print(type(scores))
    total=0
    cnt = len(scores)
    for score in scores:
        total += score
    print('총점 : ',total,'점')
    print('평균 : ',total/cnt,'점')


printAverage(80,90,100)
printAverage(64,16,45,8,78)
printAverage(90,80,40,60,30,10,80,50,60,70,80,40,50,55,75)
