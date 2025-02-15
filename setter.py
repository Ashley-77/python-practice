class student():
    def __init__(self,name,gender,age):
        self._name=name#把形式变量引出来_preserved,only 本类、子类可访问
        self.__gender=gender#private 类本身可访问
        self.age=age#commom\
    #方法转为属性
    @property
    def gender(self):
        return self.__gender
    #可写edit
    @gender.setter
    def gender(self,value):
        if value!='male' and value!="female":
            print('error')
            self.__gender=('male')
        else:
            self.__gender=value
stu1 = student('jack', 'male', 20)
stu1.gender='female'#rewrite
print(stu1._name,stu1.gender)#without__