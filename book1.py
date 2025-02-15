import random

s=set('12342122')#needs quotation mark
print(s)
s.add('lot')
for i in s:
    print(i*3)#default change the line
for item in set("hello world bye"):
    print(item,s|set('12'))
l=set()

for i in range(9):
    k = random.randint(1, 99)
    l.add(k)
print(l)#notice the sequence
p=set('2322223')
print(p)#no repeated ones
#集合能用来做并集补集等运算
