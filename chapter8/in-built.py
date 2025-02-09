import random
random.seed(10)#same seed leads to the same random number
print(random.random())
print(random.random())
print('$'*72)
random.seed(1)
print(random.randint(1,10))#including10
for i in range(10):
    print(random.randrange(1,100,5))#retract
print(random.uniform(1,29))
random.seed(2)#means fixed
print(random.uniform(1,29))
print(random.uniform(1,32))
print('$'*72)
list1=[i for i in range(1,20)]
print(random.choice(list1))#pick out randomly
#quene randomly
random.shuffle(list1)
print(list1)
#time
import time
a=time.time()
print(a)
b=time.localtime()#the exactly time and days from 1.1
print(b)
c=time.localtime(20)
print(b.tm_year,b.tm_mon,b.tm_hour,b.tm_gmtoff,b.tm_wday)#wday [0,6]
print(c)
print(time.ctime())
print(time.strftime('%Y.%m.%d',time.localtime()))
print(time.strftime('%H.%M.%S-%Y',time.localtime()))
print("%A day:",time.strftime('%A',time.localtime()))#A day
print("%B month:",time.strftime('%B',time.localtime()))#B month
print(time.strptime("2008-1",'%Y-%d'))#reverse
time.sleep(1)
print('hi')
from datetime import datetime
a=datetime.now()
print(a)
print(datetime.now())
x=datetime(2005,11,29,11,30,00)
print(x,type(x))
print(x.date(),x.hour)#extract
print(x>a)
print(x.strftime('%Y.%m.%d,%H:%M:%S'))
#change string to date
y='2022年11月20日'
z=datetime.strptime(y,'%Y年%y月%d日') #strptime vs str f time contrary
print(z)
print('$'*23)
#time delta
from datetime import timedelta
delta1=datetime(2020,11,20)-datetime(2030,12,20)
print(type(delta1),delta1)#you can subtract and add
dt1=timedelta(11)
print(type(dt1),dt1)
now1=datetime.now()
print(now1+dt1)#means interval
#python -m pip install--upgrade pip windows+r:cmd