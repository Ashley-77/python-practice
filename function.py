#once compile, multiple usages
def get_sum (num):#define the function name and fake parameter
    s=0
    for i in range(1,num+1):
        s+=i
    print(s)
print(get_sum(99))#actual parameter
b=eval(input('number'))#input is str by default
a=get_sum(b)
print(a)

#parameter
def birthday(name,age='3',spot='los'):#spot parameter must in the front of the syntax
    print('happy'+name+age+spot)#notice the corresponding numbers
birthday(spot='',name='',age=''),#by sequence or using the key
#default parameter
#如果你不自动传参，会用默认值 spot\key\default parameter
birthday('kiki',spot="am")
#quatity changeable parameter
def oop(*number):
    print(list(number))
s=eval(input('2:'))
print(oop(s))
oop(22,00,222)
oop([99,432,2])
def opp(**words):
    print(type(opp))
    for key,value in opp.items():
        print(key,'----',value)
opp(name='kiki',age=22,weight=29)#define your key
