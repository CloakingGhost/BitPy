class Person:
    pocket=[] #값을 공유하기때문에 누구를 불러도 모든 값이 나온다 

    def put_pocket(self,stuff):
        self.pocket.append(stuff)


    

# main

conan = Person()
conan.put_pocket("smart_phone")

rose = Person()
rose.put_pocket("a_book")

# 프린트 시 배열으 공유하기 때문에 모든 자료가 나온다 따로
# 만드려면 아래와 같이 하자
print("coana :",conan.pocket)
print("rose :",rose.pocket)
print("Person :",Person.pocket)

# 한줄 띄우기 구분공란
print()

# 수정
conan = Person()
conan.pocket = []
conan.put_pocket("smart_phone")

rose = Person()
rose.pocket = []
rose.put_pocket("a_book")

print("coana :",conan.pocket)
print("rose :",rose.pocket)
print("Person :",Person.pocket) # 모든 물건을 확인하고 싶다면 클래스안에 있는 필드를 호출해야 확인가능하다

