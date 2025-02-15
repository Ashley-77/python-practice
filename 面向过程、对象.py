#对象的搭建有一个个过程组成，基本型原理就是靠过程慢慢变成大对象的
#一切皆是对象type——class定义
class person():
    pass
class teacher():
    pass
#input some variants
a=person()
print(type(a))
#the component of class
#the former 2 way 类方法 类属性，打点调用，或是用对象名调用
class student:
    school='eson'#attribution of class out of function
    def __init__(self,name,age,country):#self called automatically,use init
        self.name=name#打点调用,left is 实例属性
        self.age=age
        self.country=country
    def introduce(self):
        print('my name is{self.name} and i am {self.age}year old now')
    @staticmethod#静态方法
    def fun2():
        print("can not invoke")
    @classmethod#类方法
    def fun3(cls):
        print("can not be called")
person1=student('Alice',11,'Belgium')#via variant to use the class
print(person1.age,person1.country)#对象调用
print(person1.introduce())
#functions in class are called methods
#decorator
print(student.fun3())#类名调用
print(student.fun2())
stu1=student('marry',22,'us')
stu2=student('canny',29,'UK')
#class is module, you can create object
print('$'*30)
#动态绑定
stu1.gender='female'
print(stu1.gender)#like append
def fun3():
    print('halo')
stu2.fun=fun3
print(stu2.fun())