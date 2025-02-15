class person():
    def fun1(self):
        print('intellectual')
class animal():
    def fun1(self):
        print('speak less')
class ai():
    def fun1(self):
        print('wise')
#same function,
def fun(object):
    object.fun1()#linking
person1=person()
ani1=animal()
ai1=ai()
#calling
fun(person1)
fun(ani1)
fun(ai1)