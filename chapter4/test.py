list1=['京A32178','京C43252','京F4323g','浙S3253g','粤Ah345']
for item in list1:
    s=item[0]
    print(item,'belong to:',s)
a="Happy new year,happy Chinese new year."
b=input("search for:").upper()
c=a.upper().count(b)#put all letter into one format
print('we have{0}ge{1}'.format(c,b))
sheet1=[
    ['01','computer','apple','10000'],
    ['02','microwave', 'media', '3000'],
    ['03','refrigerator', 'hare', '9000']
]
print('index\tgoods\t\tbrands\t\tprice')
for item in sheet1:
    for i in item:
        print(i,end='\t\t')
    print()    #change line
print()
#formatting
print('index\tgoods\t\tbrands\t\tprice')
for item in sheet1:
    item[0]='0000'+item[0]
    item[3]='${0:.2f}'.format(item[3])
    for a in item:
        print(a,end='\t\t')
    print()
#https://www.zhihu.com/
import re
pattern1='https://www.\w*.com/'
d='jefbhjbsdaf^'
s=re.findall(pattern1,d)#list format
for item in s:
    print(item)