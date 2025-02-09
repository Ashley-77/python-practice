import re#正则表达式匹配有对应规则的文本，需要记忆替换方法，即写出模式字符串
#match from the beginning,if the needed string is in the middle of the object,it fails
pattern='\w+@\w+\.\w+'
i='www.19@109'
match1=re.match(pattern,i,0)
print(match1)
#findall function,finding from the total string ,forming a list .should be correct
import re
text = "abc123def456"
numbers = re.findall("\d", text)#\d=find all numbers
print(numbers)
m=re.findall('\d+',text)#seperated numbers,123not1\2\3
print(m)
#sub replace sth
t2='2138的撒93时刻记得受极端'
pattern1="极端|死亡"
w=re.sub(pattern1,"xx",t2)#clean the illegal string
print(w)
k=re.sub('\w','$',text,2)#w:character or number 2ge substitute
print(k)
k=re.sub('\W','$',text,2)#2ge substitute
print(k)
#match
a=input('phone number:')
if re.match('\d{0,11}|\w{2}',a):#正则，正确的规则，验证格式least and most,几个的范围都行
    print('valid')
else:
    print('invalid')
id_number = "110101199001011234"
# 简单的18位身份证号码格式验证正则表达式，实际验证更复杂
pattern = '^\d{17}(\d|X)$'#开头^,end $ or|
if re.match(pattern, id_number):
    print("身份证号码格式正确")
else:
    print("身份证号码格式错误")
j=re.match('\s',id_number)#space blank
print(j)
j=re.match('\S',id_number)#not blank
print(j)
p='hahaaaaha color'
d=re.match('ha*ha',p)
print(d)
print(d.group(),j.group())#really print out,match\search need group,others not
#search any place in the string,just search one string
y='happy new year，happy2024'
l=re.search('\d{4}',y)
print(l.group())
pattern2='[.,/?|0-3|\d useless]'#区间字符串
pattern3='[^0-4]'#exclude mark
f=".dsfhgnc328"
n=re.findall(pattern2,f)
print(n)
m=re.search(pattern3,f)
print(m.group())#search\match need
j=re.split(pattern3,f)#split by the rule including
print(j)#list format
