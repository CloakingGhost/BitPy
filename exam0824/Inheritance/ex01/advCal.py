from cal import Calculator # cal.py파일에 있는 Calculator클래스를 불러온다


# 자식 객체임
class AdvancedCalculator(Calculator):
    def pow(self):
        print("=== pow() start ===")
        print("num1^num2 = ",self.num1 ** self.num2) # self.num1 과 self.num2 는 Calculator 클래스에 있는 인자이다

myCal = AdvancedCalculator(4,2)
myCal.pow()
myCal.add() # 부모의 function 사용가능하다

### 자식 파일에서 부모파일을 불러왔으므로 자식파일에서 메인 실행시
###  부모에서 적어놓은 모든 프린트문 메소드문도 같이 실행된다 / 저장까지 해야 된다






# https://hanyeop.tistory.com/6  공부해라
# 컴파일러는 소슼드를 기계어로
# 인터프리티는 번역없이 바로 실행
# 하지만 Python은 *.py 파일을 실행시킬 때 내부적으로 아래 두 단계를 거칩니다.
# *.py를 Python Virtual Machine(PVM)이 이해할 수 있는 Byte codes 형태로 컴파일
# 컴파일된 Byte codes를 PVM이 단계별로 실행