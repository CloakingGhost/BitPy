
# 부모객체임
class Calculator:
    def __init__(self,num1,num2): # 자바로 하면 클래스의 속성값을 넣는것 
        print("===__init__() start===")
        self.num1 = num1 # 자바로 하면생성자 지정
        self.num2 = num2 # 즉 필드값과 생성자를 초기화 함수로 한번에 지정할수 있다

    def add(self): # 자바로 하면 메소드
        print("===add() start===")
        print("num1 + num2 = ", self.num1 + self.num2)
    
    def substract(self):
        print("===substract() start===")
        print("num1 + num2 = ", self.num1 - self.num2)

### 자식 파일에서 부모파일을 불러왔으므로 자식파일에서 메인 실행시
###  부모에서 적어놓은 모든 프린트문 메소드문도 같이 실행된다 / 저장까지 해야 된다
# cal1 = Calculator(10,20)

# cal1.add()
# print()
# cal1.substract() 

# print('cal1.num1',cal1.num1) # 필드값에 접근할수 있다
# print('cal1.num2',cal1.num2)
# cal1.num1 = 100              # 필드값을 변경할수 있다
# cal1.num2 = 200
# print('cal1.num1',cal1.num1)
# print('cal1.num2',cal1.num2)