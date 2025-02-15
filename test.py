import random

from 初学.chapter4.book1 import p

for i in range(11):
    a=random.randint(1,100)
    print(a)
    s=[]
    s.append(a)
print(s)
list1=[random.randint(1,100) for i in range(10)]
print(list1)
def list_max(m):
    b=list1[0]
    for item in range(1,len(list1)):
        if list1[item]>b:
            b=list1[item]
        else:
            pass
    return b#when you use the function get what
print(list_max(list1))
print('￥'*30)
a=input("input a string")
b=list(a)#separate
print(b)
def lis(b):
    list1=[]
    for item in b:
         if item.isdigit():
            list1.append(int(item))
    y=(sum(list1))
    return list1,y
list1,s=lis(b)#一个形式变量但是有两个返回值，解包对应返回值个数
print(list1,s)
print(sum(list1))
print('#'*82)
s=[]
for i in range(0,len(b)):
    if b[i].isnumeric():
        s.append(b[i])
    else:
        pass
print(s)
def sum(a):
    for item in s:
        p=0
        p=+int(item)
    return p
print(p)
print(sum(s))




