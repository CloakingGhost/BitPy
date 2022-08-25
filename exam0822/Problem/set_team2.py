import random
# 이주엽님 작품 set을 사용
classmember = {'1','2','3','4','5','6','7','8'} # 반 인원 리스트 생성

group1 = random.sample(classmember, 2)
classmember = classmember - set(group1)
group2 = random.sample(classmember, 2)
classmember = classmember - set(group2)
group3 = random.sample(classmember, 2)
classmember = classmember - set(group3)
group4 = random.sample(classmember, 1)
classmember = classmember - set(group4)
group5 = classmember

print(group1)
print(group2)
print(group3)
print(group4)
print(group5)