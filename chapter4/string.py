
# some operation to string
s1="happy winter solstice"
a=s1.upper()#/lower capital and small letter
print(a)
list2=s1.split('winter')#create a new list
print(list2[0], list2[1])#use index in list
#search
print(s1.count("w"),s1.index("i"),s1.find('i'))
print(s1.find('z'))
#print(s1.index('z'))#find and index,the former one will print-1,the latter one will print error(not found)
#judge prefix and suffix
print(s1.startswith('happy'))
print(s1.endswith("e"))
print('writing.folder'.endswith('folder'))
#replace
s2="happy today"
b=s2.replace('p',"b",1)#default all replaced
print(b)
#centered
print('winter solstice'.center(30,'$'))
print('   winter solstice    '.strip())
print('   winter solstice    '.lstrip())
print('   winter solstice    '.rstrip())#remove space key(blank)
print('winter solstice'.strip("ce"))
print(s1.strip('e'))#only two sides
#only strings can be linked with+
name="kiki"
age=19
score=100.00
print(name,age,score)#origin
print('her name is %s,age is %d,score is %.3f' % (name,age,score))#%formatting the strings,linking all types together
#adjust floating digit
print(f'name{name},age{age}')#formatting
print('name:{0},age:{2},score:{1}'.format(name,score,age))#corresponding index
print('{name},{age}'.format(name='ki',age=2))#like function has interaction
#address the content of a string
#aligning
k='trouble is a friend'
print('{0:$<30}'.format(k),'{0:#>40}'.format(k))#the former is left aligning
print('{0:$^30}'.format(k))#center and 30 unit,":" is introducer
print('winter solstice'.center(30,'$'))
#,seperator,三位一， 千位，thousand digit
print('{0:,}'.format(12348435.23084))#precision
print('{0:,}  ， {0:.3f}'.format(128435.2304))#会输出两个，实则是一个字符串
print('{0:.4}'.format(12348435.23084))
print('{0:.4}'.format('hidssdkfha'))#maximum
print("2 is{0:b},10 is {0:d},8 is {0:o}, 16 is{0:x}".format(143875))
#system/scale
p=58976.9273
print('{0:.3f},  {0:.3e},    {0:.3E},  {0:.3%}'.format(p) )#float has科学计数法和百分号
#joint
a='hello'
b='hi'
print(a,b)
print(a+b)
print('sdkl''dsfkl')#directly
print(''.join([a,b,'merci','bonjour']))
print('$$$'.join([a,b,'merci','bonjour']))
#formatting
print('{0},{1}'.format(a,b))
print('%s,%s' % (a,b))#%s,%t，%f appoint type
print(f'{a}  {b}')
#remove duplicates
s=('merry happy new year hao')
s1=''
for  items in s:
    if items not in s1:
        s1+=items
print(s1)
s2=''
for i in range(len(s)):#range is numerics
    if s[i] not in s2:#[]index
        s2+=s[i]
print(s2)
import plistlib
s3=set(s)
print(s3)#a set is disordered and unrepeated,need joint
list1=list(s3)
list1.sort(key=s.index)
print('  '.join(list1))
l='Always look\nthe bright side\n of life'
m='''Always beside
you 
and me.'''
print(l,
      m)
#three quotation mark also means ##
l='hacker is me'
print('a' in l)
print(l[0],l[0:3],l[:-3],l[2:3:9])#🔪在索引值的右边切下
print(l[slice(1,5)],l[1:5],l[slice(None,None,2)])
print(repr('22'))
#type exchange
print(float('3232'),int('2131'),str(213))
#a=int(input(""))#exchange for computing
print(l.replace('hacker','kilo'))
print('this is my{0}{1}'.format('book','!'))
l=l.replace('me','you')
l.split(",,")
print(l)
#string into list and then put them together
p=list(l)
p[0:6]='genius'
print(p,l)
l='$'.join(p)#choose the linking mark
print(l)
y=[[2,2,3],[99,2,0]]
print(y[1][0])
s='s,pa,m'
print(s.split(','))
print(s)





