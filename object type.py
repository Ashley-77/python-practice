#apart from subclass and superclass
#methods:__new__,call automatically\systematically\__init__,initialize the variable you create
#_str_
from PIL.ImageChops import subtract


class person:
    def __init__(self,name,age):
        self.name=name#the former one is variable
        self.age=age#give the fake variant a real entity
    def fun(self):
        print(f"halo,my name is{self.name}, i am {self.age}year old.")
        return
    def __str__(self):
        return "is me"
per1=person('lucy',12)
print(per1)#str ip inter storage.after define the str you can get more than ip
print(per1.__str__())#manual operation \calling
#__is special method you can substitute _+-= with__
a=10
b=39
print(a.__add__(b),a.__sub__(b))#subtract()
print(a.__eq__(b),a.__le__(b),a.__lt__(b))#less equal than\less than
print(a.__ge__(10),a.__gt__(3),a.__ne__(34))#larger than \not equal
print(a.__mul__(30),a.__truediv__(3),a.__mod__(3))#multiple\divide\reminder
print(a.__pow__(2))
print(a.__floordiv__(b))#exact division