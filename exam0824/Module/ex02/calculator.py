# 총점 평균 합격여부

def check(*scores):
    sum = 0
    ispass = "pass"

    for score in scores:
        sum += score

    avg = sum/len(scores)

    for score in scores:
        if score < 40 :  # 40보다 작으면 실행안함
                ispass = "fail"

    print("총점 : %d  평균 : %d 합격여부 : %s" % (sum, avg, ispass))
