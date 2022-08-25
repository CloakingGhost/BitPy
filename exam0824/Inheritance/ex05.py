# unpublic field
class Knight:
    __item_limit=10 # 앞베 '__'을 붙혀주면 private속성과 비슷하게 변한다 직접접근이 불가하다

    def print_item_limit(self):
        print(Knight.__item_limit)

x= Knight()

x.print_item_limit()

print(Knight.__item_limit)