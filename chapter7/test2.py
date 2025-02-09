class car(object):
    def __init__(self,type,com):
        self.type=type
        self.com=com
    def start(self):
        print('i can start')
    def stop(self):
        print('i can stop')
        #two types of ways like branches
class taxi(car):
    def __init__(self,type,com,no):
        super().__init__(type,com)
        self.no=no
    def start(self):
        print(f'i am a taxi{self.no},{self.type}')#方法重写，改动父类内容
class car2(car):
    def __init__(self,type,com,no1):
        super().__init__(type,com)
        self.no1=no1
    def start(self):
        print(f"i am a family car{self.no1},i come from{self.com}")
taxi1=taxi('link','li',9)
car1=car2('vehicle','hi',00)
car1.stop()#不改变就是父类
taxi1.start()
print(car1.start())
