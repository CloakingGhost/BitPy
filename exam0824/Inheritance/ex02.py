class Car: # 부모클래스
    speed = 0
    
    def upSpeed(self,value): # 자식객체에서 overloading 할 예정
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" %self.speed)

class Sedan(Car):
     def upSpeed(self , value) : # overloading 
        self.speed += value

        if self.speed > 150 :  # 조건 이 추가되었음 , 프린트문도 바꿈
            self.speed = 150
            print("현재 속도(서브 클래스): %d"  %self.speed) 

class Truck(Car): # 부모객체의 속성을 그대로 사용함 따로 변한건 없다 다형성의 일종
    pass

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 -->", end="")
truck1.upSpeed(200)

print("승용차 -->", end="")
sedan1.upSpeed(200)
