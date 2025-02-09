#circle
import math
r=eval(input("radium"))
class circle():
    def __init__(self,r):
        self.r=r
    def parameter(self):
        return 2*(math.pi)* (self.r) #print what return what
    def area(self):
        return (math.pi)*r*r
a=circle(r)#you must create an object on the base of class sp that you can call it
print(a.parameter(),a.area())
print("$"*20)
class student():
    def __init__(self,name,age,score):
        self.name=a
        self.age=age
        self.score=score

    #实例方法，for print out
    def info(self):
        print(self.name,self.score,self.age)
list1=[]
for i in range(3):
    a=input("input your students:with$")
    a_list=a.split('$')#put a string into list
    stu=student(a_list[0],a_list[1],a_list[2])
    list1.append(stu)
print(list(list1))
for item in list1:
    item.info()
class instrument():
    pass
class piano(instrument):
    def sound(self):
        print("piano")
class violin(instrument):
    def sound(self):
        print("violin")#方法个性化重写
def play(a):
    a.sound()#unified here
pi=piano()
v=violin()
play(pi)
play(v)


