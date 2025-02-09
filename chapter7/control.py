#封装、继承、多态【面向对象的特征】
#封装，下划线_____
class student():
    def __init__(self,name,gender,age):
        self._name=name#把形式变量引出来_preserved,only 本类、子类可访问
        self.__gender=gender#private 类本身可访问
        self.age=age#commom
    def _fun1(self):
        print("itself and subclass")
    def __fun2(self):
        print('only itself')
    def fun(self):
        self._fun1()
        self.__fun2()
        print(self.age,)
        print(self.__gender)
        print(self._name)
stu1=student('max','ca',92)
print(stu1._name)
#print(stu1.__gender)#unuse
print(stu1._fun1())
#print(stu1.__fun2)
#how to visit, use a specific way
print(stu1._student__gender)
stu1._student__fun2()
print(dir(stu1),end="\n")
#setter of attribute
