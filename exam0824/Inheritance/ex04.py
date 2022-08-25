# p408 12-6

class Car :
    color = ""
    speed = 0
    count = 0
    
    def __init__(self):
        self.speed = 0
        Car.count+=1



myCar1,myCar2= None,None

myCar1 = Car()
myCar1.speed = 30
print(myCar1.speed,myCar1.count)

myCar2 = Car()
myCar2.speed = 30
print(myCar2.speed,myCar2.count)