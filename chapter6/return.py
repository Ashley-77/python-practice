#function is realtime ,so you need to store it


def sum(a,b):
    return(a*b)
print(sum(11,33))
print('_'*43)
def sum(a,b):
    print(sum(11,33))#won't print out
#or
def cal(a,b):
    s=b*a#all are fake
    v=a*b#a b is tuple can't connect to a int
    return s,v
print(cal(1,cal(2,9)))
s,v=cal(3,cal(3,9))#解包赋值，对应个数与变量unpack
print(s,v)
#whole situation and part variant.if outside the def function
print('--'*20)
a=99
def com(x,y,z):
    d=x+y*z
    a=200
    k=a*z
    return x,y,d,k#the numbers wanted to print out
print(com(1,4,22),a)#运算时a是内部的，局部的，输出就不是了
print(a)



