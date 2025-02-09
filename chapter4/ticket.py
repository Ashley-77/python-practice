a={'G1001':['10:22','1.1'],
   'G1003':['10:30',"1.1"],
   'G1035':['19:33',"1.2"]}
print("车次    时间   日期")
for key in a.keys():#对应
    print(key,end="  ")#不换行
    for item in a.get(key):#according to key to get the value
        print(item,end="  ")
    print()#change another line,一次循环后
b=input('choose the one you want to take:')
c=input('write down the passenger:')
#to get the value by the key
d=a.get(b,"not exist")#is it can be got?
if d!="not exist":
    s=d[0],d[1]
    print(c,"you've tke the ticket",b,d)
    print(c,'you have buy the train numbered',s)
else:
    print('error')
#set={}#error,dictionary like this
s=set()
for i in range(3):#equal to (1,4)
    a=input("inout the name and his/her phone number")
    s.add(a)#not append
    print(s)
for item in s:
    print(item)#don't print set(s)
