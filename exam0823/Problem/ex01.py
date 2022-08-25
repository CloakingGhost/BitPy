stop = True
count = 0
while stop:
    choice = int(input("1.웹사이트 방문 2.종료>>"))
    if choice == 2:   
        stop = False
        continue
    count+=1
    print("누적 방문 횟수 : %d" %count)