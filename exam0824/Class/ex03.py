# p403~405 12-3~12-5 + p400 12-2




class Car:
    color = ""  # 필드값 초기화
    name = ""
    speed = 0

    # 생성자 4
    # def __init__(): 생성자 초기화값이 필요하지 않다면 기본생성자를 만들지 않아도 된다 만들면 오히려 에러를 일으킨다
         


    def __init__(self):  # 생성자 1
        self.color = "red"
        self.speed = 0

    def __init__(self, value1, value2):  # 생성자 2
        # self.color = "red" # 이곳에서 초기화를 하면 메인 실행시 값을 넣어도 변하지 않는다 / 맨위에 필드값 초기화도 무시
        self.color = value1
        self.speed = value2

    def __init__(self, name, speed):  # 생성자 3 / 생성자 초기화시 이 방법이 읽기 좋다 / 자바와 비슷
        self.name = name
        self.speed = speed

    def getName(self):  # getter
        return self.name

    def getSpeed(self):  # getter
        return self.speed

    def upspeed(self, value):  # setter
        self.speed += value

    def downSpeed(self, value):  # setter
        self.speed -= value

# 1~~~~~~~~~~~~~생성자 1
# myCar1 = Car()
# myCar2 = Car()

# print(myCar1.color,myCar1.speed)
# print(myCar2.color,myCar2.speed)


# 2~~~~~~~~~~~~~생성자 2
# myCar3 = Car("red",30)
# myCar4 = Car("blue",50)

# print(myCar3.color,myCar3.speed)
# print(myCar4.color,myCar4.speed)


# 3~~~~~~~~~~~~~생성자 3
# car1, car2 = None, None

# car1 = Car("Kia",3)
# car2 = Car("HD",90)

# print(car1.getName(),car1.getSpeed())
# print(car2.getName(),car2.getSpeed())


# 4~~~~~~~~~~~~~ 생성자 4 / 위에 생성자 순서 일부러 꼬아놓은거임
# car3 = Car()
# car3.color = "red"
# car3.name = "Ray"
# car3.speed = 91

# print(car3.color,car3.name,car3.speed)