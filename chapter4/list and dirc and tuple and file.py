print(c*3 for c in 'spam')
print(i*8 for i in ['hi','hello'])
Di={'name':'jack','relation':'cousin'}
print(Di['relation'])#index marks
d={'time':'1,9',
   'date':'01',
   'company':'none'}
d['age']='10'
d['ages']='2'#append
for i in d:
    print(i,'\t',d[i])#one i equal to change another line
p={1:''}#spell them all
k=dict(name='',joke='')#the key must be strings
j=dict([])
j['name']='d'
j['personality']='s'#step by step
s=dict(zip([1,2,3],['2','hi','du']))
s=list(s)# when change the type use the"list'
print(s)
m=list[1,3,3,'23']
print(m)
n=[1,2,'333',20,3932,'hihi']
n.remove(1)# 1 个
print(n)
myfile=open('summary.txt','w')
myfile.write('hello,good morning')#one sentence one time
myfile.write('goodbye')
myfile.close()
myfile=open('summary.txt','r')#'r is default
myfile.readline()
open('summary.txt').read()
print(open('summary.txt').read())
for line in open('summary.txt'):#file iterator
    print(line)