import random

num = random.randint(1, 50)  # 1~50까지 임의의 수

set_bingo = []
# 배열의 수가 25개가 될때까지 반복
while len(set_bingo) < 25:
    #  배열에 있으면 새로 수를 구한다
    if num in set_bingo:
        num = random.randint(1, 50)
    # 배열에 중복된 수가 없으면 추가
    elif num not in set_bingo:
        set_bingo.append(num)


# for i in range(25):
#     num = random.randint(1, 50)
#     while num in set_bingo:
#         num = random.randint(1, 50)
#     set_bingo.append(num)
# print(set_bingo) 배열 확인용

#새로운 배열에 5개씩 넣고 출력후 배열을 비운다
bingo = []
for a in set_bingo:
    bingo.append(a)
    if len(bingo) == 5:
        print(bingo)
        bingo.clear()
