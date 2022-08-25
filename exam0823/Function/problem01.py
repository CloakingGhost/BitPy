# 국영수과 총점과 평균
def total(*scores):
    
    sum=0
    for score in scores:
        sum+=score
    return sum

def average(*scores):
    return total(*scores)/len(scores)*1.0


kor = int(input("국어 점수 입력 :"))
eng = int(input("영어 점수 입력 :"))
math = int(input("수학 점수 입력 :"))
sci = int(input("과학 점수 입력 :"))

print("4과목의 총점은 %d 평균은 %.1f 입니다"%(total(kor,eng,math,sci),average(kor,eng,math,sci)))