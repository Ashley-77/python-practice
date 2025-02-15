#superclass and subclass
class person:
    def __init__(self,name,age):
        self.name=name#the former one is variable
        self.age=age#give the fake variant a real entity
    def fun(self):
        print(f"halo,my name is{self.name}, i am {self.age}year old.")
        return
class man:
    def __init__(self,gender):
        self.gender=gender
        print(self.gender)
class student(person):#inherit
    def __init__(self,age,name,number):
        super().__init__(age,name)
        self.number=number
        #rewrite so that we can print out additional information
    def fun(self):#the name should be the same
        print(f"halo,my name is{self.name}, i am {self.age}year old. i am{self.number}")

class teacher(person):
    def __init__(self, age, name, subject, gender):
        person.__init__(self,name,age)
        #find the superclass
        man.__init__(self,gender)
        self.subject=subject
stu1=student(10,'jacy',22)
teacher1=teacher(30,'lucy','English','male')
print(stu1.name,stu1.number)
print(teacher1.age,teacher1.subject,teacher1.gender)
print(stu1.fun)
stu1.fun()

#one subclass can inherit from multiple superclass
#as well as superclass
#rewrite
#special usage
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):#not function but class related to class
        self.age=age
        self.name=name
        print('')
a=A()
b=B()
c=C('kk',12)
print(c.__dict__)
print(a.__dict__)#via dictionary
print(a.__class__,b.__class__)
print(C.__class__,C.__base__,B.__bases__,C.__bases__)
print(A.__subclasses__(),C.__mro__)
