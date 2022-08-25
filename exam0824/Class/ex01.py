class FishBread:
    def __init__(self,f,b): # 초기화  self는 클래스 자신을 가리킨다 첫번째 매개변수를 self로 지정
        self.flour = f
        self.red_bean = b
    
    def makeFishbread(self):
        print('붕어빵 제조')