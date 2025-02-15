from audioop import reverse

from lxml.html.defs import link_attrs

print(bool([]),bool({}),bool(tuple()),bool(list()))
list1=[9,2,83,84]
print(list1,type(list1))
print(list1,str(list1),type(str(list1)))
print(int(input('num'))+int(920)+float(39)+int(92.03))
print(float('29'))
print(int('30'))
l='halo'
print(list(l))
u=range(1,9)
print(tuple(u),list(u),set(u),end='\n')
print("*"*40,'mathematics')
print(abs(9)+abs(-2))
print(max(3,5,2,67,2),min(23,54,6,7))#min([2,'33','halo',9]))#int and str can not be compared
print(max('halo'))#ascll code
print(divmod(29,3))#quotient and remainder
print(round(923.32),round(392.9),round(29.3930,2),round(382.39,-2))#remain digit
print(pow(4,8),pow(2,16),pow(2,10))
print(sum([2,5,3,5]))#make it a set so that you can gather then together
print('$'*30,'iterator')
list2=[2,54,6,3,7,4,67,3]
print(list2)
list3=sorted(list2,reverse=True)#descent
list4=reversed(list3)
print(list(list4))
#zip
a=[1,2,4,53,]
b=['first','second','third',' ']
s=zip(a,b)#mapping
print(s,list(s))
v=zip(a,b)
#enumerate
d=enumerate(a,start=2)
print(type(d),d,list(d))#use list as a transmitter
#all and any
print(all(a),all(b))
print(any(a),any(b))
#next
print(next(v))
print(next(v))
#filter
def fun(y):
    return y%2==0
k=filter(fun,range(11))#if the result is true then is will be stored in k
print(list(k))
#map
def low(l):
    return l.lower()
list5=['apple','SAla','sda']
p=map(low,list5)
print(list(p))
#other
print(len(list5),)
print(format('sdj','30'),format('kk','$<90'))#left right middle and the marks
print(format(293.32,'.2f'))
print(format(23,'b'),format(23,'x'))#o b x X
print(id(p))
print(eval('30+3'))
print(f'i am {20/7:.2f}years old')